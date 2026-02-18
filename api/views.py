from rest_framework.generics import ListAPIView, RetrieveAPIView
from main.models import Project
from .serializers import ProjectSerializer

class ProjectListAPI(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailAPI(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
