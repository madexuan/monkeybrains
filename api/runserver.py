import os

from api import app
from api import connect_db

port = int(os.environ.get("PORT", 5000))
host = os.environ.get("HOST", '0.0.0.0')
connect_db(app)
app.run(port=port, host=host)
