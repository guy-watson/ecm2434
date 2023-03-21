# Generated by Django 4.1.7 on 2023-03-17 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("prof", "0003_alter_userprofile_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="friendrequest",
            name="created_at",
        ),
        migrations.AlterField(
            model_name="friendrequest",
            name="from_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="from_user",
                to="prof.user",
            ),
        ),
        migrations.AlterField(
            model_name="friendrequest",
            name="to_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="to_user",
                to="prof.user",
            ),
        ),
    ]
