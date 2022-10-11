from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from werkzeug.exceptions import NotFound
from finetune.finetune import fineclass

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
bootstrap = Bootstrap(app)
db.init_app(app)

def filt_gpt(text):
    if ('выход:' in text):
        arr = text.split('выход:')
        text = ' '.join(arr[1: ])
    
    while ('ютуб' in text):
        text = text.replace('ютуб', '')
        
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 
                'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'э',
                'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 
                'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш',
                'Щ', 'Э', 'Ю', 'Я']

    while (text[0] not in alphabet):
        if (len(text) == 1):
            return 'Please restart the program'
        text = text[1:]
    
    while ('--' in text):
        text = text.replace('--', '—')
    
    return text

class Saving(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    string = db.Column(db.String, unique=True, nullable=True)

with app.app_context():
    db.create_all()
    try:
        saving = db.get_or_404(Saving, 1)
    except NotFound:
        saving = Saving(
            string='',
        )
        db.session.add(saving)
        db.session.commit()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    response = request.get_json()
    if response['code'] == 'ZaNashix228':
        return jsonify({'success': True})
    return jsonify({'success': False})

@app.route('/scenario', methods=['GET', 'POST'])
def scenario():
    saving = db.get_or_404(Saving, 1)
    if request.method == 'POST':
        response = request.get_json()
        if response['scenario']:
            saving.string = response['scenario']
            db.session.add(saving)
            db.session.commit()
            return jsonify({'scenario': saving.string})
        else:
            return jsonify({'mess': 'no scenario was provided'})
    return jsonify({'scenario': saving.string})

@app.route('/continue', methods=['POST'])
def replic_continue():
    response = request.get_json()
    print(response)
    if response['replic']:
        return jsonify({'replic': response['replic']})

@app.route('/response', methods=['POST'])
def replic_response():
    response = request.get_json()
    if response['replic']:
        text = fineclass('вход:\n-{0}\nвыход: '.format(response['replic']))
        print(text)
        output_text = filt_gpt(text)
        return jsonify({
            'replic': output_text
        })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True)
