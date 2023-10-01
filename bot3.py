import bale
from bale import Bot, Message, EventType

client = Bot("token")


@client.listen(EventType.READY)
async def when_bot_is_ready():
    print(client.user, "is Ready!")


@client.listen(EventType.MESSAGE)
async def when_receive_message(message: Message):
    if message.content == "/start":
        photo = 'salam'
        return await message.chat.send(text=photo)

client.run()


