import urllib2, urllib
import json
from google.appengine.api import urlfetch

API_SSL_SERVER="https://www.google.com/recaptcha/api.js"
API_SERVER="http://www.google.com/recaptcha/api.js"
VERIFY_SERVER="www.google.com"

class RecaptchaResponse(object):
    def __init__(self, is_valid, error_code=None):
        self.is_valid = is_valid
        self.error_code = error_code

def displayhtml (public_key,
                 use_ssl = False,
                 error = None):
    """Gets the HTML to display for reCAPTCHA

    public_key -- The public api key
    use_ssl -- Should the request be sent over ssl?
    error -- An error message to display (from RecaptchaResponse.error_code)"""

    error_param = ''
    if error:
        error_param = '&error=%s' % error

    if use_ssl:
        server = API_SSL_SERVER
    else:
        server = API_SERVER

    return """<script src="%(ApiServer)s" async defer></script>

<div class="g-recaptcha" data-sitekey="%(PublicKey)s"></div>
""" % {
        'ApiServer' : server,
        'PublicKey' : public_key,
        }


def submit (recaptcha_response_field,
            private_key,
            remoteip):
    """
    Submits a reCAPTCHA request for verification. Returns RecaptchaResponse
    for the request

    recaptcha_response_field -- The value of recaptcha_response_field from the form
    private_key -- your reCAPTCHA private key
    remoteip -- the user's ip address
    """

    if not (recaptcha_response_field and len(recaptcha_response_field)):
        return RecaptchaResponse (is_valid = False, error_code = 'incorrect-captcha-sol')
    

    def encode_if_necessary(s):
        if isinstance(s, unicode):
            return s.encode('utf-8')
        return s

    params = urllib.urlencode ({
            'secret': encode_if_necessary(private_key),
            'response' : encode_if_necessary(recaptcha_response_field),
            'remoteip' : encode_if_necessary(remoteip),
            })

    httpresp = urlfetch.fetch (
        url = "https://%s/recaptcha/api/siteverify" % VERIFY_SERVER,
        payload = params,
        method = urlfetch.POST,
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "User-agent": "reCAPTCHA GAE Python"
            }
        )
    
    return_values = json.loads(httpresp.content)
    return_code = return_values['success']
    if (return_code == True and httpresp.status_code == 200):
        return RecaptchaResponse (is_valid=True)
    else:
        return RecaptchaResponse (is_valid=False, error_code = return_values['error-codes'])
