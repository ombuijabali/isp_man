# Generated by Django 4.2.7 on 2023-12-14 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_notification_changes"),
    ]

    operations = [
        migrations.RenameField(
            model_name="clients",
            old_name="name",
            new_name="client_nam",
        ),
        migrations.RenameField(
            model_name="mains",
            old_name="name",
            new_name="main_name",
        ),
    ]
