# Generated by Django 2.2 on 2019-09-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0005_auto_20190913_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='published_data',
            field=models.DateTimeField(null=True),
        ),
    ]
