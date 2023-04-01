from rest_framework import serializers
from .models import Project, Image, Language, Contact, Service, Skill

# image serializer...
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

# Project category serializer...
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

# Project main serializer...
class ProjectSerializer(serializers.ModelSerializer):
    languageAndTool = LanguageSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    languageAndToolIds = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all(),
        many=True,
        write_only=True,
        source='languageAndTool'
    )
    imageIds = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(),
        many=True,
        write_only=True,
        source='images'
    )
    
    class Meta:
        model = Project
        fields = '__all__'

# contact serializer
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


# service serializer
class ServiceSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    imageIds = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(),
        many=True,
        write_only=True,
        source='images'
    )
    
    class Meta:
        model = Service
        fields = "__all__"

# skill serializer
class SkillSerializer(serializers.ModelSerializer):
    title= LanguageSerializer(read_only=True)
    image = ImageSerializer(read_only=True)
    titleid = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all(),
        write_only=True,
        source='title'
    )
    imageId = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(),
        write_only=True,
        source='image'
    )

    class Meta:
        model = Skill
        fields = "__all__"

