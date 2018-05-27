# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

import requests
from json import loads, JSONEncoder

blockchain_url = "http://localhost:8080/blockchain"
sensor_id = "sensor2"

def responder(resposta, status):
    return HttpResponse(JSONEncoder().encode(resposta),
                        200)

def request_transacao(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = loads(body_unicode)
        body['destino'] = sensor_id

        confirmacao_transacao = requests.post(blockchain_url, data=JSONEncoder().encode(body)).json()
        resposta = {
            "hash": confirmacao_transacao['hash'],
            "data_insercao": confirmacao_transacao['data_insercao']
        }
        return responder(resposta,
                         200)
