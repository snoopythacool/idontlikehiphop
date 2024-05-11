from flask import Blueprint, render_template, redirect, request
from random import choice, shuffle
from operator import itemgetter
import json

bp = Blueprint('table', __name__, url_prefix='/t')

TABLE_DATA_PATH = bp.root_path + "/transferred_data/table.json"
ALBUM_DATA_PATH = bp.root_path + "/transferred_data/album.json"

COLOUR_SCHEMES = [
  ["#F23535", "#F2E1C2", "/post/everythingisalive"],
  ["#D9BF41", "#3370A6", "/post/itsusvol1"],
  ["#FFFFFF", "#000000", "/post/slowdive"],
  ["#D9D5A3", "#261B24", "/post/souvlaki"],
  ["#E9F2EA", "#18594D", "/post/pygmalion"],
  ["#D96B2B", "#40211E", "/post/justforaday"],
  ["#F2F2F2", "#A67C6D", "/post/trailerpark"],
]

@bp.route("/<id>")
def table(id:str):

  with open(TABLE_DATA_PATH, 'r') as file_read:
    table_dict = json.load(file_read)
  chosen_table = table_dict[id]

  with open(TABLE_DATA_PATH, 'w') as file_write:
    json.dump(table_dict, file_write, indent=4)

  with open(ALBUM_DATA_PATH, 'r') as file_read:
    album_dict = json.load(file_read)

  id_list:list = chosen_table["list"]
  id_list.sort()
  album_list = []
  for album_id in id_list:
    album_list.append(album_dict[album_id])

  # Sorting Algorithm
  album_list = sorted(album_list, key=itemgetter('name'))
  sort = request.args.get('sort')
  if sort == "artist":
    album_list = sorted(album_list, key=itemgetter('artist'))
  elif sort == "time":
    album_list = sorted(album_list, key=itemgetter('time'), reverse=True)

  random_colour = choice(COLOUR_SCHEMES)
  
  hiphoplover = list("I DONT LIKE HIP HOP")
  shuffle(hiphoplover)
  hiphoplover = ''.join(hiphoplover)

  return render_template("table.html", 
                         table=chosen_table, 
                         table_len=range(len(album_list)), 
                         list=album_list,
                         primary_colour = random_colour[0],
                         secondary_colour = random_colour[1],
                         choosen_link = random_colour[2],
                         like_hiphop = hiphoplover)