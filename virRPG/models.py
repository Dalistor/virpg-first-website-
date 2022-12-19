from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Character(models.Model):

	PRIVATE_CHOISES = (

		('no', 'Não'),
		('yes', 'Sim')

	)

	name                   = models.CharField(default='None', max_length=50, blank=True)

	atribute_points        = models.IntegerField(default=7, blank=True)
	skill_points		   = models.IntegerField(default=150, blank=True)

	strength_points        = models.IntegerField(default=0, blank=True)
	fight_points           = models.IntegerField(default=0, blank=True)
	maneuver_points        = models.IntegerField(default=0, blank=True)
	athletic_points        = models.IntegerField(default=0, blank=True)
	counter_points         = models.IntegerField(default=0, blank=True)
	block_points           = models.IntegerField(default=0, blank=True)

	dexterity_points       = models.IntegerField(default=0, blank=True)
	stunts_points          = models.IntegerField(default=0, blank=True)
	sleight_points         = models.IntegerField(default=0, blank=True)
	stealth_points         = models.IntegerField(default=0, blank=True)
	dodge_points           = models.IntegerField(default=0, blank=True)
	agility_points         = models.IntegerField(default=0, blank=True)
	aim_points             = models.IntegerField(default=0, blank=True)

	vigor_points           = models.IntegerField(default=0, blank=True)
	constitution_points    = models.IntegerField(default=0, blank=True)
	fortitude_points       = models.IntegerField(default=0, blank=True)
	resistance_points      = models.IntegerField(default=0, blank=True)

	inteligence_points     = models.IntegerField(default=0, blank=True)
	sanity_points          = models.IntegerField(default=0, blank=True)
	medicine_points        = models.IntegerField(default=0, blank=True)
	perception_points      = models.IntegerField(default=0, blank=True)
	search_points          = models.IntegerField(default=0, blank=True)
	cheat_points           = models.IntegerField(default=0, blank=True)
	intuition_points       = models.IntegerField(default=0, blank=True)
	survival_points        = models.IntegerField(default=0, blank=True)
	training_points        = models.IntegerField(default=0, blank=True)
	culture_points         = models.IntegerField(default=0, blank=True)
	knowledge_points       = models.IntegerField(default=0, blank=True)
	effort_points          = models.IntegerField(default=0, blank=True)
	investigation_points   = models.IntegerField(default=0, blank=True)

	personality_points     = models.IntegerField(default=0, blank=True)
	charisma_points        = models.IntegerField(default=0, blank=True)
	determination_points   = models.IntegerField(default=0, blank=True)
	eloquence_points       = models.IntegerField(default=0, blank=True)
	resilience_points      = models.IntegerField(default=0, blank=True)
	diplomacy_points       = models.IntegerField(default=0, blank=True)
	luck_points            = models.IntegerField(default=0, blank=True)
	wisdom_points          = models.IntegerField(default=0, blank=True)

	hp_points              = models.IntegerField(default=10, blank=True)
	pe_points              = models.IntegerField(default=10, blank=True)

	infos                  = models.TextField(blank=True)

	user                   = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name="character_user")
	campaign 			   = models.ForeignKey("Campaign", on_delete=models.CASCADE, related_name="character_campaing")

	is_private             = models.CharField(max_length=3 ,choices=PRIVATE_CHOISES, default='yes', blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Attack(models.Model):

	DICES = (

		('D4', 'D4'),
		('D6', 'D6'),
		('D8', 'D8'),
		('D10', 'D10'),
		('D12', 'D12'),
		('D20', 'D20'),
		('D%', 'D%'),

	)

	name                   = models.CharField(default="none", max_length=50, blank=True)
	fixed                  = models.IntegerField(default=0, blank=True)
	times                  = models.IntegerField(default=1, blank=True)
	dice_type              = models.CharField(max_length=3, choices=DICES)

	character 			   = models.OneToOneField("Character", on_delete=models.SET_NULL, null=True, related_name="attack_character")

	def __str__(self):
		return self.name


class Campaign(models.Model):
	PRIVATE_CHOISES = (

		('no', 'Não'),
		('yes', 'Sim')

	)

	name                   = models.CharField(default="None", max_length=50, blank=True)
	is_private			   = models.CharField(max_length=3, choices=PRIVATE_CHOISES, blank=True)

	users                  = models.ManyToManyField(User, blank=True, related_name="campaing_users")
	admin  				   = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name="campaing_admin")

	created_at 			   = models.DateTimeField(auto_now_add=True)
	updated_at 			   = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name