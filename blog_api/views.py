from rest_framework import generics
from rest_framework import permissions
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissions

# Create your views here.

#custom permissions
class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        #safe_methods are get options and head
        if request.method in SAFE_METHODS:
            return True #if it is true, user can view the data. 
  
        return obj.author == request.user #else for other req, it will test this.
        
        
class PostList(generics.ListCreateAPIView):
    #permission_classes = [DjangoModelPermissions] 
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission): 
    permission_classes = [PostUserWritePermission] 
    queryset = Post.objects.all() 
    serializer_class = PostSerializer

