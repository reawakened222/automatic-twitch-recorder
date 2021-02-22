import threading
import sys

import ATRHandler
import utils
from atr_cmd import AtrCmd
from daemon import Daemon

if __name__ == '__main__':
    utils.get_client_id()  # creates necessary config before launch
    server = Daemon(('127.0.0.1', 1234), ATRHandler.ATRHandler)
    if len(sys.argv) > 1 and sys.argv[1] == "--default":
        default_config = utils.get_default_config()
        for streamer,quality in default_config:
            server.add_streamer(streamer, quality)
        threading.Thread(target=server.serve_forever).start()
        server.start()
    else:
        threading.Thread(target=server.serve_forever).start()
        AtrCmd().cmdloop_with_keyboard_interrupt()
