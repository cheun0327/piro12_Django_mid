from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', lambda req: redirect('/blog/')),   # 제일 첫 화면이 블로그
    # url reverse사용하면 좋다
]
