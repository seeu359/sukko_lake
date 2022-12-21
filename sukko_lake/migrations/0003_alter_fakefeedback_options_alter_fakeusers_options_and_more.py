# Generated by Django 4.1.4 on 2022-12-17 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sukko_lake', '0002_fakefeedback_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fakefeedback',
            options={'verbose_name_plural': 'Фейковые отзывы'},
        ),
        migrations.AlterModelOptions(
            name='fakeusers',
            options={'verbose_name_plural': 'Фейковые пользователи'},
        ),
        migrations.AlterModelOptions(
            name='mainpicture',
            options={'verbose_name_plural': 'Изображения из карусели'},
        ),
        migrations.AlterField(
            model_name='fakeusers',
            name='photo',
            field=models.ImageField(upload_to='media/fake_user_photo/'),
        ),
        migrations.AlterField(
            model_name='mainpicture',
            name='description',
            field=models.CharField(help_text='Описание фото.Обязательное поле.Будет располагаться под названием в карусели', max_length=300),
        ),
        migrations.AlterField(
            model_name='mainpicture',
            name='name',
            field=models.CharField(help_text='Название фото.Обязательное поле. Будет выделено жирным шрифтом на фото в карусели.', max_length=50),
        ),
    ]