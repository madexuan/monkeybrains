from itsdangerous import URLSafeTimedSerializer

from server import app


ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])
