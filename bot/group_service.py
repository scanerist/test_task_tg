from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import User
from typing import List
from bot.logger import logger

class GroupService:
    def __init__(self, client: TelegramClient):
        self.client = client
        logger.info('GroupService created')


    async def get_participants(self, group_link: str) -> List[str]:
        group = await self.client.get_entity(group_link)
        participants = await self.client.get_participants(group)
        logger.info(f'Got {len(participants)} participants from {group_link}')

        return participants

    async def get_message_authors(self, group_link: str) -> List[int]:
        group = await self.client.get_entity(group_link)
        logger.info(f'Getting message authors from {group_link}')

        message_authors = set()
        offset_id = 0
        limit = 100

        while True:
            history = await self.client(GetHistoryRequest(
                peer=group,
                offset_id=offset_id,
                offset_date=None,
                add_offset=0,
                limit=limit,
                max_id=0,
                min_id=0,
                hash=0
            ))

            if not history.messages:
                break

            message_authors.update(message.from_id.user_id for message in history.messages)


            offset_id = history.messages[-1].id
            logger.info(f'Got {len(message_authors)} message authors from {group_link} from {offset_id}')

        return list(message_authors)

    async def get_users_without_messages(self, group_link: str) -> list[User]:
        logger.info(f'Getting users without messages from {group_link}')
        participants = await self.get_participants(group_link)
        message_authors_id = await self.get_message_authors(group_link)

        return [user for user in participants if user.id not in message_authors_id]