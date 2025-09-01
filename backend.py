from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://torooh:BTruto12883@@localhost/zaohub_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# -----------------
# Database Models
# -----------------
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('farmer', 'consumer'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    products = db.relationship('Product', backref='farmer', lazy=True)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10,2), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    farmer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# -----------------
# Routes
# -----------------
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        role=data['role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        session['user_id'] = user.id
        session['role'] = user.role
        return jsonify({"message": "Login successful", "role": user.role}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/add_product', methods=['POST'])
def add_product():
    if 'user_id' not in session or session['role'] != 'farmer':
        return jsonify({"message": "Unauthorized"}), 403

    data = request.json
    new_product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        quantity=data.get('quantity', 1),
        farmer_id=session['user_id']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"}), 201

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    output = []
    for p in products:
        output.append({
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "price": float(p.price),
            "quantity": p.quantity,
            "farmer": p.farmer.name
        })
    return jsonify(output), 200

# -----------------
# Run the app
# -----------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
