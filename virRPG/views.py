from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Character, Attack, Campaign
from .forms import CharacterForm, AttackForm, CampaignForm
from django.views.decorators.csrf import csrf_exempt

#entrada
def entrance (request):
	if request.user.is_authenticated:
		return redirect('/campaigns/')
	else:
		return render(request, 'entrance.html')

#registro
def register (request):
	return render(request, 'register.html')

#cadastrar usuário
def store_register (request):
	name             =    request.POST['user']
	password         =    request.POST['password']
	confirm_password =    request.POST['confirm_password']

	#verificar senhas
	if password != confirm_password:
		return render(request, 'register.html', {
			'msg': 'senhas diferentes',
			'class': 'msg-error'
		})

	#verificar se usuário já existe
	if User.objects.filter(username=name).exists():
		return render(request, 'register.html', {
			'msg': 'usuário já existe',
			'class': 'msg-error'
		})

	newUser = User.objects.create_user(username=name, password=password)
	newUser.save()

	login(request, newUser)

	return redirect('/campaigns/')

#login
def log (request):
	return render(request, 'login.html')

#logar usuário
def store_login (request):
	name       =    request.POST['user']
	password   =    request.POST['password']

	user = authenticate(username=name, password=password)

	if user is not None:
		login(request, user)
		return redirect('/campaigns/')

	else:
		return render(request, 'login.html', {
			'msg': 'usuário ou senha incorretos',
			'id': 'msg-error'
		})

#campanhas
@csrf_exempt
def campaigns (request):
	if request.user.is_authenticated == False:
		return redirect('/login/')

	search = request.GET.get('search')
	all_characters = Character.objects.filter(user=request.user)

	#pesquisa
	if search:
		all_campaigns = Campaign.objects.filter(name__icontains=search, is_private='no')
		campaigns = takeCampaings(request, all_campaigns, all_characters)

	#nova campanha
	else:
		form = CampaignForm()

		if request.method == 'POST':
			form = CampaignForm(request.POST)
			instance = form.save(commit=False)
			instance.is_private = 'no'
			instance.admin = request.user
			form.save()

		all_campaigns = Campaign.objects.filter(is_private='no')
		
		campaigns = takeCampaings(request, all_campaigns, all_characters)
		
	return render(request, 'campaigns.html', {'campaigns': campaigns})

#função associada a def 'campaigns'
def takeCampaings(request, all_campaigns, all_characters):
	campaigns_list = []

	for campaign in all_campaigns:
		if campaign.admin == request.user or request.user.is_staff:
			campaigns_list.append(campaign)
		else:
			for character in all_characters:
				if character.campaing == campaign and character.user == request.user:
					campaigns_list.append(campaign)
	
	paginator = Paginator(campaigns_list, 5)
	page = request.GET.get('page')
	campaigns = paginator.get_page(page)

	return campaigns

#editar campanha
def campaign_edit (request, cid):
	if request.user.is_authenticated == False:
		return redirect('/login/')

	campaign = Campaign.objects.get(pk=cid)
	if campaign.admin != request.user:
		return redirect('/campaigns/')

	if (request.method == 'POST'):
		form = CampaignForm(request.POST, instance=campaign)
		form.save()

		return redirect('/campaigns/')

	return render(request, 'campaign_edit.html', {'campaign': campaign})
		
#deletar campanha
def campaign_del (request, cid):
	if request.user.is_authenticated == False:
		return redirect('/login/')

	campaign = Campaign.objects.get(pk=cid)
	if campaign.admin != request.user and request.user.is_staff == False:
		return redirect('/campaigns/')

	campaign.delete()
	return redirect('/campaigns/')


@csrf_exempt
def characters (request, cid):
	if request.user.is_authenticated == False:
		return redirect('/login/')

	campaign = Campaign.objects.get(pk=cid)
	search = request.GET.get('search')

	#pesquisa
	if search:
		all_characters = Character.objects.filter(name__icontains=search)
		characters = takeCharacters(request, campaign, all_characters)
		
	#novo personagem
	else:
		form = CharacterForm()

		if request.method == 'POST':
			form = CharacterForm(request.POST)
			instance = form.save(commit=False)
			instance.user = request.user
			instance.campaign = campaign
			form.save()

		all_characters = Character.objects.filter(campaign=campaign)
		characters = takeCharacters(request, campaign, all_characters)

	return render(request, 'characters.html', {
		'characters': characters,
		'campaign': campaign
	})

