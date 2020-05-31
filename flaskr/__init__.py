import os

from flask import Flask

def create_app(test_config=None):
    test_config = None
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    from werkzeug.local import LocalProxy
    from flask import current_app
    logger = LocalProxy(lambda: app.logger)
    logger.debug("create_app")
    logger.info("app.instance_path: " + app.instance_path)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #from . import db
    #db.init_app(app)
    from flaskr.database import init_db
    from flaskr.database import db_session
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
    init_db()

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
