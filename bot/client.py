from telethon.sync import TelegramClient
from typing import Optional
from bot.logger import logger

class TelegramClientWrapper:
    def __init__(self, api_id: int, api_hash: str, session_name: Optional[str] = 'anon'):
        self.client = TelegramClient(session_name, api_id, api_hash)
        logger.info('Client created')

    async def start(self) -> None:
        await self.client.start()
        logger.info('Client started')

    async def stop(self) -> None:
        await self.client.disconnect()
        logger.info('Client stopped')

