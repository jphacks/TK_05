from rest_framework import viewsets

from sharo.serializers import QuestionSerializer


class QuestionReadOnlyViewSet():
    serializer_class = QuestionSerializer
    queryset = serializer_class.Meta.model.objects.public().prefetch_related("category_set", "stage_set")

