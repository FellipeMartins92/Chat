# Generated by Django 4.2.20 on 2025-05-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_friends_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='status',
            field=models.CharField(choices=[('2', 'Accepted'), ('1', 'Pending')], max_length=3),
        ),
    ]
