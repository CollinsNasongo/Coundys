from flask import Flask, render_template, request, jsonify
from models import County
from db_connect import get_db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/api/county', methods=['POST'])
def create_county():
    """
    Creates a new county in the database.

    Parameters:
    - request: The incoming request object containing JSON data.

    Returns:
    - JSON response:
        - status (str): "success" or "error"
        - message (str): Optional message depending on success or error
        - county (dict): The newly created county dictionary (if successful)

    Raises:
    - SQLAlchemyError: If there is an error interacting with the database.
    """

    with get_db() as db:
        try:
            county_data = request.get_json()

            if not county_data:
                return jsonify({"status": "error", "message": "No data provided"}), 400

            required_fields = ["county_code", "county_name"]
            missing_fields = [field for field in required_fields if field not in county_data]

            if missing_fields:
                return jsonify({"status": "error", "message": f"Missing fields: {', '.join(missing_fields)}"}), 400

            new_county = County(
                county_code=county_data["county_code"],
                county_name=county_data["county_name"],
            )

            db.add(new_county)
            db.commit()

            return jsonify({
                "status": "success",
                "message": "County created successfully",
                "county": new_county.as_dict()
            }), 201

        except SQLAlchemyError as e:
            db.rollback()
            return jsonify({"status": "error", "message": str(e)}), 500
        
@app.route('/api/county', methods=['GET'])
def get_all_counties():
    """
    Retrieves all counties from the database.

    Returns a JSON response with the following structure:
        - status (str): "success" or "error"
        - message (str): Optional message depending on success or error
        - counties (list): List of county dictionaries (if successful)

    Raises:
        Exception: If an error occurs while retrieving the counties.

    Returns:
        json: A JSON response containing the status, message, and counties data.
    """
    try:
        with get_db() as db:
            counties = db.query(County).all()
            county_data = [county.as_dict() for county in counties]
            return jsonify({
                "status": "success",
                "message": "Counties retrieved successfully",
                "counties": county_data,
            }), 200

    except Exception as e:
        # Consider more specific exception handling
        print(f"Error retrieving counties: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

@app.route('/api/county/<county_code>', methods=['GET'])
def get_county_by_id(county_code):
    """
    Retrieves a specific county by its ID from the database.

    Args:
        county_id (int): The ID of the county to retrieve.

    Returns:
        JSON response:
            - status (str): "success" or "error"
            - message (str): Optional message depending on success or error
            - county (dict): County dictionary (if successful)
    """

    try:
        with get_db() as db:
            # Fetch county by ID
            county = db.query(County).get(county_code)

            if not county:
                raise NoResultFound(f"County with ID {county_code} not found")  # Raise specific exception

            # Convert county to dictionary and return success response
            return jsonify({
                "status": "success",
                "message": "County retrieved successfully",
                "county": county.as_dict(),
            }), 200

    except NoResultFound as e:
        # Handle not found error with specific message
        return jsonify({"status": "error", "message": str(e)}), 404

    except Exception as e:
        # Consider more specific exception handling
        print(f"Error retrieving county: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500



if __name__ == '__main__':
    app.run(debug=True)