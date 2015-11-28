from datetime import datetime
from django.contrib.auth import login
from rest_framework import serializers
from sharo import models
from sharo.models import Flag, Answer, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'screen_name', 'email', 'points', 'icon', 'last_scored', 'is_staff')
        read_only_fields = ('id', 'points', 'last_scored')
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        is_staff = data.pop('is_staff', False)
        user = self.context.get('request').user

        if is_staff and not user.is_staff:
            raise serializers.ValidationError(detail="You don't have permission, Are you BlackHat? ;(")

        data['is_staff'] = is_staff

        return data

    def create(self, validated_data):
        request = self.context.get('request')

        username = validated_data['email']

        user = User(validated_data, username=username)
        user.set_password(validated_data['password'])
        user.save()

        # login new user
        login(request, user)

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        i = super(UserSerializer, self).update(instance, validated_data)
        if password:
            i.set_password(password)
        i.save()

        return i


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
        read_only_fields = ('id', 'updated_at', 'created_at')


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stage
        fields = '__all__'
        read_only_fields = ('id', 'updated_at', 'created_at')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = "__all__"
        read_only_fields = ('id', 'updated_at', 'created_at')


class AdminAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = "__all__"
        read_only_fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ("question", "answer")

    def validate(self, data):
        question = data['question']
        login_user = self.context.get('request').user

        try:
            flag = Flag.objects.get(question=question, flag=data['answer'])
        except models.Flag.DoesNotExist:
            answer = Answer(user=login_user, question=question, flag=None)
            answer.save()
            raise serializers.ValidationError(detail="The answer isn't correct.")

        # 重複防止
        if flag and Flag.objects.filter(user=login_user, flag=flag):
            raise serializers.ValidationError(detail="This flag had been submitted.")

        return data

    def create(self, validated_data):
        user = self.context.get('request').user
        question = validated_data['question']
        answer = validated_data['answer']

        try:
            flag = Flag.objects.get(question=question, answer=answer)
        except Flag.DoesNotExist:
            pass

        if flag:
            user.last_scored = datetime.now()
            user.save()

        a = Answer(user=user, question=question, answer=answer)
        a.save()

        return a


class FlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Flag
        fields = "__all__"
        read_only_fields = ('id', 'updated_at', 'created_at')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = ('id', 'name', 'url', 'question', 'updated_at', 'created_at')
        read_only_fields = ('id', 'url', 'updated_at', 'created_at')


class ImportanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Importance
        fields = ('id', 'priority', 'name')
        read_only_fields = ('id',)


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notice
        fields = "__all__"
        read_only_fields = ('id', 'updated_at', 'created_at')


# TODO: Admin's WriteUpSerializerを実装する
class WriteUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WriteUp
        fields = "__all__"
        read_only_fields = ('id', 'updated_at', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"
        read_only_fields = ('id', 'created_at', 'updated_at')
