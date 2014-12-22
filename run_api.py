#!/usr/bin/env

# Backend API running script on port 5500
import api
from common import core
core.app.run(port=int("5500"), debug=True)



