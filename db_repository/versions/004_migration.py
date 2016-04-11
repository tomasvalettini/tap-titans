from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
hero = Table('hero', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=20)),
    Column('basecost', String(length=10)),
)

upgrade = Table('upgrade', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('level', Integer),
    Column('cost', Integer),
    Column('hero_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['hero'].create()
    post_meta.tables['upgrade'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['hero'].drop()
    post_meta.tables['upgrade'].drop()
