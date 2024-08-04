#!/usr/bin/python3
"""
Index page
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status():
    """Returns status code in json"""
    return jsonify({"status": "OK"})
