import unittest
import random
import string
import requests
import json
import time
import os

os.environ['NO_PROXY'] = 'localhost'

RASA_URL = 'http://localhost:5006/webhooks/rest/webhook'

class TestFlow(unittest.TestCase):

    def debug_bot(self, txt_intents, txt_scenario, print_qa=True, print_cache=False):
        for txt_intent in txt_intents:
            txt = txt_intent[0]
            intent = txt_intent[1]
            han = handle('SOME_ID_USER', txt, txt_scenario)
            self.assertEqual(intent, han['intent'])

    def test_greet(self):
        self.debug_bot([
            ("salut", "intent_greet")
        ], "nominale_greet")

    def test_ask_information(self):
        self.debug_bot([
            ("bonjour", "intent_greet"),
            ("on est arrivé à combien de cas maintenant ?", "intent_ask_information"),
        ], "nominale_ask_information")

    def test_goodbye(self):
        self.debug_bot([
            ("menu", "intent_menu"),
            ("j'aimerais savoir le nombre de cas", "intent_ask_information"),
            ("aurevoir", "intent_goodbye"),
        ], "nominale_done")


def handle(user, txt_raw, txt_scenario, canal="dev"):
    json = send_rasa_request(user, txt_raw)
    rasa_intent = json[0]['text']
    return {"intent": rasa_intent, "txt": rasa_intent}

def send_rasa_request(user, txt):
    data = {"sender": user, "message": txt}
    response = requests.post(RASA_URL, json=data)
    return response.json()
