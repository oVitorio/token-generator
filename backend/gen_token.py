import secrets
import string
import bcrypt

class GenerateToken:
    @staticmethod
    def generate_salt():
        characters = string.ascii_letters + string.digits
        salt_generico = ''.join(secrets.choice(characters) for _ in range(20))
        return salt_generico
    
    @staticmethod
    def generate_token(quantidade_caracteres=10, usar_salt_generico=True, salt_personalizado=""):
        characters = string.ascii_letters + string.digits
        token = ''.join(secrets.choice(characters) for _ in range(quantidade_caracteres))
        
        if usar_salt_generico:
            salt = GenerateToken.generate_salt()
        else:
            salt = salt_personalizado
        
        # Verifique se token e salt não estão vazios antes de chamar generate_sha
        if token and salt:
            sha = GenerateToken.generate_sha(token, salt)
            return token, salt, sha
        else:
            return None, None, None  # Tratar o caso em que token ou salt é vazio

    @staticmethod
    def generate_sha(token, salt):
        return str(bcrypt.kdf(
            password=token.encode('utf-8'),
            salt=salt.encode('utf-8'),
            desired_key_bytes=32,
            rounds=len(salt) ** 2))
