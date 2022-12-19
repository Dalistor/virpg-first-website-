function autoSave(form, autonow) {
	const link = window.location.href

	function getCookie(name) {
		let cookieValue = null;
		if (document.cookie && document.cookie !== '') {
		    const cookies = document.cookie.split(';');
		    for (let i = 0; i < cookies.length; i++) {
		        const cookie = cookies[i].trim();
		        // Does this cookie string begin with the name we want?
		        if (cookie.substring(0, name.length + 1) === (name + '=')) {
		            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		            break;
		        }
		    }
		}

		return cookieValue;
	}

	const csrftoken = getCookie('csrftoken');

	const config = {
	    // O nome do header é o Django que dá, por padrão. Mas você pode mudar nas configurações.
	    headers: {
	        'X-CSRFToken': csrftoken,
	        'Content-Type': 'multipart/form-data', //Aqui você passa o formato novamente.
	    }
	}
	
	let data = new FormData(form)
	axios.post(link, data, config)

}

