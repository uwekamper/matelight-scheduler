# -*- coding: utf-8 -*-

import logging
import asyncio
import time

from matelight_scheduler.protocol import handle_client, accept_client

logging.basicConfig(level=logging.DEBUG)

def test_server():
    loop = asyncio.get_event_loop()
    f = asyncio.start_server(accept_client, host=None, port=1337)
    server = loop.run_until_complete(f)

    @asyncio.coroutine
    def kill_later():
        yield from asyncio.sleep(10)
        loop.stop()
    loop.run_until_complete(kill_later())

    loop.run_forever()

