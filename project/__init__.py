from flask import Flask
from .blueprints.add_user.add_user import add_user_bp
from .blueprints.add_user.extensions import db
from .backhround_processor import celery_init_app

def create_app():

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/himasha-105522/Data-Science/Flask-Blueprint/CRM.db"
    app.config["SECRET_KEY"] = "IAMTHEONEWHOKNOCKS"
    app.config['CELERY_CONFIG'] = {
                                    'broker_url': 'redis://127.0.0.1:6379' ,
                                    'result_backend' : 'redis://127.0.0.1:6379'
                                }
    
    celery = celery_init_app(app=app)

    #register the blueprint
    app.register_blueprint(add_user_bp)
    # integrate db to the app
    db.init_app(app=app)

    return app , celery
