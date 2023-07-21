from django.contrib import admin
from post.models import Post ,IMG

class PhotoInline(admin.StackedInline):
    model = IMG
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'upload_date','tag_list','slug')
    list_fliter = ('upload_date')
    prepopulated_fields = {'slug' : ('title',)}
    inlines = (PhotoInline,)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tag')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tag.all())



@admin.register(IMG)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'image', 'owner', 'pk')
    # Register your models here.
