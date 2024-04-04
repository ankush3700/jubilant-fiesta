import asyncio
import socket
import time


class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))
        resp = self.model(message)
        print('Send: {!r}'.format(f'{resp}'))
        self.transport.write(b'False')
    # Do something here
    def model(self, domain):
        asyncio.sleep(1)
        return False

async def main():
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        '127.0.0.1', 5336)

    async with server:
        await server.serve_forever()

asyncio.run(main())
