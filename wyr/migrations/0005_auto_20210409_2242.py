# Generated by Django 3.1.5 on 2021-04-09 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyr', '0004_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='voter',
            field=models.CharField(default='', max_length=64),
        ),
    ]