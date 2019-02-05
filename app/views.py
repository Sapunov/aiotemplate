from aiohttp import web
import logging

from app import __version__ as version


log = logging.getLogger(__file__)


class MainHandler:

    def __init__(self):

        pass

    async def index(self, request):

        data = {
            'name': 'app',
            'version': version
        }

        return web.json_response(data)
