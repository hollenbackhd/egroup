# Generated by Django 3.0.1 on 2020-10-28 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allgroups', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='allgroups',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='allgroups.Allgroups'),
        ),
    ]
