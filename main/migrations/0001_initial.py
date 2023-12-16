# Generated by Django 4.2.7 on 2023-12-05 21:28

import cloudinary.models
from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Center",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "main_route",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                ("code", models.CharField(max_length=100, null=True)),
                ("descriptio", models.CharField(max_length=100, null=True)),
                ("status", models.CharField(max_length=100, null=True)),
                ("photo_name", models.CharField(default="", max_length=255)),
                ("photo_url", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
            ],
            options={
                "verbose_name_plural": "Centers",
            },
        ),
        migrations.CreateModel(
            name="Clients",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pon_type", models.CharField(blank=True, default="", max_length=254)),
                ("name", models.CharField(blank=True, default="", max_length=254)),
                ("olt", models.CharField(blank=True, default="", max_length=254)),
                ("zone", models.CharField(blank=True, default="", max_length=254)),
                ("address", models.CharField(blank=True, default="", max_length=254)),
                (
                    "building_t",
                    models.CharField(blank=True, default="", max_length=254),
                ),
                ("latitude", models.FloatField(blank=True, default="")),
                ("longitude", models.FloatField(blank=True, default="")),
                ("odb_split", models.CharField(blank=True, default="", max_length=254)),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPointField(srid=4326),
                ),
            ],
            options={
                "verbose_name_plural": "Clients",
            },
        ),
        migrations.CreateModel(
            name="Closures",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("closore_na", models.CharField(default="", max_length=254)),
                (
                    "installati",
                    models.CharField(blank=True, default="", max_length=254),
                ),
                ("condition", models.CharField(blank=True, default="", max_length=254)),
                ("latitude", models.FloatField(blank=True, default="")),
                ("longitude", models.FloatField(blank=True, default="")),
                ("photo_name", models.CharField(default="", max_length=255)),
                ("photo_url", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPointField(srid=4326),
                ),
            ],
            options={
                "verbose_name_plural": "Closures",
            },
        ),
        migrations.CreateModel(
            name="Fats",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fat_name", models.CharField(blank=True, default="", max_length=254)),
                (
                    "installati",
                    models.CharField(blank=True, default="", max_length=254),
                ),
                ("condition", models.CharField(blank=True, default="", max_length=254)),
                ("latitude", models.FloatField(blank=True, default="", null=True)),
                ("longitude", models.FloatField(blank=True, default="", null=True)),
                ("photo_name", models.CharField(default="", max_length=255)),
                ("photo_url", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPointField(srid=4326),
                ),
            ],
            options={
                "verbose_name_plural": "Fats",
            },
        ),
        migrations.CreateModel(
            name="Mains",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, default="", max_length=100)),
                ("types", models.CharField(blank=True, default="", max_length=100)),
                ("length", models.FloatField(blank=True, default=None, null=True)),
                ("comment", models.CharField(blank=True, default="", max_length=100)),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326),
                ),
            ],
            options={
                "verbose_name_plural": "Mains",
            },
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("timestamp", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Routes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "route_name",
                    models.CharField(blank=True, default="", max_length=100),
                ),
                ("length", models.FloatField(blank=True, default=None, null=True)),
                (
                    "service_av",
                    models.CharField(blank=True, default="", max_length=100),
                ),
                ("installati", models.DateField(null=True)),
                ("bandwidth", models.FloatField(null=True)),
                ("status", models.CharField(blank=True, default="", max_length=100)),
                ("olt", models.CharField(blank=True, default="", max_length=100)),
                ("comment", models.CharField(blank=True, default="", max_length=100)),
                (
                    "infrasturc",
                    models.CharField(blank=True, default="", max_length=100),
                ),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326),
                ),
            ],
            options={
                "verbose_name_plural": "Routes",
            },
        ),
        migrations.CreateModel(
            name="Splitters",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "spliter_na",
                    models.CharField(blank=True, default="", max_length=254),
                ),
                (
                    "spliter_ty",
                    models.CharField(blank=True, default="", max_length=254),
                ),
                (
                    "no_of_port",
                    models.CharField(blank=True, default="", max_length=254),
                ),
                (
                    "installati",
                    models.CharField(blank=True, default="", max_length=254),
                ),
                ("condition", models.CharField(blank=True, default="", max_length=254)),
                ("latitude", models.FloatField(blank=True, default="")),
                ("longitude", models.FloatField(blank=True, default="")),
                ("photo_name", models.CharField(default="", max_length=255)),
                ("photo_url", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPointField(srid=4326),
                ),
            ],
            options={
                "verbose_name_plural": "Splitters",
            },
        ),
        migrations.CreateModel(
            name="Zones",
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
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("photo_name", models.BigIntegerField()),
                ("photo_url", models.CharField(max_length=200)),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
            ],
            options={
                "verbose_name_plural": "Zones",
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "profile_pic",
                    models.ImageField(blank=True, null=True, upload_to="media/"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "UserProfiles",
            },
        ),
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("photo_name", models.CharField(max_length=255, unique=True)),
                (
                    "image",
                    cloudinary.models.CloudinaryField(
                        blank=True, max_length=255, null=True, verbose_name="image"
                    ),
                ),
                (
                    "center",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.center",
                    ),
                ),
                (
                    "closure",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.closures",
                    ),
                ),
                (
                    "fat",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.fats",
                    ),
                ),
                (
                    "splitter",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.splitters",
                    ),
                ),
            ],
        ),
    ]
