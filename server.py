"""
Serve webcam images from a Redis store using Tornado.
Usage:
   python3 server.py
"""

import base64
import io
import time
from PIL import Image
from PIL import ImageFile

import coils
import numpy as np
import redis
from tornado import websocket, web, ioloop


MAX_FPS = 1

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('index.html')

class SocketHandler(websocket.WebSocketHandler):
    """ Handler for websocket queries. """
    
    def __init__(self, *args, **kwargs):
        """ Initialize the Redis store and framerate monitor. """

        super(SocketHandler, self).__init__(*args, **kwargs)
        self._store = redis.Redis()
        self._fps = coils.RateTicker((1, 5, 10))
        self._prev_image_id = None
        ImageFile.LOAD_TRUNCATED_IMAGES = True

    def on_message(self, message):
        """ Retrieve image ID from database until different from last ID,
        then retrieve image, de-serialize, encode and send to client. """

        while True:
            time.sleep(1./MAX_FPS)
            image_id = self._store.get('image_id')
            if image_id != self._prev_image_id:
                break
        self._prev_image_id = image_id
        image_filename = self._store.get('image').decode() # tempfile
        try:
            image_pil = Image.open(image_filename) # PIL.JpegImagePlugin.JpegImageFile
            image_base64 = base64.b64encode(image_pil.tobytes()) # base64 string
            self.write_message(image_base64)

            # Print object ID and the framerate.
            text = '{} {:.2f}, {:.2f}, {:.2f} fps'.format(id(self), *self._fps.tick())
            print(text)
        except:
            pass

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
])

if __name__ == '__main__':
    app.listen(9000)
    print('visit localhost:9000')
    ioloop.IOLoop.instance().start()
