from rest_framework.response import Response
from rest_framework.decorators import api_view
from myawards.models import Project, Profile, Rating
from .serializers import ProfileSerializer, ProjectSerializer, RatingSerializer, UserSerializer
from django.contrib.auth.models import User


# api_views here
@api_view(['GET'])
def GetProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def GetUserDetails(request,pk):
    profile = User.objects.get(id=pk)
    serializer = UserSerializer(profile, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def GetProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def GetSpecificProject(request,id):
    article = Projects.objects.get(id=id)
    serializer = ProjectSerializer(article, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def GetSpecificRating(request,pk):
    rating = Rating.objects.filter(project_id=pk)
    serializer = RatingSerializer(rating, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def GetUserProjects(request,pk):
    projects = Projects.objects.filter(owner_id=pk)
    serializer = ProjectSerializer(projects, many = True)
    return Response(serializer.data)
