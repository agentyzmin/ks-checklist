# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.IntegerField(default=0)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=300)),
                ('ap_class', models.IntegerField()),
                ('state', models.CharField(max_length=30)),
                ('developer_offer', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('apartment', models.ManyToManyField(to='main.Apartment')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='apartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Apartment'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Question'),
        ),
    ]