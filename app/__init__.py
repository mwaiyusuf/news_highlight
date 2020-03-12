from flask import Flask 
from flask_bootstrap import Bootstrap
from .config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
  
    app = Flask(__name__) #connecting to instance folder
  

    #creating  up configuration
    app.config.from_object(config_options[config_name]
    # app.config.from_object(DevConfig)
    # app.config.from_pyfile('config.py') #connectin to config.py

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
      # setting config
    from .requests import configure_request
    configure_request(app)

    # from app import views
    # from app import error
    return app