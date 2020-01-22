from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import CreateView
from .forms import SignupForm


'''def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user=form.save()    
            # 이부분에서 회원가입이 완료됨 / 여기에서 로그인 처리 해주면됨
            auth_login(request, user)
            return redirect('profile')
    else:
        form=SignupForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })'''

class SignupView(CreateView):
    model=User
    form_class=SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return resolve_url('profile')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())

signup=SignupView.as_view()
@login_required     # 로그인 상황을 보장하기 위한 코드
def profile(request):
    return render(request, 'accounts/profile.html')
