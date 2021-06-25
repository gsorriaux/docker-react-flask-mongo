  
from flask import Flask, g, jsonify

def create_app(testing: bool = True):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("server.config")

    app.register_blueprint(api_bp)
    app.register_error_handler(404, page_not_found)

    @app.before_request
    def before_request() -> None:
        g.testing = app.testing

    app.app_context().push()  # this is needed for application global context

    return app


application = create_app()