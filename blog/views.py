from django.shortcuts import render
from django.views.generic import *
from .models import *

## 빠르게 만들기 위해 클래스 기반 뷰
post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)