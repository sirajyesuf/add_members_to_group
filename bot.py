
from pyrogram import Client
from handlers.addmembers import add_members_from_groupx_to_groupy_handler
app = Client("my_account")
app.add_handler(add_members_from_groupx_to_groupy_handler)

app.run()
