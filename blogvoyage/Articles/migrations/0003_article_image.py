# Generated by Django 4.1.2 on 2023-03-15 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0002_rename_articles_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='animal.jpg', upload_to=''),
        ),
    ]
