from api import app
from api import connect_db

connect_db(app)
app.run(debug=True)
