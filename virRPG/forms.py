from django import forms
from .models import Character, Attack, Campaign

class CharacterForm(forms.ModelForm):
	class Meta:
		model = Character
		fields = (

			'name', 
			'atribute_points',
			'skill_points',
			'strength_points',
			'fight_points',
			'maneuver_points',
			'athletic_points',
			'counter_points',
			'block_points',
			'dexterity_points',
			'stunts_points',
			'sleight_points',  
			'stealth_points',  
			'dodge_points',   
			'agility_points',  
			'aim_points',
			'vigor_points',
			'constitution_points',
			'fortitude_points',
			'resistance_points',
			'inteligence_points', 
			'sanity_points', 
			'medicine_points', 
			'perception_points', 
			'search_points', 
			'cheat_points', 
			'intuition_points',
			'survival_points',
			'training_points',
			'culture_points',
			'knowledge_points', 
			'effort_points',
			'investigation_points',
			'personality_points',
			'charisma_points',     
			'determination_points',
			'eloquence_points',
			'resilience_points',  
			'diplomacy_points',  
			'luck_points',  
			'wisdom_points',
			'hp_points',
			'pe_points',
			'infos',
			'is_private'

		)

class AttackForm(forms.ModelForm):
	class Meta:
		model = Attack
		fields = (

			'name',
			'fixed',
			'times',
			'dice_type',

		)

class CampaignForm(forms.ModelForm):
	class Meta:
		model = Campaign
		fields = (

			'name',
			'is_private',
			'users'

		)