# Generated by Django 2.2.4 on 2019-10-10 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='congrega',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='genea',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='personaggio',
            old_name='user',
            new_name='giocatore',
        ),
        migrations.RenameField(
            model_name='personaggio',
            old_name='name',
            new_name='nome',
        ),
    ]