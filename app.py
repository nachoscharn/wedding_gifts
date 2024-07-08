from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///regalos.db'
db = SQLAlchemy(app)

class Regalo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    regalo = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    transferencia = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Regalo {self.nombre}>'

@app.route('/')
def index():
    return "Backend funcionando"

@app.route('/submit-gift', methods=['POST'])
def submit_gift():
    nombre = request.form['name']
    email = request.form['email']
    regalo = request.form['gift']
    monto = request.form['amount']
    transferencia = request.form['transaction']

    nuevo_regalo = Regalo(nombre=nombre, email=email, regalo=regalo, monto=monto, transferencia=transferencia)
    db.session.add(nuevo_regalo)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
