# btfLib
> [!WARNING]  
> This library has been deprecated. Use at your own risk.

The vxtwitter wrapper used by Selene. It is now obsolete as Twitter embedding has been restored.

## Install
It is not available from PyPI as it was originally discontinued from Selene and therefore a separated library. Please install from GitHub.
```
$ pip install git+https://github.com/selene-discord-dev/btflib.git
```

## Example
This is intended to be used for Discord, so it returns the Discord embedding; for use other than for DiscordBot, please [Use API](https://github.com/dylanpdx/BetterTwitFix?tab=readme-ov-file#api) directly.
```python
import discord
from discord.ext import commands
from btflib import vxTwitter

twitter_expander = vxTwitter() # If you use FxTwitter, replace vxTwitter(api="api.fxtwitter.com"). (However, functions implemented only on FxTwitter are not available.)

bot = Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_message(message):
    urls = await twitter_expander.parse(message.content)
    if urls is None:
        return
    await message.reply(embeds=await twitter_expander.expand())

bot.run(TOKEN)
```