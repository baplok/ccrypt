from cryptography.fernet import Fernet


class Crypt:

    def _generate_key(self):
        key = Fernet.generate_key()
        with open(".key", "wb") as fid:
            fid.write(key)
        return key

    def _encrypt(self, target, key=None):
        if key is None:
            key = self._generate_key()
        f = Fernet(key)
        bytestr = target.encode()
        return f.encrypt(bytestr)

    def _decrypt(self, target, key):
        f = Fernet(key)
        return f.decrypt(target).decode()
