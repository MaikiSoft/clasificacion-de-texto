$(document).ready(function() {
    const chatBox = $('#chat-box');
    const userInput = $('#user-input');
    const sendBtn = $('#send-btn');

    sendBtn.click(function() {
        const userMessage = userInput.val().trim();
        if (userMessage !== '') {
            appendMessage('user', userMessage);
            $.post('/submit', { 'entrada': userMessage }, function(data) {
                setTimeout(function() {
                    appendMessage('bot', data);
                }, 1000);
            });
            userInput.val('');
        }
    });

    function appendMessage(sender, message) {
        const messageElement = $('<div></div>');
        messageElement.addClass('chat-message ' + sender);
        messageElement.text(message);
        chatBox.append(messageElement);
        chatBox.scrollTop(chatBox[0].scrollHeight);
    }
});

function seleccionarComentario() {
    const selectComment = document.getElementById('selectComment');
    const inputText = document.getElementById('user-input'); // Cambiado a 'user-input'
    // Si se selecciona un comentario, llenar el campo de texto con su contenido
    if (selectComment.value !== '') {
        inputText.value = selectComment.value;
    }
}

async function cargarComentarios() {
    try {
        const response = await fetch('/prueba-json');
        const data = await response.json();
        const selectComment = document.getElementById('selectComment');
        // Limpiar opciones existentes
        selectComment.innerHTML = '<option value="">Selecciona un comentario</option>';
        // Agregar opciones desde el archivo JSON
        data.comentarios.forEach(comment => {
            const option = document.createElement('option');
            option.value = comment.texto;
            option.text = comment.texto;
            selectComment.appendChild(option);
        });
    } catch (error) {
        console.error('Error al cargar los comentarios:', error);
    }
}

window.onload = cargarComentarios;
