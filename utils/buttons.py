from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import requests
from utils.env import WEBAPP, BOT_TOKEN
from utils.texts import WEB_BUTTON





def send_webapp_button(lang, user_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
   

    payload = {
        "chat_id": user_id,
        "text": text,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": WEB_BUTTON[lang],
                        "web_app": {
                            "url": f"{WEBAPP}"
                        }
                    },
                ]
            ]
        }
    }

    response = requests.post(url, json=payload)
    
    if not response.ok:
        print("❌ Ошибка при отправке инлайн-кнопки:", response.text)
