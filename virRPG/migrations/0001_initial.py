# Generated by Django 4.1.4 on 2022-12-18 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='none', max_length=50)),
                ('fixed', models.IntegerField(blank=True, default=0)),
                ('times', models.IntegerField(blank=True, default=1)),
                ('dice_type', models.CharField(choices=[('D4', 'D4'), ('D6', 'D6'), ('D8', 'D8'), ('D10', 'D10'), ('D12', 'D12'), ('D20', 'D20'), ('D%', 'D%')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='None', max_length=50)),
                ('is_private', models.CharField(blank=True, choices=[('no', 'Não'), ('yes', 'Sim')], max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='campaing_admin', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(blank=True, null=True, related_name='campaing_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='None', max_length=50)),
                ('atribute_points', models.IntegerField(blank=True, default=7)),
                ('skill_points', models.IntegerField(blank=True, default=150)),
                ('strength_points', models.IntegerField(blank=True, default=0)),
                ('fight_points', models.IntegerField(blank=True, default=0)),
                ('maneuver_points', models.IntegerField(blank=True, default=0)),
                ('athletic_points', models.IntegerField(blank=True, default=0)),
                ('counter_points', models.IntegerField(blank=True, default=0)),
                ('block_points', models.IntegerField(blank=True, default=0)),
                ('dexterity_points', models.IntegerField(blank=True, default=0)),
                ('stunts_points', models.IntegerField(blank=True, default=0)),
                ('sleight_points', models.IntegerField(blank=True, default=0)),
                ('stealth_points', models.IntegerField(blank=True, default=0)),
                ('dodge_points', models.IntegerField(blank=True, default=0)),
                ('agility_points', models.IntegerField(blank=True, default=0)),
                ('aim_points', models.IntegerField(blank=True, default=0)),
                ('vigor_points', models.IntegerField(blank=True, default=0)),
                ('constitution_points', models.IntegerField(blank=True, default=0)),
                ('fortitude_points', models.IntegerField(blank=True, default=0)),
                ('resistance_points', models.IntegerField(blank=True, default=0)),
                ('inteligence_points', models.IntegerField(blank=True, default=0)),
                ('sanity_points', models.IntegerField(blank=True, default=0)),
                ('medicine_points', models.IntegerField(blank=True, default=0)),
                ('perception_points', models.IntegerField(blank=True, default=0)),
                ('search_points', models.IntegerField(blank=True, default=0)),
                ('cheat_points', models.IntegerField(blank=True, default=0)),
                ('intuition_points', models.IntegerField(blank=True, default=0)),
                ('survival_points', models.IntegerField(blank=True, default=0)),
                ('training_points', models.IntegerField(blank=True, default=0)),
                ('culture_points', models.IntegerField(blank=True, default=0)),
                ('knowledge_points', models.IntegerField(blank=True, default=0)),
                ('effort_points', models.IntegerField(blank=True, default=0)),
                ('investigation_points', models.IntegerField(blank=True, default=0)),
                ('personality_points', models.IntegerField(blank=True, default=0)),
                ('charisma_points', models.IntegerField(blank=True, default=0)),
                ('determination_points', models.IntegerField(blank=True, default=0)),
                ('eloquence_points', models.IntegerField(blank=True, default=0)),
                ('resilience_points', models.IntegerField(blank=True, default=0)),
                ('diplomacy_points', models.IntegerField(blank=True, default=0)),
                ('luck_points', models.IntegerField(blank=True, default=0)),
                ('wisdom_points', models.IntegerField(blank=True, default=0)),
                ('hp_points', models.IntegerField(blank=True, default=10)),
                ('pe_points', models.IntegerField(blank=True, default=10)),
                ('infos', models.TextField(blank=True)),
                ('is_private', models.CharField(blank=True, choices=[('no', 'Não'), ('yes', 'Sim')], default='yes', max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attack', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_attack', to='virRPG.attack')),
                ('campaign', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='character_campaing', to='virRPG.campaign')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='character_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='attack',
            name='character',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attack_character', to='virRPG.character'),
        ),
    ]
