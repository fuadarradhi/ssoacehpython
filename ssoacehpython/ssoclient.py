import json
import base64
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


class SSOResult:
    """
    Result dari parse Token, didefinisikan hanya valid,
    sisanya akan dilooping dari JSON.
    """

    def __init__(self, valid):
        self.mapping = {
            "id": "SessionID",
            "nk": "NIK",
            "np": "NIP",
            "nm": "Nama",
            "hp": "HP",
            "em": "Email",
            "tl": "TelegramID",
            "ea": "EmailAlternatif",
            "av": "Avatar",
            "dt": "Datetime"
        }
        self.valid = valid


class SSOClient:

    def __init__(self, jsonpath):
        """
        Base class sso client untuk bahasa python,
        load sso_secure.json saat init.
        """
        try:
            with open(jsonpath) as json_file:
                data = json.load(json_file)
                for key, value in data.items():
                    setattr(self, key, value)

        except Exception as e:
            print("Parse Json File Error : {}".format(str(e)))

    def ParseToken(self, token):
        """
        Main method sso client untuk bahasa python,
        parse token dan result menjadi SSOResult.
        """

        result = SSOResult(valid=False)

        try:
            """
            Token dan privateKey masih dalam format Base64 Url safe,
            decode terlebih dahulu.
            """
            decoded_private_key = base64.urlsafe_b64decode(
                self.base64_rsa_private_key)
            decoded_token = base64.urlsafe_b64decode(token)

            """
            Decrypt OAEP dengan SHA-1,
            dalam bentuk bytes, perlu di decode ke string
            """
            key = RSA.importKey(decoded_private_key)
            cipher = PKCS1_OAEP.new(key)
            message = cipher.decrypt(decoded_token)

            """
            Hasil dikembalikan dalam bentuk SSOResult
            menggunakan looping ke dalam atribut
            """
            jsonParsed = json.loads(message.decode('utf-8'))
            result.valid = True
            for key, value in jsonParsed.items():
                setattr(result, result.mapping[key], value)

            return result

        except Exception as e:
            """
            Default return jika terjadi error
            agar tidak error di sisi client
            """
            print("Error Parse Token : {}".format(str(e)))
            for key, value in result.mapping.items():
                setattr(result, value, "")
            return result
