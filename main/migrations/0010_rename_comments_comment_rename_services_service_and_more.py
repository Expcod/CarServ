# Generated by Django 5.0.1 on 2024-01-27 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_booking_select'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
        migrations.RenameModel(
            old_name='Technicians',
            new_name='Technician',
        ),
    ]
