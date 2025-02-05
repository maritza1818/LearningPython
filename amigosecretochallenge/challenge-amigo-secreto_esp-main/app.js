// El principal objetivo de este desafío es fortalecer tus habilidades en lógica de programación. Aquí deberás desarrollar la lógica para resolver el problema.

let amigos = [];

function agregarAmigo() {
    const nombre = document.getElementById('amigo').value;
    if (nombre === "") {
        alert("Por favor ingrese un nombre válido.");
        return;
    }
    amigos.push(nombre);
    actualizarLista();
    document.getElementById('amigo').value = ""; 
}

function actualizarLista() {
    const lista = document.getElementById('listaAmigos');
    lista.innerHTML = ""; 
    amigos.forEach((amigo, index) => {
        const li = document.createElement("li");
        li.textContent = amigo;
        lista.appendChild(li);
    });
}

function sortearAmigo() {
    if (amigos.length === 0) {
        alert("Debe agregar al menos un amigo para sortear.");
        return;
    }

    const indexAleatorio = Math.floor(Math.random() * amigos.length);
    const amigoSorteado = amigos[indexAleatorio];

    const resultado = document.getElementById('resultado');
    resultado.innerHTML = `<li>¡Tu amigo secreto es: <strong>${amigoSorteado}</strong>!</li>`;
}
