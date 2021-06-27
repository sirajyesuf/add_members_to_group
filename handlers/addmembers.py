from pyrogram.handlers import MessageHandler
from pyrogram import Client as app
from pyrogram import filters
from pyrogram.errors import RPCError


async def addMembersFromGroupXToGroupY(app, message):
    g1, g2 = await joinBothGroups(app, message)
    await addMembers(app, message, g1, g2)


async def joinBothGroups(app, message):
    cmd, g1, g2 = message.text.split()
    try:
        g1 = await app.join_chat(g1)
        # print("group1", g1)
        await sendSuccessMessage(message, f"you successfully joined group {g1.title} @{g1.username}")
        g2 = await app.join_chat(g2)
        await sendSuccessMessage(message, f"you successfully joined group {g1.title} @{g2.username}")
        # print("group2", g2)

    except RPCError as e:
        print(e)
    return g1, g2


async def addMembers(app, message, g1, g2):
    count = await app.get_chat_members_count(g1.id)
    await sendSuccessMessage(message, f"total number of members of  {g1.title} @{g1.username} is {count}")

    async for member in app.iter_chat_members(g1.id):
        try:
            if(await app.add_chat_members(g2.id, member.user.id)):
                await sendSuccessMessage(message, f"@{member.user.username} addede successfully")
        except RPCError as e:
            print(e)

add_members_from_groupx_to_groupy_handler = MessageHandler(
    addMembersFromGroupXToGroupY, filters.command('add') & filters.private)


async def sendSuccessMessage(message, msg):
    await message.reply_text(msg)
