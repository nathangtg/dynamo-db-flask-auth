import flask
import logging

# Routes
from .routes.UserRoute import UserRoute
from .routes.AuthRoute import AuthRoute

app = flask.Flask(__name__)

# Register routes
app.register_blueprint(UserRoute)
app.register_blueprint(AuthRoute)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
    logging.basicConfig(level=logging.INFO)