import logging
import requests
from pathlib import Path

logger = logging.getLogger(__name__)

class TelegramNotifier:
    def __init__(self, bot_token: str, chat_id: str):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{bot_token}"

    def send_message(self, text: str):
        logger.info("Sending the message/notification on telegram")
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": text
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()

    def send_file(self, file_path: str, caption: str = ""):
        logger.info(f"Sending the file to telegram : {file_path}")
        url = f"{self.base_url}/sendDocument"

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"{file_path} doesn't exist")
        
        with open(path, "rb") as f:
            files = { "document": f}
            data = {
                "chat_id": self.chat_id, 
                "caption": caption
            }

            response = requests.post(url, data=data, files=files)
            response.raise_for_status()