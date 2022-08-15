# Generated by Django 3.2.15 on 2022-08-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Teacher', 'verbose_name_plural': 'Teachers'},
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.CharField(max_length=10, verbose_name='Group'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(max_length=10, verbose_name='Lesson'),
        ),
    ]
