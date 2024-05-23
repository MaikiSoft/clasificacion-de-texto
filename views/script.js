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
