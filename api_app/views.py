from rest_framework.decorators import api_view
from rest_framework.response import Response
from projects_app.models import Project
from .serializers import ProjectSerializer

@api_view(['GET'])
def projects_api(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)
