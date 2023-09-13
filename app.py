from flask import Flask, render_template, request, jsonify, make_response
from backend.gen_token import GenerateToken

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_token', methods=['POST'])
def generate_custom_token():
    # Obtenha os dados do formulário enviado pelo frontend
    data = request.json
    # Obtenha os valores específicos do dicionário de dados
    quantidade_caracteres = int(data.get('quantidadeCaracteres', 10))
    usar_salt_generico = data.get('usarSaltGenerico')
    salt_personalizado = data.get('saltPersonalizado', '')
    token_generator = GenerateToken()
    token, salt, sha = token_generator.generate_token(quantidade_caracteres, usar_salt_generico, salt_personalizado)

    # Crie um objeto de resposta JSON
    response_data = {'token': token, 'salt': salt, 'sha': sha}

    # Crie e retorne uma resposta Flask
    response = make_response(jsonify(response_data))
    response.status_code = 200  # Código de status HTTP 200 (OK)

    return response

if __name__ == '__main__':
    app.run(debug=True)
