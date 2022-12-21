# Generated by Django 4.1.4 on 2022-12-17 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FakeUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='fake_user_photo/')),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name': 'Фейковые пользователи',
            },
        ),
        migrations.CreateModel(
            name='MainPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='main_picture/')),
                ('description', models.CharField(blank=True, max_length=300)),
            ],
            options={
                'verbose_name': 'Изображения из карусели',
            },
        ),
        migrations.CreateModel(
            name='FakeFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=50)),
                ('feedback_body', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sukko_lake.fakeusers')),
            ],
            options={
                'verbose_name': 'Фейковые пользователи',
            },
        ),
    ]
