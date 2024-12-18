# Generated by Django 5.1.3 on 2024-12-10 11:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblogging_app', '0005_rename_user_id_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(default=models.F('user__username'), max_length=255),
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('profil_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Bio', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='images/')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
