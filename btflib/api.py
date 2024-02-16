import asyncio
import re
from typing import Union

import aiohttp
from motor.motor_asyncio import AsyncIOMotorClient as aiomotor
import discord


class vxTwitter:
    def __init__(
        self,
        api: str = "api.vxtwitter.com",
    ) -> None:
        self.api = api

    async def expand(self, url: list) -> list:
        embeds = []
        for i in url:
            url_replaced = (
                i.replace("twitter.com", self.api)
                .replace("x.com", self.api)
                .replace("www.x.com", self.api)
                .replace("www.twitter.com", self.api)
                .replace("www.api.vxtwitter.com", self.api)
            )
            async with aiohttp.ClientSession() as session:
                async with session.get(url_replaced) as resp:
                    if not resp.status == 500:
                        resp = await resp.json()
                        if not resp["mediaURLs"] == []:
                            murl = True
                        else:
                            murl = False
                        embed = discord.Embed(
                            title="{} (@{})".format(
                                resp["user_name"], resp["user_screen_name"]
                            ),
                            url=resp["tweetURL"],
                            description=resp["text"],
                            color=0x0091FF,
                        )
                        embed.set_author(
                            name="BetterTwitFix",
                            url="https://github.com/dylanpdx/BetterTwitFix",
                        )
                        if murl:
                            embed.set_image(url=resp["mediaURLs"][0])
                        embed.set_footer(text="Using BetterTwitFix")
                        embeds.append(embed)
        return embeds

    async def parse(self, text) -> Union[list, None]:
        pattern = r"(?<!\|\|)(https?://(?:www\.)?(twitter\.com|x\.com)/[a-zA-Z0-9_]{1,15}/status/\d+)(?!\|\|)"
        urls = re.findall(pattern, text)
        resp = []
        for url in urls:
            resp.append(url[0])
        if resp == []:
            return None
        return resp
