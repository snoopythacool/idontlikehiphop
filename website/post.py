from flask import Blueprint, render_template, redirect, request
import json

bp = Blueprint('post', __name__, url_prefix='/post')

ALBUM_DATA_PATH = bp.root_path + "/transferred_data/album.json"

@bp.route("/<id>")
def table(id:str):

  with open(ALBUM_DATA_PATH, 'r') as file_read:
    album_dict = json.load(file_read)

  if id not in list(album_dict.keys()):
    redirect("/")
  album = album_dict[id]

  return render_template(f"translations/{id}.html", 
                         album=album)