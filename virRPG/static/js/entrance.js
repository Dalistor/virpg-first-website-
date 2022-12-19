window.onload = () => {

	const login = document.getElementById('login');
	const register = document.getElementById('register');

	login.addEventListener("click", () => {

		window.location.href = "/login/";

	})

	register.addEventListener("click", () => {

		window.location.href = "/register/";

	})

}