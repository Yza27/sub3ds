function validacao() {
			var usuario = formulario.usuario;
			var senha = formulario.senha;
			var email = formulario.email;
			var telefone = formulario.telefone;
			const emailregex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g;
			const telefoneregex = /81[9]{0,1}[0-9]{8}/g;
			const emailok = emailregex.test(email.value);
			const telefoneok = telefoneregex.test(telefone.value);
			console.log(emailok);
			console.log(telefoneok);
			if (usuario.value == "") {
				alert("Usuário não informado.");
			}
			if (senha.value == "") {
				alert("Senha não informada.");
			}
			if (emailok === false) {
				alert("Email Inválido.");
			}
			if (telefoneok === false) {
				alert("Telefone Inválido.");
			}
		}
