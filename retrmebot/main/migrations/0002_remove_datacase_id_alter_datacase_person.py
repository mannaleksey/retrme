# Generated by Django 4.1.7 on 2023-03-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datacase',
            name='id',
        ),
        migrations.AlterField(
            model_name='datacase',
            name='person',
            field=models.CharField(default='', max_length=64, primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]
