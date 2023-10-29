from typing import Optional

from .vigenere_cypher import VigenereCypher


def vigenere_encrypt(text, key, reverse: Optional[bool] = False):
    if reverse:
        v_cypher = VigenereCypher("zyxwvutsrqponmlkjihgfedcba")
    else:
        v_cypher = VigenereCypher()

    encrypted = v_cypher.encrypt(text, key)
    return encrypted