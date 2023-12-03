# Generated by Django 4.2.7 on 2023-12-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TeamMember",
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
                ("phone_number", models.IntegerField(unique=True)),
                ("email", models.EmailField(max_length=100, unique=True)),
                (
                    "role",
                    models.CharField(
                        choices=[("admin", "ADMIN"), ("regular", "REGULAR")],
                        default="regular",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
