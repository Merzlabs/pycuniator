
import base64
import hashlib
import os


#got code from https://github.com/openstack/deb-python-oauth2client/blob/master/oauth2client/_pkce.py
class PKCE:
    def __init__(self):
        bytes_verifier = self._generate_code_verifier()
        self.code_verifier: str = str(bytes_verifier)
        self.code_challenge: str = str(self._generate_code_challenge(bytes_verifier))

    def _generate_code_verifier(self, n_bytes=64):
        """
        Generates a 'code_verifier' as described in section 4.1 of RFC 7636.
        This is a 'high-entropy cryptographic random string' that will be
        impractical for an attacker to guess.
        Args:
            n_bytes: integer between 31 and 96, inclusive. default: 64
                number of bytes of entropy to include in verifier.
        Returns:
            Bytestring, representing urlsafe base64-encoded random data.
        """
        verifier = base64.urlsafe_b64encode(os.urandom(n_bytes)).rstrip(b'=')
        # https://tools.ietf.org/html/rfc7636#section-4.1
        # minimum length of 43 characters and a maximum length of 128 characters.
        if len(verifier) < 43:
            raise ValueError("Verifier too short. n_bytes must be > 30.")
        elif len(verifier) > 128:
            raise ValueError("Verifier too long. n_bytes must be < 97.")
        else:
            return verifier


    def _generate_code_challenge(self, verifier):
        """
        Creates a 'code_challenge' as described in section 4.2 of RFC 7636
        by taking the sha256 hash of the verifier and then urlsafe
        base64-encoding it.
        Args:
            verifier: bytestring, representing a code_verifier as generated by
                code_verifier().
        Returns:
            Bytestring, representing a urlsafe base64-encoded sha256 hash digest,
                without '=' padding.
        """
        digest = hashlib.sha256(verifier).digest()
        return base64.urlsafe_b64encode(digest).rstrip(b'=')



# old and retired
# def generate_code_challenge():
#     #TODO urandom cryptocraphically secure?
#     #https://www.stefaanlippens.net/oauth-code-flow-pkce.html
#     code_verifier = urlsafe_b64encode(urandom(40)).decode('utf-8')
#     code_verifier = re_sub('[^a-zA-Z0-9]+', '', code_verifier)
#     code_challenge = hash_sha256(code_verifier.encode('utf-8')).digest()
#     code_challenge = urlsafe_b64encode(code_challenge).decode('utf-8')
#     code_challenge = code_challenge.replace('=', '')
#     return code_challenge