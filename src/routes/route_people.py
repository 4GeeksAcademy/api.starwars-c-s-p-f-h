from flask import Blueprint, jsonify, request
from models import Planet
from models import db

people_bp=Blueprint('peoples', __name__,url_prefix="/people")