from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from sharo.serializers import QuestionSerializer


class QuestionReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer
    queryset = serializer_class.Meta.model.objects.public().prefetch_related("category_set", "stage_set")
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend)

