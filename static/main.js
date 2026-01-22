document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat_box');
    if (!chatBox) return;

    const container = chatBox.querySelector('.chat-container');
    const salonId = chatBox.dataset.salonId;
    const currentUser = chatBox.dataset.username;

    // IDs des messages déjà affichés
    const renderedIds = new Set();

    function renderMessages(data) {
        const wasAtBottom =
            chatBox.scrollHeight - (chatBox.scrollTop + chatBox.clientHeight) <= 50;

        data.messages.forEach(msg => {
            if (renderedIds.has(msg.id)) return;

            renderedIds.add(msg.id);

            const div = document.createElement('div');
            const cls = msg.sender === currentUser ? 'my-message' : 'other-message';

            div.className = `message ${cls}`;
            div.innerHTML = `
                <div class="message-content">${msg.content}</div>
                <small class="message-meta">${msg.sender} • ${msg.date}</small>
            `;

            container.appendChild(div);
        });

        if (wasAtBottom) {
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    function fetchMessages() {
        fetch(`/salon/${salonId}/messages-json/`)
            .then(res => res.json())
            .then(renderMessages)
            .catch(() => {});
    }

    // premier chargement
    fetchMessages();

    // rafraîchissement toutes les secondes
    setInterval(fetchMessages, 1000);
});