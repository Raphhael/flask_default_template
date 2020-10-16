from flask_security.models import fsqla_v2 as fsqla
from flask_security import SQLAlchemyUserDatastore, hash_password
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String
from flask.cli import with_appcontext
import click

db = SQLAlchemy()

fsqla.FsModels.set_db_info(db)


class Role(db.Model, fsqla.FsRoleMixin):
    pass


class User(db.Model, fsqla.FsUserMixin):
    email = Column(String(255))
    username = Column(String(255), unique=True, nullable=False)

    blogs = db.relationship("Blog", backref="user", lazy="dynamic")
    pass


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    text = db.Column(db.UnicodeText)


user_datastore = SQLAlchemyUserDatastore(db, User, Role)


@click.command('init-db')
@with_appcontext
def init_db():
    # Init db
    db.drop_all()
    db.create_all()
    click.echo("db reinitialised")

    # Roles
    roles = [
        ("admin", {"rw_admin", "rw_user"}),
        ("user", {"rw_user"})
    ]
    for name, permissions in roles:
        user_datastore.create_role(name=name, permissions=permissions)
    print(len(roles), "roles créés")

    # Users
    users = [
        ("raphael", hash_password("azerty"), ["admin"]),
        ("test", hash_password("azerty"), ["user"])
    ]
    for username, pwd, roles in users:
        user_datastore.create_user(username=username, password=pwd, roles=roles)
    print(len(users), "utilisateurs créés")


def init_commands(app):
    app.cli.add_command(init_db)
