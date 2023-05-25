# Generated by Django 4.2.1 on 2023-05-25 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HotelModel",
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
                ("hotel_name", models.CharField(max_length=32, unique=True)),
                ("address", models.CharField(max_length=128)),
                (
                    "rate",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=4, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HotelRoomModel",
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
                ("room_no", models.SmallIntegerField()),
                ("capacity", models.PositiveSmallIntegerField()),
                ("description", models.TextField(default="")),
                ("price_per_night", models.PositiveIntegerField()),
                ("is_available", models.BooleanField(default=True)),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hotel_room",
                        to="api.hotelmodel",
                    ),
                ),
            ],
        ),
    ]
