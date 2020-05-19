import click
from .crypt import Crypt


@click.group()
def ccrypt():
    """A simple Cryptgraphy wrapper"""
    pass


@ccrypt.command()
@click.argument('fp', nargs=1)
def encrypt(fp):
    c = Crypt()
    with open(fp, 'r') as fid:
        file_contents = fid.read()
    with open(fp, 'wb') as fid:
        enc = c._encrypt(file_contents)
        fid.write(enc)


@ccrypt.command()
@click.option("--key", "key_path", default=".key")
@click.argument("fp", nargs=1)
def decrypt(key_path, fp):
    c = Crypt()
    with open(fp, 'rb') as fid:
        target = fid.read()
    with open(key_path, 'rb') as fid:
        key = fid.read()
    with open(fp, 'w') as fid:
        dec = c._decrypt(target, key)
        fid.write(dec)
