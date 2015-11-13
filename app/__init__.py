from app.core.helper import create_app
from app.core.db import db
from app.user.views import user_views

# Development Config
config = 'config.dev'
# Production Config
# config = 'config.Prod'

app = create_app(config)
#db.init_app(app)
db.__init__(app)
# register blueprint
app.register_blueprint(user_views)
