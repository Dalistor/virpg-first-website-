window.onload = () => {
	//formulário
	const formu = document.getElementById('form')

	//dados
	const dices = document.querySelectorAll(".dice");
	const attacks_catalog = document.querySelectorAll('.attacks-block')

	dices.forEach((item)=>{
		item.addEventListener("click", ()=> {
			times = prompt('Quantas vezes deseja jogar?');

			if(times % 1 === 0) {
			 	roll(item.id, times);   
			} else {
			    alert('Insira um número inteiro');
			}
		});
	});


	//alterar hp/pe/pp

	const popup = document.getElementById("popup-wrapper")
	const button_create = document.getElementById("popup-content-button")
	const popup_input = document.querySelector(".popup-content-input")
	const add = document.getElementById('add')

	let popup_id;

	const itensIdsNames = ['hp_points', 'pe_points', 'skill_points', 'atribute_points']

	let elementsClickedId;

	for (var i = 0; i < itensIdsNames.length; i++) {
		const element = document.getElementById(itensIdsNames[i])
		const name = itensIdsNames[i]

		element.addEventListener("click", ()=> {
			elementsClickedId = name
			console.log(elementsClickedId)

			popup_input.id = 'id_' + name
			popup_id = 'id_' + name
			popup_input.name = name

			document.getElementById(popup_id).value = ""
			popup.style.display = 'block'
		})
	}

	popup.addEventListener("click", ()=> {
		const clickedClassName = event.target.classList[0]
		const classNames = ['popup-close', 'popup-wrapper']
		const closePopup = classNames.some(className => className === clickedClassName)

		if(closePopup) {
			popup.style.display = 'none'
		}
	});


	button_create.addEventListener("click", ()=> {
		if (elementsClickedId == 'atribute_points') {
			elementsClickedId = 'atribute_point'
		}
		if (elementsClickedId == 'skill_points') {
			elementsClickedId = 'skill_point'
		}

		let input_value = document.getElementById(popup_id).value

		document.getElementById(elementsClickedId).innerHTML = input_value
		autoSave(formu)

		popup.style.display = 'none'
	})

	add.addEventListener("click", ()=> {
		if (elementsClickedId == 'atribute_points') {
			elementsClickedId = 'atribute_point'
		}

		const att   = parseInt(document.getElementById(elementsClickedId).textContent)
		const value = att + parseInt(popup_input.value)

		popup_input.value = value
	})

	attacks_catalog.forEach((item)=> {
		item.addEventListener("click", ()=> {
			id = item.id.split('-')
			id = id[1]

			let formula = document.getElementById('attack_formula-' + id).textContent
			formula = formula.split('+')
			
			const fixed = formula[0]

			formula = formula[1].split('D')

			let times = formula[0]
			const dice = formula[1]

			results = [];

			while (times > 0) {
				const random = Math.round((Math.random() * (dice - 1)) + 1)
				results.push(random)

				times--
			}

			let sum = 0;

			for (var i = 0; i < results.length; i++) {
				sum += results[i]
			}

			const result = parseInt(fixed) + sum

			alert(result)
		})
	})

	//salvando o textarea

	const textArea = document.getElementById('id_infos')
	textArea.addEventListener('input', ()=>{
		autoSave(formu)
	})
}

function roll(dice, times) {

	dice = parseInt(dice.replace(/[^0-9]/g,''))
	times = parseInt(times)

	results = [];

	while (times > 0) {
		const random = Math.round((Math.random() * (dice - 1)) + 1)
		results.push(random)

		times--
	}

	let sum = 0;

	for (var i = 0; i < results.length; i++) {
		sum += results[i]
	}

	const min = Math.min.apply(null, results)
	const max = Math.max.apply(null, results)

	alert('Resultado(s): ' + results + '\nSoma: ' + sum + '\nMínimo: ' + min + '\nMáximo: ' + max);

}