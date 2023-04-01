from rest_framework import generics
from .models import Project, Image, Language, Contact, Service, Skill
from .serializers import ProjectSerializer, ImageSerializer, LanguageSerializer, ContactSerializer
from .serializers import ServiceSerializer, SkillSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser, AllowAny

# Create your views here.

# language view sets...
class LanguageViewSet(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes=[IsAuthenticated]

# single language view sets...
class SingleLanguageViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    lookup_field='pk'
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
# project main view sets...
class ProjectViewSet(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    
# single project main view sets...
class SingleProjectViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    lookup_field='pk'
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
# images view sets...
class ImageViewSet(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes=[IsAuthenticated, IsAdminUser]
    
# single images view sets...
class SingleImageViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes=[IsAuthenticated, IsAdminUser]
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
        
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
# contact create view sets...
class ContactViewSet(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        return super(ContactViewSet, self).get_permissions()

# service view sets...
class ServiceViewsSet(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    
# single service view sets...
class SingleServiceViewsSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

# skill view sets...
class SkillViewsSet(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

# single skill view sets...
class SingleSkillViewsSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    lookup_field='pk'
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)