from nacl.public import PrivateKey, SealedBox
import base64
import os

def load_private_key_from_b64(private_key_b64: str) -> PrivateKey:
    """
    Decodes a base64 encoded private key into a PrivateKey object.
    """
    try:
        return PrivateKey(base64.b64decode(private_key_b64))
    except Exception as e:
         raise ValueError(f"Invalid Private Key: {str(e)}")

def decrypt_ciphertext_b64(ciphertext_b64: str, private_key) -> str:
    """
    Decrypts a base64 encoded ciphertext using the provided private key.
    private_key can be a base64 string or a PrivateKey object.
    """
    try:
        if isinstance(private_key, str):
            sk = PrivateKey(base64.b64decode(private_key))
        else:
            sk = private_key

        box = SealedBox(sk)

        ciphertext = base64.b64decode(ciphertext_b64)
        plaintext_bytes = box.decrypt(ciphertext)
        return plaintext_bytes.decode("utf-8")
    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")
