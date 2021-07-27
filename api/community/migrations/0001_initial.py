# Generated by Django 3.2 on 2021-07-27 15:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Member",
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
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("title", models.CharField(max_length=150)),
                (
                    "email",
                    models.EmailField(db_index=True, max_length=255, unique=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewsItem",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(default="", max_length=100)),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_community.newsitem_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
        ),
        migrations.CreateModel(
            name="Announcement",
            fields=[
                (
                    "newsitem_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="community.newsitem",
                    ),
                ),
                ("preview", models.TextField(max_length=500)),
                ("publication_date", models.DateField()),
                ("link", models.CharField(max_length=300)),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("community.newsitem",),
        ),
        migrations.CreateModel(
            name="Organization",
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
                ("title", models.CharField(blank=True, max_length=150)),
                ("description", models.TextField(blank=True, null=True)),
                ("website", models.CharField(blank=True, max_length=300)),
                ("facebook", models.CharField(blank=True, max_length=250)),
                ("instagram", models.CharField(blank=True, max_length=250)),
                ("discord", models.CharField(blank=True, max_length=250)),
                ("slack", models.CharField(blank=True, max_length=250)),
                ("slug", models.SlugField(default="", editable=False, unique=True)),
                ("members", models.ManyToManyField(blank=True, to="community.Member")),
                (
                    "announcements",
                    models.ManyToManyField(blank=True, to="community.Announcement"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "newsitem_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="community.newsitem",
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("start_time", models.DateTimeField(blank=True, null=True)),
                ("end_time", models.DateTimeField(blank=True, null=True)),
                ("location", models.TextField(blank=True, max_length=200, null=True)),
                ("link", models.CharField(max_length=300)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("finalized", "FINALIZED"),
                            ("in planning", "IN PLANNING"),
                        ],
                        default="in planning",
                        max_length=12,
                    ),
                ),
                ("poster", models.ImageField(blank=True, null=True, upload_to="event")),
                ("organization", models.ManyToManyField(to="community.Organization")),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("community.newsitem",),
        ),
    ]
