from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required     # 로그인 상황을 보장하기 위한 코드
def profile(request):
    return render(request, 'accounts/profile.html')
