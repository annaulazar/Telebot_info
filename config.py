import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str


@dataclass
class Config:
    bot: Bots


def get_config():
    load_dotenv()
    return Config(
        bot=Bots(
            bot_token=os.getenv('BOT_TOKEN')
        )
    )


config = get_config()
