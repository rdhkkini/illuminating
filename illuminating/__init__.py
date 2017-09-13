from flask import Flask

app = Flask(__name__)

from illuminating.site.views import mod
from illuminating.data.views import mod
from illuminating.ann.views import mod
from illuminating.ml.views import mod

app.register_blueprint(site.views.mod)
app.register_blueprint(data.views.mod, url_prefix='/data')
app.register_blueprint(ann.views.mod, url_prefix='/ann')
app.register_blueprint(ml.views.mod, url_prefix='/ml')