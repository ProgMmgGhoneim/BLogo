# Generated by Django 2.2 on 2019-09-12 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_model',
            old_name='tiile',
            new_name='title',
        ),
    ]