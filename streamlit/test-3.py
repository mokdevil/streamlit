import os
import signal
import ssl

from tornado.options import define, options, parse_command_line
from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError
from tornado.ioloop import IOLoop
from tornado import gen


class EchoServer(TCPServer):
    @gen.coroutine
    def handle_stream(self, stream, address):
        while True:
            try:
                data = yield stream.read_until(b"\n")
                print(data)
            except StreamClosedError:
                break

def signal_init():
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

def ssl_config(cert, key):
    ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_ctx.load_cert_chain(cert, key)
    return ssl_ctx

def handle_signal(sig, frame):
    IOLoop.current().add_callback(IOLoop.current().stop)
    print("Exiting.")

def start_server(port, ssl_ctx):
    server = EchoServer(ssl_options=ssl_ctx)
    server.listen(port)
    IOLoop.current().start()

def main():
    define("port", type=int, default=8888, help="port to bind to")
    define("cert", type=str, default="host.cert", help="path to cert file")
    define("key", type=str, default="host.key", help="path to key file")
    options.parse_command_line()

    signal_init()
    ssl_ctx = ssl_config(cert=options.cert, key=options.key)
    start_server(options.port, ssl_ctx)

if __name__ == "__main__":
    main()