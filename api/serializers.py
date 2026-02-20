from rest_framework.serializers import ModelSerializer
from main.models import Project, ContactMessage

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ContactMessageSerializer(ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
