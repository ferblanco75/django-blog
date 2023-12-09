from rest_framework import status
#APIview tengo varios metodos get, post, put, delete
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer

class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


"""" class PostApiView(APIView):
    def get(self, request):
        #posts = Post.objects.all()
        serializer = PostSerializer(Post.objects.all(), many=True)
        # posts= [post.title for post in Post.objects.all()]
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
       new_post = PostSerializer(data=request.POST)
       new_post.is_valid(raise_exception=True)
       new_post.save()
       return Response(status=status.HTTP_200_OK, data=new_post.data)"""

"""class PostViewSet(ViewSet):
    def list(self, request):
        #posts = Post.objects.all()
        serializer = PostSerializer(Post.objects.all(), many=True)
        # posts= [post.title for post in Post.objects.all()]
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk: int):
        post = PostSerializer(Post.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=post.data)

    def create(self, request):
       new_post = PostSerializer(data=request.POST)
       new_post.is_valid(raise_exception=True)
       new_post.save()
       return Response(status=status.HTTP_200_OK, data=new_post.data)"""