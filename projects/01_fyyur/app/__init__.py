from flask import Flask, render_template
from .extensions import db, migrate
import os

def create_app(test_config=None):
   app = Flask(__name__, instance_relative_config=True)

   if test_config == None:
      app.config.from_pyfile('config.py', silent=True)
   else:
      app.config.from_mapping(test_config)

   # create instance folder is does not exist
   try:
      os.makedirs(app.instance_path)
   except OSError:
      pass
   
   # initialize the app
   db.init_app(app)
   migrate.init_app(app, db)

   # Register my blueprints
   from .blueprints import blueprints
   for blueprint in blueprints:
      app.register_blueprint(blueprint)

   #app.add_url_rule('/', endpoint='index')
   @app.route('/')
   def home():
     return render_template('pages/home.html')

   return app

# Default port:
if __name__ == '__main__':
  create_app()
