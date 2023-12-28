# Generated by Django 4.2.5 on 2023-12-21 10:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_on", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("created_by", models.UUIDField(blank=True, null=True)),
                ("updated_on", models.DateTimeField(auto_now=True, db_index=True)),
                ("updated_by", models.UUIDField(blank=True, null=True)),
                ("deleted_on", models.DateTimeField(blank=True, db_index=True, null=True)),
                ("deleted_by", models.UUIDField(blank=True, null=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
            options={
                "verbose_name_plural": "Employees",
                "db_table": "app_employee",
            },
        ),
    ]