from modules._base_ import BaseModule, Command, get_perm_level, set_perm_level, InsufficientPrivilegesException
import logging_helper
import discord
import constants



class MemeModule(BaseModule):
    def __init__(self):
        BaseModule.__init__(self)
        self.logger = logging_helper.init_logger(MemeModule.__name__)
        super().register_command(Command("👌", self.cmd_ok_hand, constants.LEVEL_EVERYONE))


    async def cmd_ok_hand(self, client, message):
        em = discord.Embed()
        em.set_image(url="https://i.imgur.com/lmLc0Or.png")
        await client.send_message(message.channel, embed=em)
