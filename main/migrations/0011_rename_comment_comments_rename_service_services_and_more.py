# Generated by Django 5.0.1 on 2024-01-27 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_comments_comment_rename_services_service_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comments',
        ),
        migrations.RenameModel(
            old_name='Service',
            new_name='Services',
        ),
        migrations.RenameModel(
            old_name='Technician',
            new_name='Technicians',
        ),
    ]
