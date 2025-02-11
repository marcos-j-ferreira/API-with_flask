from flask import Blueprint, jsonify
from app.model import products

api_bp = Blueprint('api', __name__)

@api_bp.route('/products', methods=['GET'])
def get_products():
 
    result = [{"id": p.id, "name": p.name, "price": p.price} for p in products]
    return jsonify(result)
