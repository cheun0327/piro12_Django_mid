
from django.conf import settings
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.db import models

class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    website_url = models.URLField(blank=True)

def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:   #처음 생성이 되었을 때 = 가입시기
        user=kwargs['instance']
        Profile.objects.create(user=user)

        # 프로필 생성 후에 환영 이메일 보내는 부분
        send_mail(
            '가입을 환영합니다!',
            'Here is the message',
            'me@askcompany.kr',
            [user.email],
            fail_silently=False,
        )

post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)