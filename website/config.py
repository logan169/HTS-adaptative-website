import os

class ConfigClass(object):
    # Flask settings
    DEBUG = os.getenv('DEBUG',      False )
    SECRET_KEY =              os.getenv('SECRET_KEY',       'm51ze181fsfzedplez15ze78')
    SECURITY_PASSWORD_SALT=os.getenv('SECURITY_PASSWORD_SALT', 'actga45zdnlqi453o545ziehqdnc464quycbi56qelncqi864lcqus')
    CSRF_ENABLED = True

    MAIL_SERVER =os.getenv('MAIL_SERVER',                    'smtp.googlemail.com'                                )
    MAIL_PORT =os.getenv('MAIL_PORT',                  465                                                        )
    MAIL_USE_TLS =os.getenv('MAIL_USE_TLS',                   False                                            )
    MAIL_USE_SSL =os.getenv('MAIL_USE_SSL',                   True                                                 )
    MAIL_DEBUG =os.getenv('MAIL_DEBUG',                     True                                                  )
    MAIL_DEFAULT_SENDER =os.getenv('MAIL_DEFAULT_SENDER',      'wellness.garden.website@gmail.com'                  ) #EDIT displayed when email sent
    MAIL_USERNAME =os.getenv('MAIL_USERNAME',                  'wellness.garden.website@gmail.com'                 ) #EDIT with your mail adress username
    MAIL_PASSWORD =os.getenv('MAIL_PASSWORD',                  'qsdfgh13'                                          ) #EDIT with your mail adress password
