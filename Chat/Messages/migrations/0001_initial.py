# Generated by Django 4.2.20 on 2025-04-29 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Groups', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='messages_to_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('id_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='Users.user')),
                ('id_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='Users.user')),
            ],
        ),
        migrations.CreateModel(
            name='messages_to_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('id_group', models.ManyToManyField(to='Groups.groupchat')),
                ('id_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages_group', to='Users.user')),
            ],
        ),
    ]
