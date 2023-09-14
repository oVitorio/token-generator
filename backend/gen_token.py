import secrets
import string
import bcrypt

class GenerateToken:
    @staticmethod
    def generate_salt():
        """
        Generate a random salt value.

        Returns:
            str: The generated salt value.
        """
        characters = string.ascii_letters + string.digits
        generic_salt = ''.join(secrets.choice(characters) for _ in range(20))
        return generic_salt
    
    @staticmethod
    def generate_token(character_count=10, use_generic_salt=True, custom_salt=""):
        """
        Generate a random token with a specified character count and salt value.

        Args:
            character_count (int, optional): The number of characters in the token. Defaults to 10.
            use_generic_salt (bool, optional): Whether to use a generic salt value. Defaults to True.
            custom_salt (str, optional): A custom salt value to use. Defaults to "".

        Returns:
            tuple: A tuple containing the generated token, salt, and SHA value.
        """
        characters = string.ascii_letters + string.digits
        token = ''.join(secrets.choice(characters) for _ in range(character_count))
        
        if use_generic_salt:
            salt = GenerateToken.generate_salt()
        else:
            salt = custom_salt
        
        # Check if token and salt are not empty before calling generate_sha
        if token and salt:
            sha = GenerateToken.generate_sha(token, salt)
            return token, salt, sha
        else:
            return None, None, None  # Handle the case where token or salt is empty

    @staticmethod
    def generate_sha(token, salt):
        """
        Generate a secure hash algorithm (SHA) value for a given token and salt.

        Args:
            token (str): The token to generate the SHA value for.
            salt (str): The salt value to use in the SHA generation.

        Returns:
            str: The generated SHA value.
        """
        return str(bcrypt.kdf(
            password=token.encode('utf-8'),
            salt=salt.encode('utf-8'),
            desired_key_bytes=32,
            rounds=len(salt) ** 2))
