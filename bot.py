# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import datetime
from botbuilder.core import ActivityHandler, TurnContext, MessageFactory
from botbuilder.schema import SuggestedActions, CardAction, ChannelAccount
from options_reply import pergunta
from check_id import check_id

class MyBot(ActivityHandler):
        
    async def on_message_activity(self, turn_context: TurnContext):
        # isso vai ser executado cada vez que o bot receber uma mensagem

        # SENDER ID
        sender_id = turn_context.activity.from_property.id
        is_first_timer = check_id(sender_id)
        if not is_first_timer:
           await turn_context.send_activity('Bem vindo!')
        # SENDER ID

        # # DATETIME
        # data = datetime.datetime.today().date()
        # hora = datetime.datetime.today().time()
        # await turn_context.send_activity(data, hora)
        # # DATETIME

        if turn_context.activity.text == 'Sim, por favor': 
            # se a mensagem for 'Gostaria do Evangelho de hoje, por favor', ele vai executar esse if
            exec(open("get_api.py").read()) # executa o arquivo api.py que cria um arquivo evangelho.txt
            meuArquivo = open("evangelho.txt", 'r') # le o arquivo evangelho.txt
            evangelho = meuArquivo.read() # cria uma string com o que tem escrito no arquivo
            await turn_context.send_activity(evangelho) # manda uma mensagem (turn_context.send_activity) com o evangelho

        elif turn_context.activity.text == 'Não, obrigado':
            # se a mensagem for 'Não, obrigado', ele vai responder com 'Paz de Cristo'
            await turn_context.send_activity('Paz de Cristo')
        
        else:
            await turn_context.send_activity('Desculpe, não entendi. Você gostaria do evangelho de hoje?') # vai dizer que não entendeu
            # e mandar as opções de novo
            await turn_context.send_activity(pergunta)

    async def on_members_added_activity(
        self,
        members_added: [ChannelAccount],
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Olá, bem-vindo(a) ao bot do evangelho! Você gostaria de receber o evangelho de hoje?")
                await turn_context.send_activity(pergunta)