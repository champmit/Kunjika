#CSRF section
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
CSRF_SESSION_KEY="somethingimpossibletoguess"

#OpenID section

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

#Database section

DB_HOST = 'localhost'
DB_PORT = '8091'

#reCaptcha seaction

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6Lc-t-ASAAAAAB0YkGtdwfWS4lJio8-aCf4IM1II'
RECAPTCHA_PRIVATE_KEY = '6Lc-t-ASAAAAABjbkjOyZpnD1wZ4VEstwQUtQ3Pb'
RECAPTCHA_OPTIONS = {'theme': 'white'}

#Application configuration section

#Maximum comment length
MAX_COMMENT_LENGTH = 400
#Minimum comment length
MIN_COMMENT_LENGTH = 20

QUESTIONS_PER_PAGE = 20
TAGS_PER_PAGE = 40
USERS_PER_PAGE = 40
USER_QUESTIONS_PER_PAGE = 10
USER_ANSWERS_PER_PAGE = 10

ADMIN_EMAIL='shivshankar.dayal@gmail.com'