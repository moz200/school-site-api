# Generated by Django 2.2.1 on 2019-05-06 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190505_2045'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subject',
            new_name='SubjectCategory',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='miniBody',
            new_name='mini_body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subject_id',
        ),
        migrations.AddField(
            model_name='post',
            name='subject_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.SubjectCategory', verbose_name='Предмет'),
        ),
    ]
