from flask import Blueprint, render_template, redirect, request
from os import path
import json

bp = Blueprint('post', __name__, url_prefix='/post')

ALBUM_DATA_PATH = bp.root_path + "/transferred_data/album.json"

@bp.route("/<id>")
def post(id:str):

  with open(ALBUM_DATA_PATH, 'r') as file_read:
    album_dict = json.load(file_read)

  if id not in list(album_dict.keys()):
    redirect("/")
  album = album_dict[id]

  return render_template(f"translations/{id}.html", 
                         album=album)

@bp.route("/<id>/<version>")
def postv(id:str, version:str):

  with open(ALBUM_DATA_PATH, 'r') as file_read:
    album_dict = json.load(file_read)

  if id not in list(album_dict.keys()):
    redirect("/")
  album = album_dict[id]

  if int(version) < album["version"]:
    return render_template(f"translations/versions/{id}_v{version}.html", 
                         album=album,
                         version=int(version))
  else:
    return redirect(f"/post/{id}")