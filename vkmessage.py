import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from oken import token_group, id_group

vk_session = vk_api.VkApi(token = token_group)
longpoll = VkBotLongPoll(vk_session, id_group)

def send_utro(id, message, attachment):
    vk_session.method('messages.send', {'chat_id' : id, "message": message,
"attachment": attachment, "random_id": 0})

