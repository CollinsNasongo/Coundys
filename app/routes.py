from flask import Blueprint, jsonify
from .models import County

bp = Blueprint("main", __name__)

@bp.route("/counties", methods=["GET"])
def list_counties():
    counties = County.query.all()
    return jsonify([{"code": c.county_code, "name": c.county_name} for c in counties])
