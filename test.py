import requests


def register(username, password, phone, email):
    url = 'http://localhost:8000/register'
    data = dict(username=username, password=password, phone=phone, email=email)
    req = requests.post(url, json=data)
    print(req)
    print(req.content)
register('yangjia', 'Admin@1233', '18730273263', '123123@qq.com')

'''
from Crypto import Random
from Crypto.PublicKey import RSA
from pprint import pprint


random_generator = Random.new().read
rsa = RSA.generate(1024, random_generator)

# private_pem = rsa.exportKey()
# print(private_pem)
# public_pem = rsa.publickey().exportKey()
# print(public_pem)
KEY = {
    'private': b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDA8TDW0Mzm01QStkxyZW98Y3GbmwQhsZFx8TQ6ViT9bs4zzKPX\ndFwme3D9W7mOADdA/qJpjuegkVeBjy1DsJ5Ge91vG0C97vQOgib2bd3oSiy6FZp9\nzwPMY3jxnoA5LkaPp8kf8d51e0/q5AQrs0NOldr8oO5MHlDffgsF9kGuDwIDAQAB\nAoGBAI1WIXi7K95LIGM0t3t1Yt2z2x0pyTUFZo4ZKzEwuZgM+3Bmj/7cdkSaWILA\nFoU3E0LBRSgeTv8IeRmnUHktgELLcrkITx40oGhXHJOaGs2sQjQkjp2cuOUfs38q\nlsSbytoXOeQIc0NiXOOS+lzqHp8E87Qribqu1SGaZKy1p5FBAkEA0Rm3Y7hD07ux\nXC0pSMMdS/ysz0EcBNEqHViR60L1K0lEoq9LKylKYq5B+6EnM35BGzE0UE+WX4VH\ny6iXsQR29QJBAOw3r2HUSnpxliTiEXMuHnCk2gEu7JYTZbG15tAsa19vgQQOS7LV\nA7vuSZB5+A+vKYez2BpeQsZY1gZj7bmMhnMCQB9ocXd1EhsXskhaMD1RsXDcf0iS\nSxceI+lMiH6CDDl4Q+r70ZqmFRpFenvFdRHzAOyIs4bsrXWjm2kn5cEdHpECQQDe\neWO449RxleEvQ6vjqyAIP3sDekpg3kv9H7EPh4ZpD/+W7k/lUjJ+IWMvq3AydWrL\n4Fo8G2MQpEKPKjaPdwZ5AkB1NqfDG3CpChxAEdt0eI3nCJpMQQwbv0Qnf3R++DqF\nHC7LZmd5YtLr71oVNGyaL2rR0IAYhVn+llh/4l+9oVef\n-----END RSA PRIVATE KEY-----',
    'public': b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA8TDW0Mzm01QStkxyZW98Y3Gb\nmwQhsZFx8TQ6ViT9bs4zzKPXdFwme3D9W7mOADdA/qJpjuegkVeBjy1DsJ5Ge91v\nG0C97vQOgib2bd3oSiy6FZp9zwPMY3jxnoA5LkaPp8kf8d51e0/q5AQrs0NOldr8\noO5MHlDffgsF9kGuDwIDAQAB\n-----END PUBLIC KEY-----'
}

from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64


def encrypt(secret_key):
    public_key = KEY['public']
    rsa_key = RSA.importKey(public_key)
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    password = base64.b64encode(cipher.encrypt(secret_key.encode(encoding="utf-8")))
    return password
# print(encrypt('admin'))


def decrypt(secret_key):
    private_key = KEY['private']
    rsa_key = RSA.importKey(private_key)
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    password = cipher.decrypt(base64.b64decode(secret_key), '')
    return password
print(decrypt('nzS6fQaZG9I38sGYt/JdRNXd1BlwZMtztTEFNNJXNDzZg8lYrYFz0n/MnU5pmi13wj5EybYqHMXiec9mYa9MTHUbs+iS7AjT7MFcwtjdBlvvyHv8iRb/a7+l9Q12ae5kQnvI6lLtEW+T2ncTiuxpdGHrPa90kEBH2T01CjsXkz0='))
'''
