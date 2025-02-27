# Generated by Django 4.2 on 2025-01-30 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0002_alter_settings_description_contact_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Form",
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
                ("name", models.CharField(max_length=155)),
                ("info", models.CharField(max_length=255)),
                ("comment", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name_plural": "Формула обраного",
            },
        ),
    ]
