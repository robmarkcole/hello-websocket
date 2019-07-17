# issues
On connecting to the stream:
```
ERROR:tornado.application:Uncaught exception GET /ws (::1)
HTTPServerRequest(protocol='http', host='localhost:9000', method='GET', uri='/ws', version='HTTP/1.1', remote_ip='::1')
Traceback (most recent call last):
  File "/Users/robincole/Documents/GitHub/hello-websocket/venv/lib/python3.7/site-packages/tornado/websocket.py", line 649, in _run_callback
    result = callback(*args, **kwargs)
  File "server.py", line 48, in on_message
    image_pil = Image.open(image_filename) # PIL.JpegImagePlugin.JpegImageFile
  File "/Users/robincole/Documents/GitHub/hello-websocket/venv/lib/python3.7/site-packages/PIL/Image.py", line 2822, in open
    raise IOError("cannot identify image file %r" % (filename if filename else fp))
OSError: cannot identify image file 'tempfile.jpg'
```
Possibly https://stackoverflow.com/questions/19230991/image-open-cannot-identify-image-file-python
Overcome by introducing a sleep in recorder