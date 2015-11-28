from rest_framework import viewsets, filters, mixins
from rest_framework.permissions import IsAuthenticated

from sharo.serializers import QuestionSerializer, StageSerializer, CategorySerializer, AnswerSerializer, \
    AdminAnswerSerializer


class QuestionReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer
    queryset = serializer_class.Meta.model.objects.public().prefetch_related("category_set", "stage_set")
    permission_classes = (IsAuthenticated,)

    filter_backends = (filters.DjangoFilterBackend)
    filter_fields = ("category", "stage")

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
    permission_classes =