from flask import Flask, request
from flask_cors import CORS

from resources.product import Product, Products

app = Flask(__name__)
CORS(app, supports_credentials=True)  # Enables CORS for all routes. This is not recommend for production.
product = Product()
products = Products()


@app.route('/products/', methods=['POST'])
def create_products():
    return products.post(request)


@app.route('/qproducts', methods=['POST'])
def create_products_from_query():
    return products.post_query(request)


@app.route('/products/<string:pname>', methods=['GET'])
def get_order(pname):
    return product.get(pname)


@app.route('/products/<string:pname>/quantity', methods=['PUT'])
def update_order(pname):
    return product.put(pname, int(request.args.get('value')))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
