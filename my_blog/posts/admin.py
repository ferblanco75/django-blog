from django.contrib import admin
from posts.models import Post

#añado un decorador
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #aca leindico que parametros o propiedades se van a visuelizar en el admin panel
    list_display = ['title', 'created_at']
