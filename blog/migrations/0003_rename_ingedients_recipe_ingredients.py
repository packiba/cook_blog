# Generated by Django 3.2.8 on 2021-10-15 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingedients',
            new_name='ingredients',
        ),
    ]