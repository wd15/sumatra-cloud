#!/usr/bin/env

# Backend API running script on port 5500
from smt_api import app
app.run(port=int("5500"), debug=True)



