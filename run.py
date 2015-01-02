"""Usage: run.py [--port=<port>] [--api | --view] [--debug | --no-debug]

--api           run the api app on port 5500
--view          run the view app on port 5000
--port=<port>   set the port number

"""
from docopt import docopt
arguments = docopt(__doc__, version='0.1dev')

port = arguments['--port']
debug = not arguments['--no-debug']

if arguments['--api']:
    from smt_api import app
    if not port: port = 5500
else:
    from smt_view import app
    if not port: port = 5000

app.run(debug=debug, port=int(port))

