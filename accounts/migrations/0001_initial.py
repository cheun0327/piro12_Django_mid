# Generated by Django 2.2.9 on 2020-01-22 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

def forward_func(apps, schema_editor):
    # 모든 user에 대해 profile을 만들어 준다.
    auth_user_model = settings.AUTH_USER_MODEL.split('.')
    User=apps.get_model(*auth_user_model)
    Profile = apps.get_model('accounts', 'Profile')     ## unpacking해서 user model획득

    for user in User.objects.all():
        print('create profile for user#{}'.format(user.pk))
        Profile.objects.create(user=user)

def backward_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('website_url', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(forward_func, backward_func),
        ## migrate하자마자 forward, backward함수 호출 된다.
    ]
