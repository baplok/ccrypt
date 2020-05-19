from ccrypt import Crypt


def test_create_file(tmpdir):
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 1


def test_encrypt(tmpdir):
    c = Crypt()
    s = "Hello world!"
    enc = c._encrypt(s)
    assert enc is not str


def test_enc_dec(tmpdir):
    c = Crypt()
    s = "Hello world!"
    enc = c._encrypt(s)
    with open('.key', 'rb') as fid:
        key = fid.read()
    dec = c._decrypt(enc, key)
    assert dec == s
