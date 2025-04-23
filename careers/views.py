from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Career
from .serializers import CareerGetSerializer, CareerPostSerializer, CareerPatchSerializer


class CareerView(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ["username",]
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CareerPostSerializer
        return CareerGetSerializer


class CareerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerPatchSerializer
    http_method_names = ['patch', 'delete']
