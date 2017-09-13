from flask import Blueprint

mod = Blueprint('ml', __name__)

@mod.route('/')
def home():
	return "machine learning application"