from django.contrib import admin
from .models import Post,Category,Tag,Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # 자동으로 채워주는 역할을 하는 field

admin.site.register(Category,CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Tag,TagAdmin)

