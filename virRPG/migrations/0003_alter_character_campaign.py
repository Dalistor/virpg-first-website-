# Generated by Django 4.1.4 on 2022-12-18 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virRPG', '0002_alter_character_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_campaing', to='virRPG.campaign'),
        ),
    ]