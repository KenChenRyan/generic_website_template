from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt

#Everything that's commented out is related to the current lack of need for a db and users

#db = SQLAlchemy()
#bcrypt = Bcrypt()
#login_manager = LoginManager()
#login_manager.login_view = 'users.login'
#login_manager.login_message_category = 'info'

#def create_app(config_class=Config):
def create_app():
    app = Flask(__name__)
#    app.config.from_object(Config)

#    db.init_app(app)
#    bcrypt.init_app(app)
#    login_manager.init_app(app)

    from website.users.routes import users
    from website.classes.routes import classes
    from website.main.routes import main
    app.register_blueprint(classes)
    app.register_blueprint(users)
    app.register_blueprint(main)

    return app
