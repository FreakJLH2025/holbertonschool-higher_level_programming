#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json():
    json_path = os.path.join(os.path.dirname(__file__), 'products.json')
    try:
        with open(json_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def read_csv():
    csv_path = os.path.join(os.path.dirname(__file__), 'products.csv')
    products = []
    try:
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert id and price to proper types
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validar fuente
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source", products=[])

    # Filtrar por id si se proporciona
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in data if p.get("id") == product_id]
            if not filtered:
                return render_template('product_display.html', error="Product not found", products=[])
            data = filtered
        except ValueError:
            return render_template('product_display.html', error="Invalid id format", products=[])

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
