from flask import render_template, request, redirect, session
from app import app, models, db


@app.route('/')
@app.route('/index')
def index():
    heroes = models.Hero.query.order_by(models.Hero.id).all()
    upgrades = models.Upgrade.query.order_by(models.Upgrade.id).all()

    skill_levels = [10, 25, 50, 100, 200, 400, 800, 1000, 1010, 1025, 1050, 1100, 1200, 1400, 1800, 2000]
    upgrades_list = []

    for upgrade in upgrades:
        hero = None
        for h in heroes:
            if h.id == upgrade.hero_id:
                hero = h

        prev = 1
        for lvl in skill_levels:
            if lvl == upgrade.level:
                break
            else:
                prev = lvl + 1

        cost = eval(upgrade.cost)
        for x in xrange(prev, upgrade.level + 1):
            if upgrade.level < 1000:
                if x != 1:
                    cost += eval(hero.basecost) * 1.075 ** x
                else:
                    cost += eval(hero.basecost)
            else:
                cost += eval(hero.basecost) * 10 * 1.075 ** x

        upgrades_list.append({'name': hero.name, 'level': upgrade.level, 'coins': str(cost)})

    return render_template('index.html',
                           title='Tap Titans Upgrade',
                           heroes=heroes,
                           upgrades=upgrades_list)


@app.route('/adminpanel')
def adminpanel():
    heroes = models.Hero.query.order_by(models.Hero.id).all()
    upgrades = models.Upgrade.query.order_by(models.Upgrade.id).all()
    prev_hero_choice = 1
    prev_skill_level = 10

    if session.has_key('data'):
        prev_hero_choice = session['data'][0]
        prev_skill_level = session['data'][1]

    return render_template('adminpanel.html',
                           title='Tap Titans Upgrade',
                           heroes=heroes,
                           upgrades=upgrades,
                           prev_hero_choice=prev_hero_choice,
                           prev_skill_level=prev_skill_level)


@app.route('/save_hero_cost', methods=['GET', 'POST'])
def save_hero_cost():
    upgrade = db.session.query(models.Upgrade).filter_by(level=request.form['skill_level'],
                                                         hero_id=request.form['hero_choice']).first()
    session['data'] = [request.form['hero_choice'], request.form['skill_level']]
    cost = 0
    if request.form['cost'] != "":
        cost += eval(request.form['cost'])

    if upgrade:
        upgrade.cost = str(cost)
    else:
        upgrade = models.Upgrade(level=request.form['skill_level'], cost=str(cost), hero_id=request.form['hero_choice'])

    db.session.add(upgrade)
    db.session.commit()

    return redirect('/adminpanel')


