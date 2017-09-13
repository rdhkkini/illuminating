from flask import Blueprint

mod = Blueprint('data', __name__)

@mod.route('/')
def home():
	return "data collection application"