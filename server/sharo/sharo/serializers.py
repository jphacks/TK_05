from rest_framework import serializers

from sharo import models


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        field = ('id', 'screen_name', 'email', 'points', 'icon', 'last_scored')
        read_only_fields = ('id', 'points', 'last_scored')


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

#TODO: Admin's QuestionSerializerを実装する
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = "__all__"
        read_only_fields = "__all__"

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = "__all__"
        read_only_fields = "__all__"

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
        read_only_fields = ('id', )

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notice
        fields = "__all__"
        read_only_fields = ('id', 'updated_at', 'created_at')

#TODO: Admin's WriteUpSerializerを実装する
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
