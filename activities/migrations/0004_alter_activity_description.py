# Generated by Django 3.2.7 on 2021-09-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0003_alter_activity_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
