import uuid

import requests

import json


class Token:
    def get_token(self):  # получить ТОКЕН, чтобы в будущем его использовать для получения ответа от GC
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
        payload = 'scope=GIGACHAT_API_PERS'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': f'{str(uuid.uuid4())}',
            'Authorization': 'Basic NGY1ODhiMjMtN2RjOS00OTM4LWJkMmMtNjJjNzE4ZDkwNGRjOmViMzYyYTYzLTQ2MmEtNDhiYi1iNTU1LTliMmJiODVhZDE5Yg=='
        }

        return requests.request(method="POST",
                                url=url,
                                headers=headers,
                                data=payload,
                                verify="certificate.cer").json().get('access_token')

    def get_answer(self, list_with_messages_from_user, access_token):  # получаем ответ от нейросети
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

        payload = json.dumps({
            "model": "GigaChat",
            "messages": [
                {
                    "role": "user",
                    "content": f"{" ".join(list_with_messages_from_user)}"
                }
            ],
            "stream": False,
            "repetition_penalty": 1
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        return requests.request(method="POST",
                                url=url,
                                headers=headers,
                                data=payload,
                                verify="certificate.cer").json().get('choices')[0].get('message').get('content')

# Пример использования
# token = Token().get_token()
# list_messages = ["Привет!", "Меня сегодня обидели в школе", "Да, это просто ужасно"]
# print(Token().get_answer(list_messages, token))
