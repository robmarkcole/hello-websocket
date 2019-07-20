## hello-websocket python3 BROKEN - see issues.md

Webcam over websocket in Python, using OpenCV and 
`Tornado <http://www.tornadoweb.org>`_.

## Details

The code runs a *recorder* process that continuously reads images
from the webcam. Upon every capture it writes the image to a Redis
key-value store.

Separately, a *server* process (running Tornado) handles websocket messages. 
Upon receiving a request message (sent from *client* web browser)
it retrieves the latest image from the Redis database and sends it 
to the *client* over websocket connection.

The *client* web page is dead simple: 
It sends an initial request on a WebSocket.
When image data comes in, it assigns it to ``src`` attribute of the
``<img>`` tag, then simply sends the next request. That's it!

# Installation
It is recommended to use a venv:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

# Usage
There are two separate programs that need to be running:

*recorder* - webcam capture process that writes to Redis database.
*server* - the Tornado server which reads current image from 
   the Redis database and serves to requesting WebSocket clients.

Make sure redis server is running with `redis-server` then run the recorder:
```python3 recorder.py```

Now (in a different shell) run the server:
```python3 server.py```
   
Go to http://localhost:9000 to view the webcam.

## References
* https://github.com/wildfios/Tornado-mjpeg-streamer-python
