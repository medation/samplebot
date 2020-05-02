const constant = require('./constants');
const webhook = require('./webhook');

const http = require('http');
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());

app.use(bodyParser.urlencoded({ extended: false }));

const server = http.createServer(app);

server.listen(3000, () => {
	console.log('Server listening on port: ', 3000);
});

app.get('/webhook/messenger', function(req, res) {
    if (req.query['hub.mode'] && req.query['hub.verify_token'] === constant.MESSENGER_VERIFY_TOKEN)
        res.status(200).send(req.query['hub.challenge']);
    else
        res.sendStatus(403);
});

app.post('/webhook/messenger', function(req, res) {
    if (req.body.object === 'page') {
        req.body.entry.forEach(entry => {
            entry.messaging.forEach(event => {
                if (event.message && event.message.text) {
                    webhook.sendMessenger(event);
                }
            });
        });
        res.status(200).end();
    }
});