from rest_framework import viewsets, filters, mixins
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated

from sharo.permissions import IsStaff
from sharo.serializers import QuestionSerializer, StageSerializer, CategorySerializer, AnswerSerializer, \
    AdminAnswerSerializer

class QuestionViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin):
    serializer_class = QuestionSerializer
    queryset = serializer_class.Meta.model.objects.public().prefetch_related("category_set", "stage_set")
    permission_classes = (IsAuthenticated,)

    filter_backends = (filters.DjangoFilterBackend)
    filter_fields = ("category", "stage")

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        super(QuestionViewSet,self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        super(QuestionViewSet,self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="This method use only admin.")
        super(QuestionViewSet,self).partial_update(request, *args, **kwargs)


class StageReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StageSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = (IsAuthenticated,)

class CategoryReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = (IsAuthenticated,)

class AnswerWriteOnlyViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = AnswerSerializer
    queryset = serializer_class.Meta.model.objects.all(id=-1)
    permission_classes = (IsAuthenticated,)


class AdminAnswerReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AdminAnswerSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes =  (IsStaff,)

