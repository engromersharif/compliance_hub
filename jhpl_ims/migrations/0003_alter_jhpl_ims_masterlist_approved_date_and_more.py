# Generated by Django 4.2.3 on 2023-07-24 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "jhpl_ims",
            "0002_doc_controller_created_at_doc_controller_updated_at_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="jhpl_ims_masterlist",
            name="approved_date",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="jhpl_ims_masterlist",
            name="issue_date",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="jhpl_ims_masterlist",
            name="reviewed_date",
            field=models.DateTimeField(),
        ),
    ]
