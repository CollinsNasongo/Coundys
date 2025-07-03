from flask import Blueprint, jsonify
from .models import County
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from . import db

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    try:
        # Try a trivial DB query
        db.session.execute(text("SELECT 1"))
        return jsonify(message="✅ Database is running and connected.")
    except OperationalError:
        return jsonify(message="❌ Database is NOT available."), 500

@bp.route("/counties", methods=["GET"])
def list_counties():
    counties = County.query.all()
    return jsonify([{"code": c.county_code, "name": c.county_name} for c in counties])
