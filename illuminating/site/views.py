from flask import Blueprint

mod = Blueprint('site', __name__)

@mod.route('/')
def home():
	return "illuminating application"