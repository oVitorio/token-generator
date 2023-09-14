# Token Generator

<p align="center">
 <a href="#-about">About</a> •
 <a href="#-features">Features</a> •
 <a href="#-layout">Layout</a> •
 <a href="#-how-to-run">How to Run</a> •
 <a href="#-technologies">Technologies</a> •
 <a href="#-contribution">Contribution</a> •
 <a href="#-license">License</a>
</p>

---

## 💻 About the project

This project contains a Flask application to generate random tokens with customizable character counts and salt values. It provides a friendly user interface for generating tokens with options to use a generic salt or provide a custom one.

Additionally, the application also offers an API to programmatically generate tokens through HTTP requests.

---

## ⚙️ Features

Generate random tokens with a specified character count.
Choose between using a generic salt or providing a custom one.
Copy generated tokens and salt values to clipboard.
View the SHA value of the token for security purposes.
API for programmatically generating tokens.

---

🚀 How to execute the project

Running the web application
To run the web application locally, follow these steps:

Clone the repository: git clone <https://github.com/your-username/token-generator.git>
Navigate to the project directory: cd token-generator
Install required dependencies: pip install -r requirements.txt
Run the Flask application: python app.py
Access the web application in your browser at <http://localhost:5000>
Running the API
You can use the API to programmatically generate tokens. Here are some ways to use it:

1. Using cURL
You can use cURL to make an HTTP POST request to the /generate_token API route. Here is an example:

``` bash

curl -X POST -H "Content-Type: application/json" -d '{
     "characterCount": 12,
     "useGenericSalt": true,
     "customSalt": "abc123"
}' 

```

<http://localhost:5000/generate_token>

This will return a JSON response with the generated token, salt value, and token SHA.

2. Using an HTTP library in your favorite programming language
You can use an HTTP library in your favorite programming language to make HTTP POST requests to the API route. Here is an example in Python using the requests library:

```python

import requests

url = 'http://localhost:5000/generate_token'
date = {
     'characterCount': 12,
     'useGenericSalt': True,
     'customSalt': 'abc123'
}

response = requests.post(url, json=data)
print(response.json())
```

This will also return a JSON response with the generated token, salt value, and token SHA.

### What is Salt?

Salt, in cryptography, is a random sequence of data that is added to the original data before being processed by a hashing algorithm. The main purpose of salt is to increase the security of passwords or sensitive data. When a salt is used, it makes each generated hash unique, even if the original data is the same.

### Why use Salt?

The use of salt is essential to mitigate dictionary and brute force attacks, where an attacker tries to guess passwords or original data by testing various combinations. Without salt, identical hashes would be generated for the same input, making it easier for an attacker to pre-calculate hashes and compare them to stored hashes.

### Usage of "useGenericSalt": true or false

In the context of this project, you have the option to choose between using a generic (default) salt or providing a custom salt when generating tokens. Here's how it works:

- When you set "useGenericSalt" to true (the default value), the system automatically generates a random salt for each token. This increases security as each generated token will have a unique hash due to the use of a different salt.

- When you set "useGenericSalt" to false, you have the option of providing a custom salt in the "customSalt" field. This allows you to control the salt used to generate the token. You can use a custom salt if you need to replay the same token at different times or situations, as long as you keep the custom salt consistent.

In short, the "useGenericSalt" determines whether a generic (random) salt or a custom salt should be used when generating tokens. Using a random salt is recommended for security purposes, while a custom salt is useful in specific scenarios where you need consistency in the tokens generated.

---

## 🛠 Technologies

- Flask: A Python web framework for building web applications.
- Bootstrap: A popular CSS framework for designing responsive web pages.
- Axios: A JavaScript library for making HTTP requests to the backend.
- bcrypt: A library for secure password hashing.
- secrets and string: Python libraries for generating random strings and salts.

---

## 💪 Contribution

Contributions to the project are welcome! Here's how you can contribute:

1. Fork the project.
2. Create a new branch for your feature: `git checkout -b my-feature`
3. Make your changes and commit them: `git commit -m "feature: My new feature"`
4. Push your changes to your fork: `git push origin my-feature`
5. Submit a pull request.

---

## 📝 License

This project is licensed under the [license-here](./LICENSE).
