from flask import request, jsonify
from app import app, db, vision_client, firebase_db
from app.models import Product, Log

@app.route("/register_product", methods=["POST"])
def register_product():
    data = request.get_json()
    product = Product(name=data["name"], image_url=data["image_url"])
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product registered successfully"})

@app.route("/search_products", methods=["GET"])
def search_products():
    query = request.args.get("query")
    products = Product.query.filter(Product.name.like("%" + query + "%")).all()
    return jsonify([{"id": p.id, "name": p.name, "image_url": p.image_url} for p in products])

@app.route("/analyze_image", methods=["POST"])
def analyze_image():
    data = request.get_json()
    image_data = data["image_data"]
    response = vision_client.annotate_image(image_data)
    labels = [label.description for label in response.label_annotations]
    return jsonify({"labels": labels})

@app.route("/log", methods=["POST"])
def log():
    data = request.get_json()
    log = Log(timestamp=data["timestamp"], message=data["message"])
    db.session.add(log)
    db.session.commit()
    return jsonify({"message": "Log saved successfully"})