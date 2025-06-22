import click
from flask.cli import with_appcontext
from models import get_db, create_user_table
from auth import hash_password, prompt_password

@click.command("init-db")
@with_appcontext
def init_db():
    create_user_table()
    click.echo("✅ Database initialized.")

@click.command("create-user")
@click.argument("username")
@click.argument("role")
@with_appcontext
def create_user(username, role):
    password = prompt_password()
    db = get_db()
    db.execute(
        "INSERT INTO User (Username, PasswordHash, Role) VALUES (?, ?, ?)",
        (username, hash_password(password), role)
    )
    db.commit()
    click.echo(f"✅ User '{username}' created.")

@click.command("list-users")
@with_appcontext
def list_users():
    db = get_db()
    users = db.execute("SELECT Username, Role FROM User").fetchall()
    for u in users:
        click.echo(f"{u[0]} - {u[1]}")

@click.command("change-password")
@click.argument("username")
@with_appcontext
def change_password(username):
    password = prompt_password()
    db = get_db()
    db.execute(
        "UPDATE User SET PasswordHash = ? WHERE Username = ?",
        (hash_password(password), username)
    )
    db.commit()
    click.echo(f"🔐 Password updated for '{username}'.")
