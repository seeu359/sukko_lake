# Generated by Django 4.1.4 on 2022-12-21 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sukko_lake', '0011_alter_mainpicture_options_alter_fakefeedback_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fakefeedback',
            old_name='user_id',
            new_name='user',
        ),
    ]
