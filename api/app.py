import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'fibonacci.sqlite'),
    # )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        from . import config
        app.config.from_object(config.Config())
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)


    from . import db
    db.init_app(app)

    from .fibonacci_module import fibonacci
    app.register_blueprint(fibonacci.bp)

    return app