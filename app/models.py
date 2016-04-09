from app import db


class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True)
    basecost = db.Column(db.String(10), index=True, unique=True)

    def __repr__(self):
        return "Hero's name %r" % self.name


class Upgrade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)
    cost = db.Column(db.String(20))
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))

    def __repr__(self):
        return "Next upgrade cost: %r" % self.cost
