from flask import Flask
from app.config import init_db, create_user, list_users, change_password

app = Flask(__name__)
app.secret_key = "your-secret"

# Register CLI commands
app.cli.add_command(init_db)
app.cli.add_command(create_user)
app.cli.add_command(list_users)
app.cli.add_command(change_password)
