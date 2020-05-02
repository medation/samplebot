# Covid-19 Bot

Node.js project for connecting messenger with nlu and different services.

## Overview of the files


`bot.js` - Server listener with endpoint


`connect.js` - Connect socket implementation


`webhook.js` - Implementation for sending message to messenger

## Installation and run

Pre-requirement :

    - node v10+ , npm v6+


Installation :

```
npm install
```

Run :

```
node bot.js
```

Deploying in server with PM2 :

```
pm2 bot.js -i ${number_of_instance}
```
