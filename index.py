"""
This module contains a Flask application that handles a POST request to '/generate_token'. It receives data from the frontend, including the character count, whether to use a generic salt, and a custom salt. It then uses the GenerateToken class to generate a random token with the specified character count and salt value. The generated token, salt, and SHA value are returned as a JSON response.

Example Usage:
    ```python
    # POST request to '/generate_token'
    data = {
        'characterCount': 12,
        'useGenericSalt': True,
        'customSalt': 'abc123'
    }
    response = client.post('/generate_token', json=data)
    print(response.json())
    # Output: {'token': 'aBcDeFgHiJkL', 'salt': 'abc123', 'sha': '...'}
    ```

Attributes:
    app (Flask): The Flask application instance.

Routes:
    - '/' (GET): Renders the index.html template.
    - '/generate_token' (POST): Handles the generation of a custom token.

"""

from flask import Flask, render_template, request, jsonify, make_response
from backend.gen_token import GenerateToken

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the index.html template.

    Returns:
        str: The rendered HTML template.
    """
    return render_template('index.html')

@app.route('/generate_token', methods=['POST'])
def generate_custom_token():
    """
    Handles the generation of a custom token.

    Returns:
        Response: The Flask response object containing the generated token, salt, and SHA value.
    """
    # Get data from the form submitted by the frontend
    data = request.json
    # Get specific values from the data dictionary
    character_count = int(data.get('characterCount', 10))
    use_generic_salt = data.get('useGenericSalt')
    custom_salt = data.get('customSalt', '')
    token_generator = GenerateToken()
    token, salt, sha = token_generator.generate_token(character_count, use_generic_salt, custom_salt)
    print(sha)

    # Create a JSON response object
    response_data = {'token': token, 'salt': salt, 'sha': sha}

    # Create and return a Flask response
    response = make_response(jsonify(response_data))
    response.status_code = 200  # HTTP status code 200 (OK)

    return response

if __name__ == '__main__':
    app.run(debug=True)