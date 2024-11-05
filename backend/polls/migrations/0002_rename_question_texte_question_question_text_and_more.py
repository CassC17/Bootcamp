# Generated by Django 5.1.2 on 2024-11-04 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='question_texte',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='game',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='polls.player'),
        ),
    ]