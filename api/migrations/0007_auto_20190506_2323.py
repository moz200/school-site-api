# Generated by Django 2.2.1 on 2019-05-06 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190506_2212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['id'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='subjectcategory',
            options={'ordering': ['id'], 'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
    ]