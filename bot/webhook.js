const constant = require('./constants');

sendMessenger = (event) => {
    return fetch(
        `${constant.MESSENGER_API}?access_token=${constant.MESSENGER_ACCESS_TOKEN}`, {
            headers: {
                'Content-Type': 'application/json',
            },
            method: 'POST',
            body: JSON.stringify({
                messaging_type: 'RESPONSE',
                recipient: { id: event.sender.id },
                message: event.message.text
            }),
        }
    );
}

module.exports = {
    sendMessenger : sendMessenger
};