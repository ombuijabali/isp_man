# Generated by Django 4.2.7 on 2023-12-07 17:57

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_clients_address_alter_clients_building_t_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Zone",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("input_fid", models.IntegerField()),
                ("id_1", models.BigIntegerField()),
                ("spliter_id", models.BigIntegerField()),
                ("spliter_na", models.CharField(max_length=254)),
                ("spliter_ty", models.CharField(max_length=254)),
                ("no_of_port", models.CharField(max_length=254)),
                ("installati", models.CharField(max_length=254)),
                ("condition", models.CharField(max_length=254)),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
            ],
            options={
                "verbose_name_plural": "Zones",
            },
        ),
        migrations.DeleteModel(
            name="Zones",
        ),
    ]