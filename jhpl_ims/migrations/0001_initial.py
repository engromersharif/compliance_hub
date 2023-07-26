# Generated by Django 4.2.3 on 2023-07-23 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="doc_controller",
            fields=[
                (
                    "doc_controller_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="jhpl_ims_masterlist",
            fields=[
                (
                    "ims_masterlist_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("doc_num", models.IntegerField()),
                ("doc_title", models.CharField(blank=True, max_length=200, null=True)),
                ("rev_num", models.IntegerField()),
                ("issue_date", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(max_length=10)),
                ("approved_date", models.DateTimeField(auto_now=True)),
                ("reviewed_date", models.DateTimeField(auto_now=True)),
                ("control_copy_num", models.IntegerField()),
                (
                    "approved_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="jhpl_approved_by",
                        to="jhpl_ims.doc_controller",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "reviewed_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="jhpl_reviewed_by",
                        to="jhpl_ims.doc_controller",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="notes",
            fields=[
                ("notes_id", models.AutoField(primary_key=True, serialize=False)),
                ("large_text_body", models.TextField()),
                (
                    "jhpl_ims_masterlist_key",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jhpl_ims.jhpl_ims_masterlist",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]