from flask import Blueprint

mod = Blueprint('ann', __name__)

@mod.route('/')
def home():
	return "annotation application"