@app.route('/generate_updates')
def generate_updates():
    upgrades = [
        {
            "hero_id": 1,  # Takeda
            "level": 10,
            "cost": 515
        },
        {
            "hero_id": 1,  # Takeda
            "level": 25,
            "cost": 1520
        },
        {
            "hero_id": 1,  # Takeda
            "level": 50,
            "cost": 9290
        },
        {
            "hero_id": 1,  # Takeda
            "level": 100,
            "cost": 354770
        },
        {
            "hero_id": 1,  # Takeda
            "level": 200,
            "cost": 478230000
        },
        {
            "hero_id": 1,  # Takeda
            "level": 400,
            "cost": 914810000000000
        },
        {
            "hero_id": 1,  # Takeda
            "level": 800,
            "cost": 3.34E+027
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1000,
            "cost": 1.28E+034
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1010,
            "cost": 1.318E+034
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1025,
            "cost": 3.905E+034
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1050,
            "cost": 2.3814E+035
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1100,
            "cost": 8.85E+036
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1200,
            "cost": 1.224E+040
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1400,
            "cost": 2.343E+046
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1800,
            "cost": 7.42E+057
        },
        {
            "hero_id": 1,  # Takeda
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 2,  # Contessa
            "level": 10,
            "cost": 1800
        },
        {
            "hero_id": 2,  # Contessa
            "level": 25,
            "cost": 5330
        },
        {
            "hero_id": 2,  # Contessa
            "level": 50,
            "cost": 32540
        },
        {
            "hero_id": 2,  # Contessa
            "level": 100,
            "cost": 1210000
        },
        {
            "hero_id": 2,  # Contessa
            "level": 200,
            "cost": 1670000000
        },
        {
            "hero_id": 2,  # Contessa
            "level": 400,
            "cost": 3.2E+015
        },
        {
            "hero_id": 2,  # Contessa
            "level": 800,
            "cost": 1.171E+028
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1000,
            "cost": 4.482E+034
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1010,
            "cost": 4.619E+034
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1025,
            "cost": 1.3668E+035
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1050,
            "cost": 8.3351E+035
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1100,
            "cost": 3.099E+037
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1200,
            "cost": 4.287E+040
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1400,
            "cost": 8.201E+046
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1800,
            "cost": 2.597E+058
        },
        {
            "hero_id": 2,  # Contessa
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 10,
            "cost": 6940
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 25,
            "cost": 20540
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 50,
            "cost": 125280
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 100,
            "cost": 4650000
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 200,
            "cost": 6440000000
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 400,
            "cost": 1.232E+016
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 800,
            "cost": 4.51E+028
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1000,
            "cost": 1.7257E+035
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1010,
            "cost": 1.7784E+035
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1025,
            "cost": 5.2621E+035
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1050,
            "cost": 3.2E+036
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1100,
            "cost": 1.1934E+038
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1200,
            "cost": 1.6506E+041
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1400,
            "cost": 3.1575E+047
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1800,
            "cost": 1.0001E+059
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 4,  # Mila
            "level": 10,
            "cost": 29360
        },
        {
            "hero_id": 4,  # Mila
            "level": 25,
            "cost": 86900
        },
        {
            "hero_id": 4,  # Mila
            "level": 50,
            "cost": 529950
        },
        {
            "hero_id": 4,  # Mila
            "level": 100,
            "cost": 19700000
        },
        {
            "hero_id": 4,  # Mila
            "level": 200,
            "cost": 27250000000
        },
        {
            "hero_id": 4,  # Mila
            "level": 400,
            "cost": 5.214E+016
        },
        {
            "hero_id": 4,  # Mila
            "level": 800,
            "cost": 1.9081E+029
        },
        {
            "hero_id": 4,  # Mila
            "level": 1000,
            "cost": 7.3E+035
        },
        {
            "hero_id": 4,  # Mila
            "level": 1010,
            "cost": 7.5228E+035
        },
        {
            "hero_id": 4,  # Mila
            "level": 1025,
            "cost": 2.22E+036
        },
        {
            "hero_id": 4,  # Mila
            "level": 1050,
            "cost": 1.357E+037
        },
        {
            "hero_id": 4,  # Mila
            "level": 1100,
            "cost": 5.0483E+038
        },
        {
            "hero_id": 4,  # Mila
            "level": 1200,
            "cost": 6.9822E+041
        },
        {
            "hero_id": 4,  # Mila
            "level": 1400,
            "cost": 1.33E+048
        },
        {
            "hero_id": 4,  # Mila
            "level": 1800,
            "cost": 3.8328E+059
        },
        {
            "hero_id": 4,  # Mila
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 5,  # Terra
            "level": 10,
            "cost": 137050
        },
        {
            "hero_id": 5,  # Terra
            "level": 25,
            "cost": 405540
        },
        {
            "hero_id": 5,  # Terra
            "level": 50,
            "cost": 2470000
        },
        {
            "hero_id": 5,  # Terra
            "level": 100,
            "cost": 91970000
        },
        {
            "hero_id": 5,  # Terra
            "level": 200,
            "cost": 127200000000
        },
        {
            "hero_id": 5,  # Terra
            "level": 400,
            "cost": 2.4334E+017
        },
        {
            "hero_id": 5,  # Terra
            "level": 800,
            "cost": 8.9044E+029
        },
        {
            "hero_id": 5,  # Terra
            "level": 1000,
            "cost": 3.4E+036
        },
        {
            "hero_id": 5,  # Terra
            "level": 1010,
            "cost": 3.51E+036
        },
        {
            "hero_id": 5,  # Terra
            "level": 1025,
            "cost": 1.038E+037
        },
        {
            "hero_id": 5,  # Terra
            "level": 1050,
            "cost": 6.334E+037
        },
        {
            "hero_id": 5,  # Terra
            "level": 1100,
            "cost": 2.35E+039
        },
        {
            "hero_id": 5,  # Terra
            "level": 1200,
            "cost": 3.25E+042
        },
        {
            "hero_id": 5,  # Terra
            "level": 1400,
            "cost": 6.23E+048
        },
        {
            "hero_id": 5,  # Terra
            "level": 1800,
            "cost": 1.97E+060
        },
        {
            "hero_id": 5,  # Terra
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 10,
            "cost": 701780
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 25,
            "cost": 2070000
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 50,
            "cost": 12660000
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 100,
            "cost": 470940000
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 200,
            "cost": 651340000000
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 400,
            "cost": 1.24E+018
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 800,
            "cost": 4.55E+030
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1000,
            "cost": 1.744E+037
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1010,
            "cost": 1.797E+037
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1025,
            "cost": 5.318E+037
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1050,
            "cost": 3.2435E+038
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1100,
            "cost": 1.206E+040
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1200,
            "cost": 1.668E+043
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1400,
            "cost": 3.191E+049
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1800,
            "cost": 1.01E+061
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 10,
            "cost": 3950000
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 25,
            "cost": 11700000
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 50,
            "cost": 71400000
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 100,
            "cost": 2650000000
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 200,
            "cost": 3670000000000
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 400,
            "cost": 7.02E+018
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 800,
            "cost": 2.57E+031
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1000,
            "cost": 9.835E+037
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1010,
            "cost": 1.0136E+038
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1025,
            "cost": 2.9991E+038
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1050,
            "cost": 1.82E+039
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1100,
            "cost": 6.801E+040
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1200,
            "cost": 9.407E+043
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1400,
            "cost": 1.7996E+050
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1800,
            "cost": 5.698E+061
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 10,
            "cost": 24520000
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 25,
            "cost": 72570000
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 50,
            "cost": 442550000
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 100,
            "cost": 16450000000
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 200,
            "cost": 22760000000000
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 400,
            "cost": 4.354E+019
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 800,
            "cost": 1.5934E+032
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1000,
            "cost": 6.0962E+038
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1010,
            "cost": 6.2822E+038
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1025,
            "cost": 1.85E+039
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1050,
            "cost": 1.133E+040
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1100,
            "cost": 4.2157E+041
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1200,
            "cost": 5.8307E+044
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1400,
            "cost": 1.11E+051
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1800,
            "cost": 3.5316E+062
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 9,  # Jukka #Jukka
            "level": 10,
            "cost": 245260000
        },
        {
            "hero_id": 9,  # Jukka #Jukka
            "level": 25,
            "cost": 725700000
        },
        {
            "hero_id": 9,  # Jukka #Jukka
            "level": 50,
            "cost": 4420000000
        },
        {
            "hero_id": 9,  # Jukka #Jukka
            "level": 100,
            "cost": 164580000000
        },
        {
            "hero_id": 9,  # Jukka #Jukka
            "level": 200,
            "cost": 227630000000000
        },
        {
            "hero_id": 9,  # Jukka #Jukka
            "level": 400,
            "cost": 4.3545E+020
        },
        {
            "hero_id": 9,  # Jukka
            "level": 800,
            "cost": 1.59E+033
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1000,
            "cost": 6.09E+039
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1010,
            "cost": 6.28E+039
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1025,
            "cost": 1.858E+040
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1050,
            "cost": 1.1335E+041
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1100,
            "cost": 4.21E+042
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1200,
            "cost": 5.83E+045
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1400,
            "cost": 1.115E+052
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1800,
            "cost": 3.53E+063
        },
        {
            "hero_id": 9,  # Jukka
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 10,  # Milo
            "level": 10,
            "cost": 1470000000
        },
        {
            "hero_id": 10,  # Milo
            "level": 25,
            "cost": 4360000000
        },
        {
            "hero_id": 10,  # Milo
            "level": 50,
            "cost": 26590000000
        },
        {
            "hero_id": 10,  # Milo
            "level": 100,
            "cost": 988900000000
        },
        {
            "hero_id": 10,  # Milo
            "level": 200,
            "cost": 1.36E+015
        },
        {
            "hero_id": 10,  # Milo
            "level": 400,
            "cost": 2.61E+021
        },
        {
            "hero_id": 10,  # Milo
            "level": 800,
            "cost": 9.57E+033
        },
        {
            "hero_id": 10,  # Milo
            "level": 1000,
            "cost": 3.662E+040
        },
        {
            "hero_id": 10,  # Milo
            "level": 1010,
            "cost": 3.774E+040
        },
        {
            "hero_id": 10,  # Milo
            "level": 1025,
            "cost": 1.1168E+041
        },
        {
            "hero_id": 10,  # Milo
            "level": 1050,
            "cost": 6.811E+041
        },
        {
            "hero_id": 10,  # Milo
            "level": 1100,
            "cost": 2.533E+043
        },
        {
            "hero_id": 10,  # Milo
            "level": 1200,
            "cost": 3.503E+046
        },
        {
            "hero_id": 10,  # Milo
            "level": 1400,
            "cost": 6.701E+052
        },
        {
            "hero_id": 10,  # Milo
            "level": 1800,
            "cost": 2.122E+064
        },
        {
            "hero_id": 10,  # Milo
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 11,  # Macelord
            "level": 10,
            "cost": 9710000000
        },
        {
            "hero_id": 11,  # Macelord
            "level": 25,
            "cost": 28750000000
        },
        {
            "hero_id": 11,  # Macelord
            "level": 50,
            "cost": 175350000000
        },
        {
            "hero_id": 11,  # Macelord
            "level": 100,
            "cost": 6520000000000
        },
        {
            "hero_id": 11,  # Macelord
            "level": 200,
            "cost": 9.01E+015
        },
        {
            "hero_id": 11,  # Macelord
            "level": 400,
            "cost": 1.725E+022
        },
        {
            "hero_id": 11,  # Macelord
            "level": 800,
            "cost": 6.313E+034
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1000,
            "cost": 2.4154E+041
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1010,
            "cost": 2.4891E+041
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1025,
            "cost": 7.365E+041
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1050,
            "cost": 4.49E+042
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1100,
            "cost": 1.6703E+044
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1200,
            "cost": 2.3102E+047
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1400,
            "cost": 4.4193E+053
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1800,
            "cost": 1.3993E+065
        },
        {
            "hero_id": 11,  # Macelord
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 10,
            "cost": 70480000000
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 25,
            "cost": 208560000000
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 50,
            "cost": 1270000000000
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 100,
            "cost": 47300000000000
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 200,
            "cost": 6.542E+016
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 400,
            "cost": 1.2514E+023
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 800,
            "cost": 4.5794E+035
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1000,
            "cost": 1.75E+042
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1010,
            "cost": 1.8E+042
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1025,
            "cost": 5.34E+042
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1050,
            "cost": 3.257E+043
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1100,
            "cost": 1.21E+045
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1200,
            "cost": 1.67E+048
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1400,
            "cost": 3.2E+054
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1800,
            "cost": 1.01E+066
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 10,
            "cost": 563690000000
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 25,
            "cost": 1660000000000
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 50,
            "cost": 10170000000000
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 100,
            "cost": 378270000000000
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 200,
            "cost": 5.2318E+017
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 400,
            "cost": 1E+024
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 800,
            "cost": 3.66E+036
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1000,
            "cost": 1.401E+043
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1010,
            "cost": 1.443E+043
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1025,
            "cost": 4.272E+043
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1050,
            "cost": 2.6053E+044
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1100,
            "cost": 9.68E+045
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1200,
            "cost": 1.34E+049
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1400,
            "cost": 2.563E+055
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1800,
            "cost": 8.12E+066
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 10,
            "cost": 8450000000000
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 25,
            "cost": 25000000000000
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 50,
            "cost": 152470000000000
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 100,
            "cost": 5.67E+015
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 200,
            "cost": 7.84E+018
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 400,
            "cost": 1.5E+025
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 800,
            "cost": 5.489E+037
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1000,
            "cost": 2.1003E+044
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1010,
            "cost": 2.1644E+044
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1025,
            "cost": 6.4044E+044
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1050,
            "cost": 3.9E+045
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1100,
            "cost": 1.4525E+047
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1200,
            "cost": 2.0089E+050
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1400,
            "cost": 3.8429E+056
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1800,
            "cost": 1.2168E+068
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 15,  # Elpha
            "level": 10,
            "cost": 84500000000000
        },
        {
            "hero_id": 15,  # Elpha
            "level": 25,
            "cost": 250030000000000
        },
        {
            "hero_id": 15,  # Elpha
            "level": 50,
            "cost": 1.52E+015
        },
        {
            "hero_id": 15,  # Elpha
            "level": 100,
            "cost": 5.67E+016
        },
        {
            "hero_id": 15,  # Elpha
            "level": 200,
            "cost": 7.842E+019
        },
        {
            "hero_id": 15,  # Elpha
            "level": 400,
            "cost": 1.5003E+026
        },
        {
            "hero_id": 15,  # Elpha
            "level": 800,
            "cost": 5.4899E+038
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1000,
            "cost": 2.1E+045
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1010,
            "cost": 2.16E+045
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1025,
            "cost": 6.4E+045
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1050,
            "cost": 3.905E+046
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1100,
            "cost": 1.45E+048
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1200,
            "cost": 2E+051
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1400,
            "cost": 3.3252E+056
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1800,
            "cost": 1.22E+069
        },
        {
            "hero_id": 15,  # Elpha
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 16,  # Poppy
            "level": 10,
            "cost": 1.69E+015
        },
        {
            "hero_id": 16,  # Poppy
            "level": 25,
            "cost": 5E+015
        },
        {
            "hero_id": 16,  # Poppy
            "level": 50,
            "cost": 3.049E+016
        },
        {
            "hero_id": 16,  # Poppy
            "level": 100,
            "cost": 1.13E+018
        },
        {
            "hero_id": 16,  # Poppy
            "level": 200,
            "cost": 1.56E+021
        },
        {
            "hero_id": 16,  # Poppy
            "level": 400,
            "cost": 3E+027
        },
        {
            "hero_id": 16,  # Poppy
            "level": 800,
            "cost": 1.098E+040
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1000,
            "cost": 4.2E+046
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1010,
            "cost": 4.328E+046
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1025,
            "cost": 1.2808E+047
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1050,
            "cost": 7.8112E+045
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1100,
            "cost": 2.905E+049
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1200,
            "cost": 4.017E+052
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1400,
            "cost": 6.65E+057
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1800,
            "cost": 2.434E+070
        },
        {
            "hero_id": 16,  # Poppy
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 10,
            "cost": 1.69E+016
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 25,
            "cost": 5E+016
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 50,
            "cost": 3.0495E+017
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 100,
            "cost": 1.134E+019
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 200,
            "cost": 1.568E+022
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 400,
            "cost": 3E+028
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 800,
            "cost": 1.098E+041
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1000,
            "cost": 4.2007E+047
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1010,
            "cost": 4.3289E+047
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1025,
            "cost": 1.28E+048
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1050,
            "cost": 7.81E+048
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1100,
            "cost": 2.905E+050
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1200,
            "cost": 4.0178E+053
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1400,
            "cost": 6.65E+058
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1800,
            "cost": 2.4335E+071
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 10,
            "cost": 5.0701E+017
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 25,
            "cost": 1.5E+018
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 50,
            "cost": 9.14E+018
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 100,
            "cost": 3.4023E+020
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 200,
            "cost": 4.7057E+023
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 400,
            "cost": 9.0017E+029
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 800,
            "cost": 3.29E+042
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1000,
            "cost": 1.26E+049
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1010,
            "cost": 1.298E+049
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1025,
            "cost": 3.842E+049
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1050,
            "cost": 2.3433E+050
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1100,
            "cost": 8.71E+051
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1200,
            "cost": 1.205E+055
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1400,
            "cost": 6.65E+058
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1800,
            "cost": 2.4335E+071
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 19,  # Orba
            "level": 10,
            "cost": 2.535E+019
        },
        {
            "hero_id": 19,  # Orba
            "level": 25,
            "cost": 7.5E+019
        },
        {
            "hero_id": 19,  # Orba
            "level": 50,
            "cost": 4.5743E+020
        },
        {
            "hero_id": 19,  # Orba
            "level": 100,
            "cost": 1.701E+022
        },
        {
            "hero_id": 19,  # Orba
            "level": 200,
            "cost": 2.352E+025
        },
        {
            "hero_id": 19,  # Orba
            "level": 400,
            "cost": 4.5E+031
        },
        {
            "hero_id": 19,  # Orba
            "level": 800,
            "cost": 1.6469E+044
        },
        {
            "hero_id": 19,  # Orba
            "level": 1000,
            "cost": 6.3011E+050
        },
        {
            "hero_id": 19,  # Orba
            "level": 1010,
            "cost": 6.4934E+050
        },
        {
            "hero_id": 19,  # Orba
            "level": 1025,
            "cost": 1.92E+051
        },
        {
            "hero_id": 19,  # Orba
            "level": 1050,
            "cost": 1.171E+052
        },
        {
            "hero_id": 19,  # Orba
            "level": 1100,
            "cost": 4.3575E+053
        },
        {
            "hero_id": 19,  # Orba
            "level": 1200,
            "cost": 6.0267E+056
        },
        {
            "hero_id": 19,  # Orba
            "level": 1400,
            "cost": 9.976E+061
        },
        {
            "hero_id": 19,  # Orba
            "level": 1800,
            "cost": 3.6503E+074
        },
        {
            "hero_id": 19,  # Orba
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 20,  # Remus
            "level": 10,
            "cost": 7.6052E+020
        },
        {
            "hero_id": 20,  # Remus
            "level": 25,
            "cost": 2.25E+021
        },
        {
            "hero_id": 20,  # Remus
            "level": 50,
            "cost": 1.372E+022
        },
        {
            "hero_id": 20,  # Remus
            "level": 100,
            "cost": 5.1035E+023
        },
        {
            "hero_id": 20,  # Remus
            "level": 200,
            "cost": 7.0586E+026
        },
        {
            "hero_id": 20,  # Remus
            "level": 400,
            "cost": 1.35E+033
        },
        {
            "hero_id": 20,  # Remus
            "level": 800,
            "cost": 4.94E+045
        },
        {
            "hero_id": 20,  # Remus
            "level": 1000,
            "cost": 1.89E+052
        },
        {
            "hero_id": 20,  # Remus
            "level": 1010,
            "cost": 1.948E+052
        },
        {
            "hero_id": 20,  # Remus
            "level": 1025,
            "cost": 5.763E+052
        },
        {
            "hero_id": 20,  # Remus
            "level": 1050,
            "cost": 3.515E+053
        },
        {
            "hero_id": 20,  # Remus
            "level": 1100,
            "cost": 1.307E+055
        },
        {
            "hero_id": 20,  # Remus
            "level": 1200,
            "cost": 1.56E+057
        },
        {
            "hero_id": 20,  # Remus
            "level": 1400,
            "cost": 2.99E+063
        },
        {
            "hero_id": 20,  # Remus
            "level": 1800,
            "cost": 1.095E+076
        },
        {
            "hero_id": 20,  # Remus
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 21,  # Mickey
            "level": 10,
            "cost": 2.514E+022
        },
        {
            "hero_id": 21,  # Mickey
            "level": 25,
            "cost": 7.439E+022
        },
        {
            "hero_id": 21,  # Mickey
            "level": 50,
            "cost": 4.5371E+023
        },
        {
            "hero_id": 21,  # Mickey
            "level": 100,
            "cost": 1.687E+025
        },
        {
            "hero_id": 21,  # Mickey
            "level": 200,
            "cost": 2.333E+028
        },
        {
            "hero_id": 21,  # Mickey
            "level": 400,
            "cost": 4.464E+034
        },
        {
            "hero_id": 21,  # Mickey
            "level": 800,
            "cost": 1.6336E+047
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1000,
            "cost": 6.2499E+053
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1010,
            "cost": 6.4406E+053
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1025,
            "cost": 1.9E+054
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1050,
            "cost": 1.162E+055
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1100,
            "cost": 4.322E+056
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1200,
            "cost": 5.172E+058
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1400,
            "cost": 9.894E+064
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1800,
            "cost": 3.6206E+077
        },
        {
            "hero_id": 21,  # Mickey
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 22,  # Peter
            "level": 10,
            "cost": 2.51E+024
        },
        {
            "hero_id": 22,  # Peter
            "level": 25,
            "cost": 7.43E+024
        },
        {
            "hero_id": 22,  # Peter
            "level": 50,
            "cost": 4.537E+025
        },
        {
            "hero_id": 22,  # Peter
            "level": 100,
            "cost": 1.68E+027
        },
        {
            "hero_id": 22,  # Peter
            "level": 200,
            "cost": 2.33E+030
        },
        {
            "hero_id": 22,  # Peter
            "level": 400,
            "cost": 4.46E+036
        },
        {
            "hero_id": 22,  # Peter
            "level": 800,
            "cost": 1.633E+049
        },
        {
            "hero_id": 22,  # Peter
            "level": 1000,
            "cost": 6.249E+055
        },
        {
            "hero_id": 22,  # Peter
            "level": 1010,
            "cost": 6.44E+055
        },
        {
            "hero_id": 22,  # Peter
            "level": 1025,
            "cost": 1.9057E+056
        },
        {
            "hero_id": 22,  # Peter
            "level": 1050,
            "cost": 1.16E+057
        },
        {
            "hero_id": 22,  # Peter
            "level": 1100,
            "cost": 3.74E+057
        },
        {
            "hero_id": 22,  # Peter
            "level": 1200,
            "cost": 5.17E+060
        },
        {
            "hero_id": 22,  # Peter
            "level": 1400,
            "cost": 9.89E+066
        },
        {
            "hero_id": 22,  # Peter
            "level": 1800,
            "cost": 3.621E+079
        },
        {
            "hero_id": 22,  # Peter
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 23,  # Teeny
            "level": 10,
            "cost": 5.0186E+026
        },
        {
            "hero_id": 23,  # Teeny
            "level": 25,
            "cost": 1.48E+027
        },
        {
            "hero_id": 23,  # Teeny
            "level": 50,
            "cost": 9.05E+027
        },
        {
            "hero_id": 23,  # Teeny
            "level": 100,
            "cost": 4.6579E+032
        },
        {
            "hero_id": 23,  # Teeny
            "level": 200,
            "cost": 4.6579E+032
        },
        {
            "hero_id": 23,  # Teeny
            "level": 400,
            "cost": 8.9103E+038
        },
        {
            "hero_id": 23,  # Teeny
            "level": 800,
            "cost": 3.26E+051
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1000,
            "cost": 5.8E+057
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1010,
            "cost": 1.11E+057
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1025,
            "cost": 3.29E+057
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1050,
            "cost": 2.007E+058
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1100,
            "cost": 7.4644E+059
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1200,
            "cost": 1.03E+063
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1400,
            "cost": 1.97E+069
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1800,
            "cost": 7.23E+081
        },
        {
            "hero_id": 23,  # Teeny
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 24,  # Deznis
            "level": 10,
            "cost": 2.0095E+029
        },
        {
            "hero_id": 24,  # Deznis
            "level": 25,
            "cost": 5.9458E+029
        },
        {
            "hero_id": 24,  # Deznis
            "level": 50,
            "cost": 3.62E+030
        },
        {
            "hero_id": 24,  # Deznis
            "level": 100,
            "cost": 1.3485E+032
        },
        {
            "hero_id": 24,  # Deznis
            "level": 200,
            "cost": 1.8651E+035
        },
        {
            "hero_id": 24,  # Deznis
            "level": 400,
            "cost": 3.5677E+041
        },
        {
            "hero_id": 24,  # Deznis
            "level": 800,
            "cost": 1.3E+054
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1000,
            "cost": 2.32E+060
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1010,
            "cost": 4.4539E+059
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1025,
            "cost": 1.32E+060
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1050,
            "cost": 8.04E+060
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1100,
            "cost": 2.9888E+062
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1200,
            "cost": 4.1338E+065
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1400,
            "cost": 7.9075E+071
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1800,
            "cost": 2.89E+084
        },
        {
            "hero_id": 24,  # Deznis
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 10,
            "cost": 2.2053E+032
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 25,
            "cost": 6.5252E+032
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 50,
            "cost": 3.97E+033
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 100,
            "cost": 1.4799E+035
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 200,
            "cost": 2.0468E+038
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 400,
            "cost": 3.9154E+044
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 800,
            "cost": 1.43E+057
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1000,
            "cost": 2.55E+063
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1010,
            "cost": 4.8878E+062
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1025,
            "cost": 1.45E+063
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1050,
            "cost": 8.82E+063
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1100,
            "cost": 3.28E+065
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1200,
            "cost": 4.5365E+068
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1400,
            "cost": 8.6779E+074
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1800,
            "cost": 3.18E+087
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 26,  # Eistor
            "level": 10,
            "cost": 2.432E+037
        },
        {
            "hero_id": 26,  # Eistor
            "level": 25,
            "cost": 7.196E+037
        },
        {
            "hero_id": 26,  # Eistor
            "level": 50,
            "cost": 4.3884E+038
        },
        {
            "hero_id": 26,  # Eistor
            "level": 100,
            "cost": 1.632E+040
        },
        {
            "hero_id": 26,  # Eistor
            "level": 200,
            "cost": 2.257E+043
        },
        {
            "hero_id": 26,  # Eistor
            "level": 400,
            "cost": 4.317E+049
        },
        {
            "hero_id": 26,  # Eistor
            "level": 800,
            "cost": 1.4698E+062
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1000,
            "cost": 2.8115E+068
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1010,
            "cost": 5.39E+067
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1025,
            "cost": 1.5949E+068
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1050,
            "cost": 9.7264E+068
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1100,
            "cost": 3.617E+070
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1200,
            "cost": 5.003E+073
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1400,
            "cost": 9.57E+079
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1800,
            "cost": 3.5019E+092
        },
        {
            "hero_id": 26,  # Eistor
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 27,  # Flavius
            "level": 10,
            "cost": 2.669E+047
        },
        {
            "hero_id": 27,  # Flavius
            "level": 25,
            "cost": 7.8973E+047
        },
        {
            "hero_id": 27,  # Flavius
            "level": 50,
            "cost": 4.81E+048
        },
        {
            "hero_id": 27,  # Flavius
            "level": 100,
            "cost": 1.791E+050
        },
        {
            "hero_id": 27,  # Flavius
            "level": 200,
            "cost": 2.4772E+053
        },
        {
            "hero_id": 27,  # Flavius
            "level": 400,
            "cost": 4.4081E+059
        },
        {
            "hero_id": 27,  # Flavius
            "level": 800,
            "cost": 1.61E+072
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1000,
            "cost": 3.09E+078
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1010,
            "cost": 5.9156E+077
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1025,
            "cost": 1.75E+078
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1050,
            "cost": 1.067E+079
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1100,
            "cost": 3.9698E+080
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1200,
            "cost": 5.4905E+083
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1400,
            "cost": 1.05E+090
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1800,
            "cost": 3.84E+102
        },
        {
            "hero_id": 27,  # Flavius
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 28,  # Chester
            "level": 10,
            "cost": 2.7321E+062
        },
        {
            "hero_id": 28,  # Chester
            "level": 25,
            "cost": 8.0838E+062
        },
        {
            "hero_id": 28,  # Chester
            "level": 50,
            "cost": 4.93E+063
        },
        {
            "hero_id": 28,  # Chester
            "level": 100,
            "cost": 1.8334E+065
        },
        {
            "hero_id": 28,  # Chester
            "level": 200,
            "cost": 2.5357E+068
        },
        {
            "hero_id": 28,  # Chester
            "level": 400,
            "cost": 4.8506E+074
        },
        {
            "hero_id": 28,  # Chester
            "level": 800,
            "cost": 1.77E+087
        },
        {
            "hero_id": 28,  # Chester
            "level": 1000,
            "cost": 3.4E+093
        },
        {
            "hero_id": 28,  # Chester
            "level": 1010,
            "cost": 6.5095E+092
        },
        {
            "hero_id": 28,  # Chester
            "level": 1025,
            "cost": 1.93E+093
        },
        {
            "hero_id": 28,  # Chester
            "level": 1050,
            "cost": 1.175E+094
        },
        {
            "hero_id": 28,  # Chester
            "level": 1100,
            "cost": 4.3683E+095
        },
        {
            "hero_id": 28,  # Chester
            "level": 1200,
            "cost": 6.0416E+098
        },
        {
            "hero_id": 28,  # Chester
            "level": 1400,
            "cost": 1.16E+105
        },
        {
            "hero_id": 28,  # Chester
            "level": 1800,
            "cost": 4.23E+117
        },
        {
            "hero_id": 28,  # Chester
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 10,
            "cost": 3.01E+082
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 25,
            "cost": 8.906E+082
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 50,
            "cost": 5.4314E+083
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 100,
            "cost": 2.02E+085
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 200,
            "cost": 2.794E+088
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 400,
            "cost": 5.344E+094
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 800,
            "cost": 1.9555E+107
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 1000,
            "cost": 3.7407E+113
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 1010,
            "cost": 7.172E+112
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 1025,
            "cost": 2.1221E+113
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 1050,
            "cost": 1.29E+114
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 1100,
            "cost": 4.813E+115
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 1200,
            "cost": 6.656E+118
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 1400,
            "cost": 1.2733E+125
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 1800,
            "cost": 4.6593E+137
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 10,
            "cost": 3.01E+097
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 25,
            "cost": 8.906E+097
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 50,
            "cost": 5.4314E+098
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 100,
            "cost": 2.02E+100
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 200,
            "cost": 2.794E+103
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 400,
            "cost": 5.344E+109
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 800,
            "cost": 1.9555E+122
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 1000,
            "cost": 3.7407E+128
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 1010,
            "cost": 7.172E+127
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 1025,
            "cost": 2.1221E+128
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 1050,
            "cost": 1.29E+129
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 1100,
            "cost": 4.813E+130
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 1200,
            "cost": 6.656E+133
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 1400,
            "cost": 1.2733E+140
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 1800,
            "cost": 4.6593E+152
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 31,  # Pixie
            "level": 10,
            "cost": 3.6E+117
        },
        {
            "hero_id": 31,  # Pixie
            "level": 25,
            "cost": 1.067E+118
        },
        {
            "hero_id": 31,  # Pixie
            "level": 50,
            "cost": 6.504E+118
        },
        {
            "hero_id": 31,  # Pixie
            "level": 100,
            "cost": 2.42E+120
        },
        {
            "hero_id": 31,  # Pixie
            "level": 200,
            "cost": 3.35E+123
        },
        {
            "hero_id": 31,  # Pixie
            "level": 400,
            "cost": 6.4E+129
        },
        {
            "hero_id": 31,  # Pixie
            "level": 800,
            "cost": 2.342E+142
        },
        {
            "hero_id": 31,  # Pixie
            "level": 1000,
            "cost": 4.479E+148
        },
        {
            "hero_id": 31,  # Pixie
            "level": 1010,
            "cost": 8.59E+147
        },
        {
            "hero_id": 31,  # Pixie
            "level": 1025,
            "cost": 2.5410708762168E+148
        },
        {
            "hero_id": 31,  # Pixie
            "level": 1050,
            "cost": 1.54963131831487E+149
        },
        {
            "hero_id": 31,  # Pixie
            "level": 1100,
            "cost": 5.76303951713719E+150
        },
        {
            "hero_id": 31,  # Pixie
            "level": 1200,
            "cost": 7.97072861605008E+153
        },
        {
            "hero_id": 31,  # Pixie
            "level": 1400,
            "cost": 1.52472272433684E+160
        },
        {
            "hero_id": 31,  # Pixie
            "level": 1800,
            "cost": 5.57925965537788E+172
        },
        {
            "hero_id": 31,  # Pixie
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 10,
            "cost": 3.9687E+137
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 25,
            "cost": 1.17E+138
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 50,
            "cost": 7.16E+138
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 100,
            "cost": 2.6632E+140
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 200,
            "cost": 3.6834E+143
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 400,
            "cost": 7.0461E+149
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 800,
            "cost": 2.58E+162
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 1000,
            "cost": 4.93E+168
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 1010,
            "cost": 9.4559E+167
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 1025,
            "cost": 2.79788123072808E+168
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 1050,
            "cost": 1.70624299410201E+169
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 1100,
            "cost": 6.34547436195425E+170
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 1200,
            "cost": 8.7762809761828E+173
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 1400,
            "cost": 1.67881704222195E+180
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 1800,
            "cost": 6.14312100352777E+192
        },
        {
            "hero_id": 32,  # Jackalope
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 10,
            "cost": 4.371E+157
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 25,
            "cost": 1.2934E+158
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 50,
            "cost": 7.8877E+158
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 100,
            "cost": 2.933E+160
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 200,
            "cost": 4.057E+163
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 400,
            "cost": 7.761E+169
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 800,
            "cost": 2.8399E+182
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 1000,
            "cost": 5.4324E+188
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 1010,
            "cost": 1.0415E+188
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 1025,
            "cost": 3.08172425413527E+188
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 1050,
            "cost": 1.87934010944569E+189
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 1100,
            "cost": 6.98921813780468E+190
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 1200,
            "cost": 9.66662832159265E+193
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 1400,
            "cost": 1.84913181462128E+200
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 1800,
            "cost": 6.7663361777987E+212
        },
        {
            "hero_id": 33,  # Dark Lord
            "level": 2000,
            "cost": 0
        }
    ]

    msg = ""
    hero_added_count = 0
    heroes = models.Hero.query.order_by(models.Hero.id).all()
    upgrades_db = models.Upgrade.query.order_by(models.Upgrade.id).all()
    for u in upgrades:
        upgrade = None
        for ul_db in upgrades_db:
            if u["level"] == ul_db.level and u["hero_id"] == ul_db.hero_id:
                upgrade = ul_db
                upgrade.cost = str(u["cost"])
                break

        if upgrade is None:
            upgrade = models.Upgrade(level=u["level"], cost=str(u["cost"]), hero_id=u["hero_id"])

        db.session.add(upgrade)
        hero_added_count += 1
        msg += "Added " + heroes[u["hero_id"] - 1].name + " for level " + str(u["level"]) + "(" + str(
            hero_added_count) + ") <br />"

    db.session.commit()
    return msg
