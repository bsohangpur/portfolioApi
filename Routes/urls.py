from django.urls import path
from . import views


urlpatterns = [
    path('languages/', views.LanguageViewSet.as_view()),
    path('languages/<int:pk>/', views.SingleLanguageViewSet.as_view()),
    path('projects/', views.ProjectViewSet.as_view()),
    path('projects/<int:pk>/', views.SingleProjectViewSet.as_view()),
    path('images/', views.ImageViewSet.as_view()),
    path('images/<int:pk>/', views.SingleImageViewSet.as_view(), name="image_route"),
    path('contacts/', views.ContactViewSet.as_view()),
    path('services/', views.ServiceViewsSet.as_view()),
    path('services/<int:pk>/', views.SingleServiceViewsSet.as_view()),
    path('skills/', views.SkillViewsSet.as_view()),
    path('skills/<int:pk>/', views.SingleSkillViewsSet.as_view()),
]
