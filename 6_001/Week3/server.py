import json
import mimetypes
import os
from wsgiref.simple_server import make_server


cur_dir = os.path.realpath(os.path.dirname(__file__))
app_root = os.path.join(cur_dir, "static")


def parse_post(environ):
    try:
        body_size = int(environ.get("CONTENT_LENGTH", 0) ) # Default 0
    except:
        body_size = 0

    if not body_size:
        return {}

    body = environ["wsgi.input"].read(body_size)
    return json.loads(body)

def application(environ,start_response):
    status = '200 OK'
    path = environ.get("PATH_INFO","/") or "/"
    static_file = None
    params = parse_post(environ)
    for key,value in environ.items():
        print(key,value)

    print(params)
    print(f"Requested path {path}/{params}")
    print(path)
    try:
        if path == "/":
            static_file = "index.html"

        else:
            print(path)
            static_file = path[1:]
            print(static_file)
    except IOError as e:
        body = None

    test_fname = os.path.join(app_root, static_file)
    print(test_fname)
    if os.path.isfile(test_fname):
        with open(test_fname, "rb") as f:
            body = f.read()
        status = "200 OK"
        type_ = mimetypes.guess_type(test_fname)[0] or "text/plain"
    else:
        body = b"File not found: %r" % test_fname
        status = "404 FILE NOT FOUND"
        type_ = "text/plain"

    len_ = str(len(body))
    headers = [("Content-type", type_), ("Content-length", len_)]
    start_response(status, headers)
    return [body]


if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 8000

    with(make_server('0.0.0.0',PORT,application)) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt or OSError as e:
            print("Shutting Down with error",e)
            httpd.shutdown()


