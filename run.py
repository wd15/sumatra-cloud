#!/usr/bin/env

from app import app
app.debug = True
app.config['DEBUG'] = True
app.run(debug=True)



