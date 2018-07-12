# ./wsgi.py
from app import create_app
from Flask import response

application = create_app()

# @application.route("/")
# def home():
#     return response.make_response('Goodbye', 200)
