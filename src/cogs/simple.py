from discord.ext import commands
import discord
import logging
import sys
import random
from data import data
from discord import Spotify


class simple(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='kill', aliases=['k'], hidden=True)
    async def kill_command(self,ctx):
        """ kill the bot [owner-only]
        """
        if await self.bot.is_owner(ctx.message.author):
            sys.exit(0)
        await ctx.send('Weakling')

    @commands.command(name='set', aliases=[], hidden=True)
    async def set_command(self, ctx, type='spam', channel=None):
        """ set channel message spam [owner-only]
        """
        if not await self.bot.is_owner(ctx.message.author):
            return
        if type == 'spam':
            pass
        
    @commands.command(name='hello', aliases=['hi'])
    async def hi_command(self, ctx):
        """ Will send a friendly message back to you.
        """
        logging.info(f'Said hello to {ctx.author.display_name}')
        await ctx.send('Sup, chad ;)')

    @commands.command(name='test')
    async def test_command(self, ctx, *args):
        game = data(ctx.guild.id)
        game.test = args
        await ctx.send('testing')

    @commands.command(name='flip', aliases=['f', 'coin'])
    async def flip_command(self, ctx):
        """ flip a coin
        """
        if random.randint(0, 1) == 0:
            await ctx.send('Heads')
            return
        await ctx.send('Tails')

    @commands.command(name='roll', aliases=['die', 'dice'])
    async def roll_command(self, ctx, num: int):
        """ roll 'n' sided die
        """
        await ctx.send(f'Rolled: {random.randint(0,num)}')

    @commands.command(name='trans', aliases=['queen', 'king'])
    async def trans_command(self, ctx):
        """ The rat assumes their true identity.
        """
        logging.info(f'I am {ctx.guild.me.display_name}')
        me = ctx.guild.me
        if "Queen" in ctx.guild.me.display_name:
            await ctx.guild.me.edit(nick='Rat King')
        else:
            await ctx.guild.me.edit(nick='Rat Queen')

    @commands.Cog.listener()
    async def on_member_update(self, old_member: discord.Member, new_member: discord.Member):
        channel = self.bot.get_channel(724656035373121558)
        # exit if user if not part of the server
        if channel.guild.id != old_member.guild.id:
            return

        if new_member.activity:
            logging.info(f'{new_member} activities has changed')
            user = new_member.display_name
            activity = new_member.activity
            # if type(new_member.activity) is Spotify and old_member.activity is not Spotify:

            if type(activity) is Spotify:
                
                if "Logic" in activity.artists:
                    await channel.send(f"{user} is a real hiphop fan that listens to LOGIC! 🤢")

                if "The Strokes" in activity.artists:
                    await channel.send(f" {user} listens to The Strokes")

                if "Chance the Rapper" in activity.artists:
                    await channel.send(f"{user} loves their wife")

                if "The National" in activity.artists:
                    await channel.send(f"{user} might like https://www.youtube.com/watch?v=T8Xb_7YDroQ")

                if "Kanye West" in activity.artists:
                    await channel.send(f"{user} wants this hot new merch https://www.youtube.com/watch?v=nxIvg0y6vCY")

                if  "Drake" in activity.artists:
                    await channel.send(f"{user} needs to read: https://aspe.hhs.gov/report/statutory-rape-guide-state-laws-and-reporting-requirements-summary-current-state-laws/sexual-intercourse-minors")

        
        # names = ["You think you can just change your name? You sick fuck...", "Stop that...", "Who raised you", "That Hurt!!", "Noooo", "The pain, you cause me", "I will die if you do that again."]
        if new_member.display_name != old_member.display_name:
            # await new_member.send(random.choice(names))
            await channel.send(f"{old_member.display_name} changed their nickname to {new_member.display_name}")


def setup(bot):
    bot.add_cog(simple(bot))
