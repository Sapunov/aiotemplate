import asyncio
import logging
import time

from aiohttp import web

from app.routes import setup_routes
from app.settings import config
from app.views import MainHandler


async def init(loop):

    app = web.Application(loop=loop)

    handler = MainHandler()

    setup_routes(app, handler)
    host, port = config['host'], config['port']

    return app, host, port


def main():

    loop = asyncio.get_event_loop()

    root = logging.getLogger()
    if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)-8s [%(asctime)s.%(msecs)03d] '
               '(%(name)s): %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.Formatter.converter = time.gmtime

    app, host, port = loop.run_until_complete(init(loop))

    # More useful log format than default
    log_format = '%a (%{X-Real-IP}i) %t "%r" %s %b %Tf ' \
                 '"%{Referrer}i" "%{User-Agent}i"'

    web.run_app(app, access_log_format=log_format, host=host, port=port)


if __name__ == '__main__':

    main()
