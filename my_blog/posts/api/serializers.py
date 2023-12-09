from rest_framework.serializers import ModelSerializer
from posts.models import Post


#que hace el serializador? muy facil ,cuando uso el modelo post (que se lo indico) va a mandar estos campos

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        # django no recomienda usar fields = '__all__' porque si hay campos nuevos, lo agrega a las peticiones
        fields = ['title','description','created_at'] #estos son los campos que quiero utilizar

