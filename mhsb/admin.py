from django.contrib import admin
from .models import Post_1,Post_2,Post_3,Post_4,Comment_1,Comment_2,Comment_3,Comment_4

class PostAdmin_1(admin.ModelAdmin):
    search_fields = ['id']
    
admin.site.register(Post_1, PostAdmin_1)

class PostComment_1(admin.ModelAdmin):
    search_fields = ['id']
    search_fields = ['message']
    
admin.site.register(Comment_1, PostComment_1)
    
    


class PostAdmin_2(admin.ModelAdmin):
    search_fields = ['id']
    
admin.site.register(Post_2, PostAdmin_2)

class PostComment_2(admin.ModelAdmin):
    search_fields = ['id']
    search_fields = ['message']
    
admin.site.register(Comment_2, PostComment_2)





class PostAdmin_3(admin.ModelAdmin):
    search_fields = ['id']
    
admin.site.register(Post_3, PostAdmin_3)

class PostComment_3(admin.ModelAdmin):
    search_fields = ['id']
    search_fields = ['message']
    
admin.site.register(Comment_3, PostComment_3)





class PostAdmin_4(admin.ModelAdmin):
    search_fields = ['id']
    
admin.site.register(Post_4, PostAdmin_4)

class PostComment_4(admin.ModelAdmin):
    search_fields = ['id']
    search_fields = ['message']
    
admin.site.register(Comment_4, PostComment_4)