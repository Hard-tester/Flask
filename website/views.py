# here store standard routes or path user naviigation 
# blue

from flask import Blueprint, render_template # bluprint for application 


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")



