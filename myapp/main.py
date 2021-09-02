import os
import sys
from os.path import dirname, abspath, join

sys.path.append(os.getcwd())
PROJECT_DIR = dirname(dirname(abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)

from os.path import join, dirname, abspath

from flask import Flask


# app = Flask(__name__)
def create_app(config_object="myapp.settings"):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(
        __name__.split(".")[0],
        template_folder=join(PROJECT_DIR, "myapp"),
        static_folder=join(PROJECT_DIR, "myapp", "static"),
    )
    app.config.from_object(config_object)
    # app.json_encoder = CustomJSONEncoder
    # register_logging(app)
    # register_extensions(app)
    register_blueprints(app)

    # register_errorhandlers(app)
    # register_shellcontext(app)
    # register_commands(app)

    return app


def register_blueprints(app):
    """Register Flask blueprints."""

    # from StudentInfoMgr.views.admin import admin
    #
    # app.register_blueprint(admin)

    # from api.v1.resources.index import api
    # app.register_blueprint(api, url_prefix='/api/v1/index')

    from myapp.api.v1 import api as api_1_0_blueprint

    app.register_blueprint(api_1_0_blueprint, url_prefix="/api/v1")

    # from StudentInfoMgr.jobs import jobs as jobs_blueprint
    # app.register_blueprint(jobs_blueprint, url_prefix='/api/v1')

    # app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # from StudentInfoMgr.api.v1 import api2 as api2_1_0_blueprint
    # app.register_blueprint(api2_1_0_blueprint, url_prefix='/api/v1')

    # from StudentInfoMgr.user.index import admin
    # app.register_blueprint(admin)

    return None


app = create_app()


@app.route("/")
def helloWorld():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
