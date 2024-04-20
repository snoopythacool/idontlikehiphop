import os

from flask import Flask, redirect

def create_app():
  # create and configure the app
  app = Flask(__name__, instance_relative_config=True, template_folder='templates')

  @app.route("/")
  def redirect_to_menu():
    return redirect("/t/translations")

  from . import table, post
  app.register_blueprint(table.bp)
  app.register_blueprint(post.bp)

  return app