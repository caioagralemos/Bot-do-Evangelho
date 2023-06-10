from botbuilder.core import MessageFactory
from botbuilder.schema import SuggestedActions, CardAction

pergunta = MessageFactory.text('Escolha uma opção:')
pergunta.suggested_actions = SuggestedActions(
                    actions=[
                        CardAction(title='Sim, por favor.', type='imBack', value='Sim, por favor'),
                        CardAction(title='Não, obrigado', type='imBack', value='Não, obrigado'),
                    ]
                )
