from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

orders = []

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    # Call product service to get product info
    product_service_url = f"http://product-service:5001/products/{product_id}"
    product_response = requests.get(product_service_url)

    if product_response.status_code != 200:
        return jsonify({"message": "Product not found"}), 404

    product = product_response.json()
    total_price = product["price"] * quantity

    order = {
        "id": len(orders) + 1,
        "product_id": product_id,
        "quantity": quantity,
        "total_price": total_price
    }
    orders.append(order)
    return jsonify(order), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
