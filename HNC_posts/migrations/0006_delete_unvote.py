# Generated by Django 3.2.5 on 2021-09-09 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HNC_posts', '0005_unvote_vote'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Unvote',
        ),
    ]
