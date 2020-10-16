from setuptools import find_packages, setup

setup(
    name='app',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'Flask-SQLAlchemy',
        'pysqlite3-binary',
        'email_validator',
        'flask-security',
        'argon2_cffi',
        'Flask-WTF'
    ]
)
