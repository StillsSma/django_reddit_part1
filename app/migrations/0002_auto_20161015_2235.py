# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 22:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=255)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('subreddit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Subreddit')),
            ],
            options={
                'ordering': ('-creation_time',),
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Post'),
        ),
    ]
