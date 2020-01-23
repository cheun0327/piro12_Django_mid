from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email


class SignupForm(UserCreationForm):

    def clean_username(self):       # 이메일 형식 검사
        value = self.cleaned_data.get('username')
        if value:       # 값이 있을 경우
            validate_email(value)
        return value

    def save(self, commit=True):        # 이메일 필드에 이메일 저장 추가
        user=super().save(commit=False)
        user.email=user.username
        if commit:
            user.save()
        return user

    '''
    def __init__(self, *args, **kwargs):
        super().__init__(self,*args,**kwargs)
        self.fields['username'].validators = [validate_email]
        self.fields['username'].help_text = 'Enter Email Format'
        '''