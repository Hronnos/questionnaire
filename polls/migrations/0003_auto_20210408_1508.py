# Generated by Django 3.1.7 on 2021-04-08 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_donehomework_homework_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='student_hw',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.donehomework'),
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
