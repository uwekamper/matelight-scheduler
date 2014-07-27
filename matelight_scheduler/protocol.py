# -*- coding: utf-8 -*-

import asyncio
import logging

clients = {}

log = logging.getLogger(__name__)

@asyncio.coroutine
def handle_client(client_reader, client_writer):
    log.debug("Handling new client")
    while True:
        data = (yield from client_reader.readline())
        client_writer.write(data)

def accept_client(client_reader, client_writer):
    task = asyncio.Task(handle_client(client_reader, client_writer))
    clients[task] = (client_reader, client_writer)
    def client_done(task):
        del clients[task]
    task.add_done_callback(client_done)
