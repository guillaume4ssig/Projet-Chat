const chatBox = document.getElementById("chat-box");
const salonId = chatBox.dataset.salonId; // si tu passes salon.id en data attribute

// fonction pour récupérer les messages
function fetchMessages() {
    fetch(`/salon/${salonId}/messages-json/`)
        .then(response => response.json())
        .then(data => {
            chatBox.innerHTML = ""; // vide la div
            data.messages.forEach(msg => {
                const p = document.createElement("p");
                p.innerHTML = `<strong>${msg.sender}</strong> : ${msg.content} <small>${msg.date}</small>`;
                chatBox.appendChild(p);
            });
            chatBox.scrollTop = chatBox.scrollHeight; // scroll en bas
        });
}

// lancer la récupération toutes les 3 secondes
setInterval(fetchMessages, 1000);