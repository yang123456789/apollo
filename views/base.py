import json
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
from conf.config import KEY


class Render:
    def __init__(self, code, message, result):
        self.code = code
        self.message = message
        self.result = result
        self.data = self.render()

    def render(self):
        data = dict(code=self.code, message=self.message, result=self.result)
        return json.dumps(data)


class RenderJson(Render):
    def __init__(self, code, message, result):
        super(RenderJson, self).__init__(code, message, result)


def render_json(code, message, result):
    msg = RenderJson(code, message, result)
    return msg.data


def render_200(message=None, data=None):
    message = render_json(200, message, data)
    return message


def render_201(message=None, data=None):
    message = render_json(201, message, data)
    return message


def render_400(message=None, data=None):
    message = render_json(400, message, data)
    return message


def render_401(message=None, data=None):
    message = render_json(401, message, data)
    return message


def render_403(message=None, data=None):
    message = render_json(403, message, data)
    return message


def render_404(message=None, data=None):
    message = render_json(404, message, data)
    return message


def render_406(message=None, data=None):
    message = render_json(406, message, data)
    return message


def render_410(message=None, data=None):
    message = render_json(410, message, data)
    return message


def render_409(message=None, data=None):
    message = render_json(409, message, data)
    return message


def render_412(message=None, data=None):
    message = render_json(412, message, data)
    return message


def render_500(message=None, data=None):
    message = render_json(500, message, data)
    return message


def utf8(string):
    if isinstance(string, bytes):
        return string.decode('utf-8')
    return string


def encrypt(secret_key):
    public_key = KEY['public']
    rsa_key = RSA.importKey(public_key)
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    password = base64.b64encode(cipher.encrypt(secret_key.encode(encoding="utf-8")))
    return utf8(password)


def decrypt(secret_key):
    private_key = KEY['private']
    rsa_key = RSA.importKey(private_key)
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    password = cipher.decrypt(base64.b64decode(secret_key), '')
    return password

