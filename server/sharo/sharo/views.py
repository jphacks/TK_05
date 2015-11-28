from rest_framework import viewsets, filters, mixins
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny

from sharo.models import Flag, Answer
from sharo.permissions import IsStaff
from sharo.serializers import QuestionSerializer, StageSerializer, CategorySerializer, AnswerSerializer, \
    AdminAnswerSerializer, FlagSerializer, FileSerializer, ImportanceSerializer, NoticeSerializer, WriteUpSerializer, \
    CommentSerializer


# FIXME: 関数レベルでIsStaffを確認するデコレータを作る
# FIXME: というかStaffならEditを許可するViewSetを作る

class AuthViewSet(viewsets.ViewSet):
    def list(self):
        pass


class QuestionViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin):
    serializer_class = QuestionSerializer
    queryset = serializer_class.Meta.model.objects.public().prefetch_related("category_set", "stage_set")
    permission_classes = (IsAuthenticated,)

    filter_backends = (filters.DjangoFilterBackend)
    filter_fields = ("category", "stage")

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(QuestionViewSet,self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(QuestionViewSet,self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(QuestionViewSet,self).partial_update(request, *args, **kwargs)


class StageViewSet(viewsets.ModelViewSet):
    serializer_class = StageSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(StageViewSet,self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(StageViewSet,self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(StageViewSet,self).partial_update(request, *args, **kwargs)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(CategoryViewSet,self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(CategoryViewSet,self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(CategoryViewSet,self).partial_update(request, *args, **kwargs)

class AnswerWriteOnlyViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = AnswerSerializer
    queryset = serializer_class.Meta.model.objects.all(id=-1)
    permission_classes = (IsAuthenticated,)


class AdminAnswerReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AdminAnswerSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes =  (IsStaff,)

class FlagModelViewSet(viewsets.ModelViewSet):
    serializer_class = FlagSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes =  (IsStaff,)

class FileReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FileSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes =  (AllowAny,)

class ImportanceViewSet(viewsets.ModelViewSet):
    serializer_class = ImportanceSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes =  (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(ImportanceViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(ImportanceViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(ImportanceViewSet, self).destroy(request, *args, **kwargs)

class NoticeViewSet(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes =  (AllowAny,)

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(NoticeViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(NoticeViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        return super(NoticeViewSet, self).destroy(request, *args, **kwargs)


class WriteUpViewSet(viewsets.ModelViewSet):
    serializer_class = WriteUpSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes =  (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if request.user.is_staff or (Flag.objects.filter(question=request.data['question']).count() == Answer.objects.filter(is_correct=True, user=request.user)):
            return super(WriteUpViewSet, self).create(request, *args, **kwargs)
        raise PermissionDenied(detail="You don't submit all flag in this question.")

    def update(self, request, *args, **kwargs):
        if request.user.is_staff or (Flag.objects.filter(question=request.data['question']).count() == Answer.objects.filter(is_correct=True, user=request.user)):
            return super(WriteUpViewSet, self).create(request, *args, **kwargs)
        raise PermissionDenied(detail="You don't submit all flag in this question.")

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff or (Flag.objects.filter(question=request.data['question']).count() == Answer.objects.filter(is_correct=True, user=request.user)):
            return super(WriteUpViewSet, self).create(request, *args, **kwargs)
        raise PermissionDenied(detail="You don't submit all flag in this question.")

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes =  (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if request.user.is_staff or (Flag.objects.filter(question=request.data['question']).count() == Answer.objects.filter(is_correct=True, user=request.user)):
            return super(CommentViewSet, self).create(request, *args, **kwargs)
        raise PermissionDenied(detail="You don't submit all flag in this question.")

    def update(self, request, *args, **kwargs):
        if request.user.is_staff or (Flag.objects.filter(question=request.data['question']).count() == Answer.objects.filter(is_correct=True, user=request.user)):
            return super(CommentViewSet, self).create(request, *args, **kwargs)
        raise PermissionDenied(detail="You don't submit all flag in this question.")

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff or (Flag.objects.filter(question=request.data['question']).count() == Answer.objects.filter(is_correct=True, user=request.user)):
            return super(CommentViewSet, self).create(request, *args, **kwargs)
        raise PermissionDenied(detail="You don't submit all flag in this question.")
