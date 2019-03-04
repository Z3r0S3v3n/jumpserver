# Generated by Django 2.1.7 on 2019-02-28 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessKey',
            fields=[
                ('id',
                 models.UUIDField(default=uuid.uuid4, editable=False,
                                  primary_key=True, serialize=False,
                                  verbose_name='AccessKeyID')),
                ('secret',
                 models.UUIDField(default=uuid.uuid4, editable=False,
                                  verbose_name='AccessKeySecret')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='access_keys',
                    to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='PrivateToken',
            fields=[
                ('key',
                 models.CharField(max_length=40, primary_key=True,
                                  serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True,
                                                 verbose_name='Created')),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='auth_token',
                    to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Private Token',
            },
        ),
    ]
