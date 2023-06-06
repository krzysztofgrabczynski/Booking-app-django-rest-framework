# Generated by Django 4.2.1 on 2023-06-06 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_roomreservation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roomreservation",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="room_reservation",
                to="api.hotelroommodel",
            ),
        ),
    ]