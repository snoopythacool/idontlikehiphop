from flask import Blueprint, render_template, redirect, request
from os import path
import json

bp = Blueprint('report', __name__, url_prefix='/report')

ALBUM_DATA_PATH = bp.root_path + "/transferred_data/album.json"

@bp.route("/<id>")
def report(id:str):

  with open(ALBUM_DATA_PATH, 'r') as file_read:
    album_dict = json.load(file_read)

  if id not in list(album_dict.keys()):
    redirect("/")
  album = album_dict[id]

  return render_template(album=album)