from flask import Flask, request, jsonify
from flask_cors import CORS
from modele_ia import predire_collecte

app = Flask(__name__)
CORS(app) # Permet à ton site HTML de parler avec Python

@app.route('/predire', methods=['POST'])
def predire():
    data = request.json
    m1 = float(data['m1'])
    m2 = float(data['m2'])
    m3 = float(data['m3'])

    resultat = predire_collecte(m1, m2, m3)

    return jsonify({'prediction': resultat})

if __name__ == '__main__':
    app.run(port=5000, debug=True)