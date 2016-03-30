from app import db


class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True)
    upgrades = db.relationship('Upgrade', backref='hero', lazy='dynamic')

    @property
    def __repr__(self):
        return "Hero's name %r" % self.name


class Upgrade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))

    @property
    def __repr__(self):
        return "Next upgrade cost: %r" % self.cost
