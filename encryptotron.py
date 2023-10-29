import click
from app.application import vigenere_encrypt


def v_cypher_encrypt(text, key, reverse):
    return vigenere_encrypt(text, key, reverse)


def c_cypher_encrypt(text, key, *args):
    return "Not yet implemented"


@click.group()
def cli():
    pass


@cli.command()
@click.option('-t', '--text', type=str, help="Text to be encrypted")
@click.option('-k', '--key', type=str, help="Encryption key")
@click.option('-c', '--cypher', type=str,
              help="The selected cypher. Use `encryptotron cypher --list` for a list of valid cyphers")
@click.option('-r', '--reverse', is_flag=True, help="Reverse the alphabet for a vigenere cypher")
def encrypt(text: str, key: str, cypher: str, reverse):
    cyphers = {"vigenere": v_cypher_encrypt, "ceaser": c_cypher_encrypt}
    if cypher not in cyphers.keys():
        raise ValueError("Please choose a valid cypher")
    click.echo(cyphers[cypher](text, key, reverse))