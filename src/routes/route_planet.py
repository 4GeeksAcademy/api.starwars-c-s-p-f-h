from flask import Blueprint, jsonify, request
from models import Planet
from models import db

planets_bp=Blueprint('planets', __name__,url_prefix="/planet")