#função associada a def 'characters'
def takeCharacters(request, campaign, all_characters):
	characters_list = []

	for character in all_characters:
		if character.campaign == campaign:
			if character.user == request.user or request.user.is_staff or campaign.admin == request.user or character.is_private == 'no':
				characters_list.append(character)

	paginator = Paginator(characters_list, 5)

	page = request.GET.get('page')
	characters = paginator.get_page(page)

	return characters		

#edição de personagem
def character_edit (request, cid, id):
	if request.user.is_authenticated == False:
		return redirect('/login/')

	character = Character.objects.get(pk=id)
	if character.user != request.user:
		return redirect('/campaigns/')

	form = CharacterForm()

	if request.method == 'POST':
		form = CharacterForm(request.POST, instance=character)
		form.save()

		return redirect('/campaigns/' + str(cid) + '/characters')

	else:
		return render(request, 'character_edit.html', {
			'character': character,
			'form': form
		})

#deletar personagem
def character_del (request, cid,id):
	if request.user.is_authenticated == False:
		return redirect('/login/')

	character = Character.objects.get(pk=id)
	if character.user != request.user:
		return redirect('/campaigns/')

	character.delete()

	return redirect('../../../' + str(cid) + '/characters/')

#logout
def log_out (request):
		logout(request)
		return redirect('/login/')

#view de alterar senha
def c_password (request):
	if request.user.is_authenticated == False:
		return redirect('/login/')

	return render(request, 'c_password.html')

#alterar senha
def store_c_password (request):
	if request.user.is_authenticated == False:
		return redirect('/login/')

	password = request.POST['password']
	confirm_password = request.POST['c_password']

	if password == confirm_password:
		user = User.objects.get(password = request.user.password)
		user.set_password(password)
		user.save()

		return redirect('/login/')

	else:
		return render(request, 'c_password.html', {
			'msg': 'senhas não correspondem',
			'id': 'msg-error'
		})
		
#ficha do personagem
@csrf_exempt
def token (request, id):
	if request.user.is_authenticated == False:
		return redirect('/login/')

	character = Character.objects.get(pk=id)
	print(character.user)
	print(request.user)
	if character.user != request.user:
		return redirect('/campaigns/')

	attacks = list(Attack.objects.filter(character=character))

	if request.method == 'POST':
		form = CharacterForm(request.POST, instance=character)

		if form.is_valid():
			CharacterForm(instance=character).save()

			return redirect('/token/' + str(id))

	else:
		return render(request, 'token.html', {
			'character': character, 
			'attacks': attacks,
		})

#registrar ataque
@csrf_exempt
def register_attack(request, id):
	if request.user.is_authenticated == False:
		return redirect('/login/')

	if request.method == 'POST':
		form = AttackForm(request.POST, instance=attack)
		instance = form.save(commit=False)
		instance.user = request.user
		form.save()

		return redirect('/token/' + str(id))

	return render(request, 'register_attack.html')
		
#editar ataque
def edit_attack(request, id, aid):
	if request.user.is_authenticated == False:
		return redirect('/login/')

	attack = Attack.objects.get(pk=aid)

	if request.method == 'POST':
		form = AttackForm(request.POST, instance=attack)
		form.save()

		return redirect('/token/' + str(id))

	else:
		return render(request, 'register_attack.html', {'attack': attack})

#deletar ataque
def del_attack(request, id, did):
	if request.user.is_authenticated == False:
		return redirect('/login/')

	attack = get_object_or_404(Attack, pk=did)
	attack.delete()
	return redirect('/token/' + str(id))

#habilidades do personagem
@csrf_exempt
def skills(request, id):
	if request.user.is_authenticated == False:
		return redirect('/login/')

	character = Character.objects.get(pk=id)
	form = CharacterForm(instance=character)

	if request.method == 'POST':
		form = CharacterForm(request.POST, instance=character)
		form.save()

		return redirect('/token/' + str(id))

	return render(request, 'atribute.html', {
		'character': character,
		'form': form
	})