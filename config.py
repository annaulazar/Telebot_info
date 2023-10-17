import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str


@dataclass
class Apis:
    weather_key: str
    geo_key: str


@dataclass
class Config:
    bot: Bots
    apis: Apis


def get_config():
    load_dotenv()
    return Config(
        bot=Bots(
            bot_token=os.getenv('BOT_TOKEN')
        ),
        apis=Apis(
            weather_key=os.getenv('Y.WEATHER_KEY'),
            geo_key=os.getenv('JSAPI_HTTPGEOCODER_KEY')
        )
    )


config = get_config()
