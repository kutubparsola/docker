import time
from flask import Flask
from redis import Redis

app = Flask(__name__)
# Note: 'redis' here is the hostname, which will match our service name in docker-compose!
cache = Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except Exception as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello! This page has been viewed {count} times.\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)