WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

""" WTF_CSRF_ENABLED activates cross-site request forgery
prevention - true makes it more secure;
SECRET_KEY is only needed when CSRF is enabled;
used to create cryptographic token that is used to validate a form
"""