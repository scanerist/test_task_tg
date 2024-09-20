import asyncio
from bot.group_service import GroupService
from bot.client import TelegramClientWrapper
from bot.logger import logger
import os


API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
GROUP_LINK = os.getenv('GROUP_LINK')

async def main():
    client = TelegramClientWrapper(API_ID, API_HASH)
    await client.start()

    try:
        group_service = GroupService(client.client)

        users_without_messages = await group_service.get_users_without_messages(os.getenv('GROUP_LINK'))

        logger.info(f'Users without messages: {users_without_messages}')
        for user in users_without_messages:
            logger.info(f'{user.first_name} {user.last_name} (@{user.username})')

    except Exception as e:
        logger.error(e)

    finally:
        await client.stop()
        logger.info('Client stopped')

