from django.contrib import admin
from .models import Post

@admin.register(Post)
# admin페이지에서 post어떻게 보일지 설정
class PostAdmin(admin.ModelAdmin):
    list_display=['id', 'title']    # 아이디랑 제목 보임
    list_display_links=['title']    # 제목에 링크건다
    search_fields = ['title']       # 제목에 있는 단어로 검색

# Register your models here.
