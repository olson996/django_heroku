from waitress import serve
import os
from djangoproj.wsgi import application

if __name__ == '__main__':
    print("Starting on port 8000")
    serve(application, port='8000' or os.environ['PORT'])