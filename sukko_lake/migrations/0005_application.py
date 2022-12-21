# Generated by Django 4.1.4 on 2022-12-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sukko_lake', '0004_alter_fakeusers_photo_alter_mainpicture_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50)),
                ('client_number', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('W', 'В работе'), ('WO', 'Отработана')], default='W', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Заявки от клиента',
            },
        ),
    ]
