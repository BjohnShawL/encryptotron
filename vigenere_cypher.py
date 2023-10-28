from typing import Optional


class VigenereCypher:
    default_alphabet = "abcdefghijklmnopqrstuvwxyz"

    # TODO: handle spaces
    def __init__(self, alphabet: Optional[str] = None):
        if not alphabet:
            self.alphabet = list(self.default_alphabet)
        else:
            self.alphabet = list(alphabet)

    def determine_c_index(self, char):
        return self.alphabet.index(char)

    @staticmethod
    def wrap_key(length, key: str):
        wrapped = ""
        for i in range(length):
            key_index = i % len(key)

            wrapped += key[key_index]
        return wrapped

    def encrypt(self, plaintext, key) -> str:
        encrypted = []
        wrapped_key = self.wrap_key(len(plaintext), key.lower())

        for idx, letter in enumerate(plaintext.lower()):
            plain_letter_index = self.alphabet.index(letter)  # this is the index of the letter in the alphabet
            key_index_letter = wrapped_key[idx]  # this is the letter which corresponds to the index in the key
            key_letter_index = self.alphabet.index(key_index_letter)  # index of the key index letter
            encryption_index = plain_letter_index + key_letter_index
            encrypted_letter = self.alphabet[encryption_index % len(self.alphabet)]

            encrypted.append(encrypted_letter)
        return "".join(encrypted)

    def decrypt(self, encrypted, key) -> str:
        plaintext = []
        wrapped_key = self.wrap_key(len(encrypted), key.lower())

        for idx, letter in enumerate(encrypted):
            key_index_letter = wrapped_key[idx]
            key_letter_index = self.alphabet.index(key_index_letter)
            encrypted_letter_index = self.alphabet.index(letter)
            decryption_index = encrypted_letter_index - key_letter_index
            plain_text_letter = self.alphabet[decryption_index % len(self.alphabet)]
            plaintext.append(plain_text_letter)
        return "".join(plaintext)


if __name__ == "__main__":
    x = VigenereCypher()
    key = "MochiSucks"
    print(x.decrypt("rfqwxqcukoqgqtm", key))