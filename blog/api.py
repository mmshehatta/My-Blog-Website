
from .models import Post
from .serializers import PostSerialiser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics



@api_view(['GET'])
def post_list_api(request):
    all_posts = Post.objects.all()
    data = PostSerialiser(all_posts, many=True).data
    return Response({'data':data})


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiser
