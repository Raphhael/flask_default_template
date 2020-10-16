import logging


logging.basicConfig(
    # filename="instance/error.log",
    level=logging.INFO,
    format='%(levelname)s [%(asctime)s]\t%(module)s.%(funcName)s' + ' (ligne %(lineno)s) : %(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p',
)


class BaseConfig(object):
    # Default
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security
    SECURITY_PASSWORD_HASH = "argon2"
    PASSWORD_COMPLEXITY_CHECKER = "zxcvbn"
    SECURITY_USER_IDENTITY_ATTRIBUTES = ['username', 'email']

    # Secret related config
    CFG_FILE = "configuration.cfg"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    ENV = "dev"
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False


class StagingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    ENV = "staging"


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    ENV = "prod"
