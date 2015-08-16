try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(name='recaptcha-appengine',
      version='1.0.2',
      url = "http://github.com/cwyark/recaptcha-appengine",
      author = "Cwyark",
      author_email = "cwyark@gmail.com",
      description = "A plugin for reCAPTCHA and reCAPTCHA Mailhide for Google App Engine",
      long_description = """\
Provides a CAPTCHA for Python using the reCAPTCHA service. Does not require
any imaging libraries because the CAPTCHA is served directly from reCAPTCHA.
Also allows you to securely obfuscate emails with Mailhide. This functionality
requires pycrypto. This library requires two types of API keys. If you'd like
to use the CAPTCHA, you'll need a key from https://www.google.com/recaptcha/admin/create.
For Mailhide, you'll need a key from http://www.google.com/recaptcha/mailhide/apikey.

The trunk can be checked out from
http://recaptcha.googlecode.com/svn/trunk/recaptcha-plugins/python,
and the associated Google Code project lives at
http://code.google.com/p/recaptcha. Note that this is a shared
project/repository for reCAPTCHA clients for several languages/environments.

There is also a Google Group at http://groups.google.com/group/recaptcha/.
Please use the associated mailing list for any questions or comments:
recaptcha@googlegroups.com. Like the Google Code project, the Google Group
mailing list is also shared among the several reCAPTCHA client implementations.

The reCAPTCHA module is licensed under an MIT/X11 license.
""",

      license = "MIT/X11",
      classifiers = [
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        ],


      packages = find_packages(),

      extras_require = {
        'mailhide' : ['pycrypto'],
        },
      namespace_packages = ['recaptcha'],
      )
