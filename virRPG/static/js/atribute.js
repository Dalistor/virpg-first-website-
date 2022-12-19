window.onload = ()=> {
	const skill_points = document.getElementById("atributes_points")
	const atribute_points  = document.getElementById("atribute_points")
	const less_att    = document.getElementById("less_att")
	const more_att    = document.getElementById("more_att")

	const buttons = document.querySelectorAll(".operation_button")
	const points = document.querySelectorAll(".points")
	const skills = document.querySelectorAll(".skill_name")

	const location = window.location.href

	const formu = document.getElementById('formu')

	let atribute = location.split('/')
	atribute = atribute[5]

	buttons.forEach((item)=> {
		item.addEventListener("click", ()=> {
			let id = item.id
			console.log(id)
			let separator = id.split('_')
			
			let element = document.getElementById(separator[1] + '_' + separator[2])

			let element_value = parseInt(element.textContent)
			let past_element_value = element_value

			let atts = parseInt(skill_points.textContent)

			if (separator[0] === 'more' && atts > 0) {

				element_value += 1
				atts -= 1

				element.innerHTML = element_value
				skill_points.innerHTML = atts

			}

			if (separator[0] === 'less' && atts >= 0) {

				if (element_value == 0) {
					return;
				}

				element_value -= 1
				atts += 1

				element.innerHTML = element_value
				skill_points.innerHTML = atts

			}

			if (separator[1] == 'effort') {
				let pe = parseInt(document.getElementById('id_pe_points').value)
				let subPe = element_value - past_element_value
				subPe = subPe * 2
				pe = subPe + pe

				document.getElementById('id_pe_points').value = pe
			}

			if (separator[1] == 'constitution') {
				let hp = parseInt(document.getElementById('id_hp_points').value)
				let subHp = element_value - past_element_value
				subHp = subHp * 5
				hp = subHp + hp
				
				document.getElementById('id_hp_points').value = hp
			}

			let atribute_p = parseInt(atribute_points.textContent)
			let skill_p = parseInt(skill_points.textContent)

			document.getElementById('id_' + separator[1] + '_' + separator[2]).value = element_value

			document.getElementById('id_atribute_points').value   = atribute_p
			document.getElementById('id_skill_points').value    = skill_p
			
			autoSave(formu)
		})
	})

	

	const ids = ['strength', 'dexterity', 'vigor', 'inteligence', 'personality']

	let selected_atribute_value;

	for (var i = 0; i < ids.length; i++) {
		let id = ids[i]
		console.log(id)

		let element = document.getElementById(id)

		element.addEventListener("click", ()=>{
			selected_atribute_value = parseInt(document.getElementById(id + '_points').textContent)

			for (var i = 0; i < ids.length; i++) {
				document.getElementById(ids[i]).style.color = 'black'
			}

			switch(id) {
				case 'strength':
					element.style.color = 'red'
					break
				case 'dexterity':
					element.style.color = 'blue'
					break
				case 'vigor':
					element.style.color = 'orange'
					break
				case 'inteligence':
					element.style.color = 'pink'
					break
				case 'personality':
					element.style.color = 'purple'
					break
			}
		})


		let more = document.getElementById('more_' + id + '_points')
		let less = document.getElementById('less_' + id + '_points')


		more.addEventListener("click", ()=>{
			let atr_points = parseInt(document.getElementById('atribute_points').textContent)

			if (atr_points > 0) {
				let skill_points = parseInt(document.getElementById(id + '_points').textContent)
				skill_points += 1
				document.getElementById(id + '_points').innerHTML = skill_points

				atr_points -= 1
				document.getElementById('atribute_points').innerHTML = atr_points

				document.getElementById('id_atribute_points').value = atr_points
				document.getElementById('id_' + id + '_points').value = skill_points

				selected_atribute_value = parseInt(document.getElementById(id + '_points').textContent)

				autoSave(formu)
			}
		})

		less.addEventListener("click", ()=>{
			let atr_points = parseInt(document.getElementById('atribute_points').textContent)
			let skill_points = parseInt(document.getElementById(id + '_points').textContent)

			skill_points -= 1
			document.getElementById(id + '_points').innerHTML = skill_points

			atr_points += 1
			document.getElementById('atribute_points').innerHTML = atr_points

			document.getElementById('id_atribute_points').value = atr_points
			document.getElementById('id_' + id + '_points').value = skill_points

			selected_atribute_value = parseInt(document.getElementById(id + '_points').textContent)

			autoSave(formu)
		})

	}
	
	skills.forEach((item)=> {
		item.addEventListener("click", ()=> {
			if(selected_atribute_value == null) {
				alert('selecione um atributo')
				return
			}

			id = item.id
			separator = id.split('n-')

			value = parseInt(document.getElementById(separator[1]).textContent)

			if (separator[1] == 'block_points') {
				value += 3
			}

			if (separator[1] == 'counter_points') {
				value -= 3
			}

			times = parseInt(selected_atribute_value)

			roll('d20', value, times)
		})
	})
}



function roll(dice, value, times) {
	if (times < 0) {
		dice = parseInt(dice.replace(/[^0-9]/g,''))
		times = parseInt(times) - 1

		let crit_dice = Math.round((Math.random() * (dice - 1)) + 1)

		let results = []

		let media = 0;

		while (times < 0) {
			const random = Math.round((Math.random() * (dice - 1)) + 1)
			media += random

			results.push(random)
			times++
		}

		const min = Math.min.apply(null, results) + value

		alert('Resultado(s): ' + results + '\nMínimo: ' + min + '\nCrítico: ' + crit_dice)
	} else {
		dice = parseInt(dice.replace(/[^0-9]/g,''))
		times = parseInt(times) + 1

		let crit_dice = Math.round((Math.random() * (dice - 1)) + 1)

		let results = []

		let media = 0;

		while (times > 0) {
			const random = Math.round((Math.random() * (dice - 1)) + 1)
			media += random

			results.push(random)
			times--
		}

		const min = Math.round(media / results.length) + value

		const max = Math.max.apply(null, results) + value

		alert('Resultado(s): ' + results + '\nMínimo: ' + min + '\nMáximo: ' + max + '\nCrítico: ' + crit_dice)
	}
	
}