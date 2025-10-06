from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per minute"],
    storage_uri="redis://localhost:6379"  # Redis running locally
)

@app.route('/')
@limiter.limit("10 per minute")
def home():
    return "Welcome with Redis-backed rate limiting!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
