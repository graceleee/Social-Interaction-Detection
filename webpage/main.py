# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



import datetime

from flask import Flask, render_template, request, g, current_app, jsonify
from google.auth.transport import requests
from google.cloud import datastore
import google.oauth2.id_token
import pymongo
import urllib.request
import json

# from db import *

firebase_request_adapter = requests.Request()

# [START gae_python37_datastore_store_and_fetch_user_times]
datastore_client = datastore.Client()

# [END gae_python37_datastore_store_and_fetch_user_times]
app = Flask(__name__)



@app.route('/')
def root():
    return render_template(
        'index.html'
    )



if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8081, debug=True)

# the backend should