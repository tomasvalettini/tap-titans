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
    heroes = [
        {'name': 'Takeda', 'base': '5.00E+01'},
        {'name': 'Contessa', 'base': '1.75E+02'},
        {'name': 'Hornetta', 'base': '673.75'},
        {'name': 'Mila', 'base': '2853.33'},
        {'name': 'Terra', 'base': '1.33E+04'},
        {'name': 'Inquisireaux', 'base': '6.81E+04'},
        {'name': 'Charlotte', 'base': '3.84E+05'},
        {'name': 'Jordaan', 'base': '2.38E+06'},
        {'name': 'Jukka', 'base': '2.38E+07'},
        {'name': 'Milo', 'base': '1.43E+08'},
        {'name': 'Macelord', 'base': '9.43E+08'},
        {'name': 'Gertrude', 'base': '6.84E+09'},
        {'name': 'Twitterella', 'base': '5.47E+10'},
        {'name': 'Master Hawk', 'base': '8.20E+11'},
        {'name': 'Elpha', 'base': '8.20E+12'},
        {'name': 'Poppy', 'base': '1.64E+14'},
        {'name': 'Skulptor', 'base': '1.64E+15'},
        {'name': 'Sterling', 'base': '4.92E+16'},
        {'name': 'Orba', 'base': '2.46E+18'},
        {'name': 'Remus', 'base': '7.38E+19'},
        {'name': 'Mickey', 'base': '2.44E+21'},
        {'name': 'Peter', 'base': '2.44E+23'},
        {'name': 'Teeny', 'base': '4.87E+25'},
        {'name': 'Deznis', 'base': '1.95E+28'},
        {'name': 'Hamlette', 'base': '2.14E+31'},
        {'name': 'Eistor', 'base': '2.36E+36'},
        {'name': 'Flavius', 'base': '2.59E+46'},
        {'name': 'Chester', 'base': '2.85E+61'},
        {'name': 'Mohacas', 'base': '3.14E+81'},
        {'name': 'Jacqulin', 'base': '3.14E+96'},
        {'name': 'Pixie', 'base': '3.76E+116'},
        {'name': 'Jackalope', 'base': '4.14E+136'},
        {'name': 'Dark Lord', 'base': '4.56E+156'}
    ]

    upgrades = [
        {
            "hero_id": 1,  # Takeda
            "level": 10,
            "cost": 515
        },
        {
            "hero_id": 1,  # Takeda
            "level": 25,
            "cost": 1.52E+3
        },
        {
            "hero_id": 1,  # Takeda
            "level": 50,
            "cost": 9.29E+3
        },
        {
            "hero_id": 1,  # Takeda
            "level": 100,
            "cost": 345.77E+3
        },
        {
            "hero_id": 1,  # Takeda
            "level": 200,
            "cost": 478.23E+6
        },
        {
            "hero_id": 1,  # Takeda
            "level": 400,
            "cost": 914.81E+12
        },
        {
            "hero_id": 1,  # Takeda
            "level": 800,
            "cost": 3.34E+27
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1000,
            "cost": 1.28E+34
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1010,
            "cost": 1.318E+34
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1025,
            "cost": 3.905E+34
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1050,
            "cost": 2.3814E+35
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1100,
            "cost": 8.85E+36
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1200,
            "cost": 1.224E+40
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1400,
            "cost": 2.343E+46
        },
        {
            "hero_id": 1,  # Takeda
            "level": 1800,
            "cost": 7.42E+57
        },
        {
            "hero_id": 1,  # Takeda
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 2,  # Contessa
            "level": 10,
            "cost": 1.8E+3
        },
        {
            "hero_id": 2,  # Contessa
            "level": 25,
            "cost": 5.33E+3
        },
        {
            "hero_id": 2,  # Contessa
            "level": 50,
            "cost": 32.54E+3
        },
        {
            "hero_id": 2,  # Contessa
            "level": 100,
            "cost": 1.21E+6
        },
        {
            "hero_id": 2,  # Contessa
            "level": 200,
            "cost": 1.67E+9
        },
        {
            "hero_id": 2,  # Contessa
            "level": 400,
            "cost": 3.2E+15
        },
        {
            "hero_id": 2,  # Contessa
            "level": 800,
            "cost": 1.171E+28
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1000,
            "cost": 4.482E+34
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1010,
            "cost": 4.619E+34
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1025,
            "cost": 1.3668E+35
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1050,
            "cost": 8.3351E+35
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1100,
            "cost": 3.099E+37
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1200,
            "cost": 4.287E+40
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1400,
            "cost": 8.201E+46
        },
        {
            "hero_id": 2,  # Contessa
            "level": 1800,
            "cost": 2.597E+58
        },
        {
            "hero_id": 2,  # Contessa
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 10,
            "cost": 6.94E+3
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 25,
            "cost": 20.54E+3
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 50,
            "cost": 125.28E+3
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 100,
            "cost": 4.65E+6
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 200,
            "cost": 6.44E+9
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 400,
            "cost": 1.232E+16
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 800,
            "cost": 4.51E+28
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1000,
            "cost": 1.7257E+35
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1010,
            "cost": 1.7784E+35
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1025,
            "cost": 5.2621E+35
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1050,
            "cost": 3.2E+36
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1100,
            "cost": 1.1934E+38
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1200,
            "cost": 1.6506E+41
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1400,
            "cost": 3.1575E+47
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 1800,
            "cost": 1.0001E+59
        },
        {
            "hero_id": 3,  # Hornetta
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 4,  # Mila
            "level": 10,
            "cost": 29.36E+3
        },
        {
            "hero_id": 4,  # Mila
            "level": 25,
            "cost": 86.90E+3
        },
        {
            "hero_id": 4,  # Mila
            "level": 50,
            "cost": 529.95E+3
        },
        {
            "hero_id": 4,  # Mila
            "level": 100,
            "cost": 19.70E+6
        },
        {
            "hero_id": 4,  # Mila
            "level": 200,
            "cost": 27.25E+9
        },
        {
            "hero_id": 4,  # Mila
            "level": 400,
            "cost": 5.214E+16
        },
        {
            "hero_id": 4,  # Mila
            "level": 800,
            "cost": 1.9081E+29
        },
        {
            "hero_id": 4,  # Mila
            "level": 1000,
            "cost": 7.3E+35
        },
        {
            "hero_id": 4,  # Mila
            "level": 1010,
            "cost": 7.5228E+35
        },
        {
            "hero_id": 4,  # Mila
            "level": 1025,
            "cost": 2.22E+36
        },
        {
            "hero_id": 4,  # Mila
            "level": 1050,
            "cost": 1.357E+37
        },
        {
            "hero_id": 4,  # Mila
            "level": 1100,
            "cost": 5.0483E+38
        },
        {
            "hero_id": 4,  # Mila
            "level": 1200,
            "cost": 6.9822E+41
        },
        {
            "hero_id": 4,  # Mila
            "level": 1400,
            "cost": 1.33E+48
        },
        {
            "hero_id": 4,  # Mila
            "level": 1800,
            "cost": 3.8328E+59
        },
        {
            "hero_id": 4,  # Mila
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 5,  # Terra
            "level": 10,
            "cost": 137.05E+3
        },
        {
            "hero_id": 5,  # Terra
            "level": 25,
            "cost": 405.54E+3
        },
        {
            "hero_id": 5,  # Terra
            "level": 50,
            "cost": 2.47E+6
        },
        {
            "hero_id": 5,  # Terra
            "level": 100,
            "cost": 91.97E+6
        },
        {
            "hero_id": 5,  # Terra
            "level": 200,
            "cost": 127.20E+9
        },
        {
            "hero_id": 5,  # Terra
            "level": 400,
            "cost": 2.4334E+17
        },
        {
            "hero_id": 5,  # Terra
            "level": 800,
            "cost": 8.9044E+29
        },
        {
            "hero_id": 5,  # Terra
            "level": 1000,
            "cost": 3.4E+36
        },
        {
            "hero_id": 5,  # Terra
            "level": 1010,
            "cost": 3.51E+36
        },
        {
            "hero_id": 5,  # Terra
            "level": 1025,
            "cost": 1.038E+37
        },
        {
            "hero_id": 5,  # Terra
            "level": 1050,
            "cost": 6.334E+37
        },
        {
            "hero_id": 5,  # Terra
            "level": 1100,
            "cost": 2.35E+39
        },
        {
            "hero_id": 5,  # Terra
            "level": 1200,
            "cost": 3.25E+42
        },
        {
            "hero_id": 5,  # Terra
            "level": 1400,
            "cost": 6.23E+48
        },
        {
            "hero_id": 5,  # Terra
            "level": 1800,
            "cost": 1.97E+60
        },
        {
            "hero_id": 5,  # Terra
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 10,
            "cost": 701.78E+3
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 25,
            "cost": 2.07E+6
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 50,
            "cost": 12.66E+6
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 100,
            "cost": 470.94E+6
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 200,
            "cost": 651.34E+9
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 400,
            "cost": 1.24E+18
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 800,
            "cost": 4.55E+30
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1000,
            "cost": 1.744E+37
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1010,
            "cost": 1.797E+37
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1025,
            "cost": 5.318E+37
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1050,
            "cost": 3.2435E+38
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1100,
            "cost": 1.206E+40
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1200,
            "cost": 1.668E+43
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1400,
            "cost": 3.191E+49
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 1800,
            "cost": 1.01E+61
        },
        {
            "hero_id": 6,  # Inquisireaux
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 10,
            "cost": 3.95E+6
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 25,
            "cost": 11.70E+6
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 50,
            "cost": 71.40E+6
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 100,
            "cost": 2.65E+9
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 200,
            "cost": 3.67E+12
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 400,
            "cost": 7.02E+18
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 800,
            "cost": 2.57E+31
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1000,
            "cost": 9.835E+37
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1010,
            "cost": 1.0136E+38
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1025,
            "cost": 2.9991E+38
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1050,
            "cost": 1.82E+39
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1100,
            "cost": 6.801E+40
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1200,
            "cost": 9.407E+43
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1400,
            "cost": 1.7996E+50
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 1800,
            "cost": 5.698E+61
        },
        {
            "hero_id": 7,  # Charlotte
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 10,
            "cost": 24.52E+6
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 25,
            "cost": 72.57E+6
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 50,
            "cost": 442.55E+6
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 100,
            "cost": 16.45E+9
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 200,
            "cost": 22.76E+12
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 400,
            "cost": 4.354E+19
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 800,
            "cost": 1.5934E+32
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1000,
            "cost": 6.0962E+38
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1010,
            "cost": 6.2822E+38
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1025,
            "cost": 1.85E+39
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1050,
            "cost": 1.133E+40
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1100,
            "cost": 4.2157E+41
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1200,
            "cost": 5.8307E+44
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1400,
            "cost": 1.11E+51
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 1800,
            "cost": 3.5316E+62
        },
        {
            "hero_id": 8,  # Jordaan
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 9,  # Jukka
            "level": 10,
            "cost": 245.26E+6
        },
        {
            "hero_id": 9,  # Jukka
            "level": 25,
            "cost": 725.70E+6
        },
        {
            "hero_id": 9,  # Jukka
            "level": 50,
            "cost": 4.42E+9
        },
        {
            "hero_id": 9,  # Jukka
            "level": 100,
            "cost": 164.58E+9
        },
        {
            "hero_id": 9,  # Jukka
            "level": 200,
            "cost": 227.63E+12
        },
        {
            "hero_id": 9,  # Jukka
            "level": 400,
            "cost": 4.3545E+20
        },
        {
            "hero_id": 9,  # Jukka
            "level": 800,
            "cost": 1.59E+33
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1000,
            "cost": 6.09E+39
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1010,
            "cost": 6.28E+39
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1025,
            "cost": 1.858E+40
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1050,
            "cost": 1.1335E+41
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1100,
            "cost": 4.21E+42
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1200,
            "cost": 5.83E+45
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1400,
            "cost": 1.115E+52
        },
        {
            "hero_id": 9,  # Jukka
            "level": 1800,
            "cost": 3.53E+63
        },
        {
            "hero_id": 9,  # Jukka
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 10,  # Milo
            "level": 10,
            "cost": 1.47E+9
        },
        {
            "hero_id": 10,  # Milo
            "level": 25,
            "cost": 4.36E+9
        },
        {
            "hero_id": 10,  # Milo
            "level": 50,
            "cost": 26.59E+9
        },
        {
            "hero_id": 10,  # Milo
            "level": 100,
            "cost": 988.90E+9
        },
        {
            "hero_id": 10,  # Milo
            "level": 200,
            "cost": 1.36E+15
        },
        {
            "hero_id": 10,  # Milo
            "level": 400,
            "cost": 2.61E+21
        },
        {
            "hero_id": 10,  # Milo
            "level": 800,
            "cost": 9.57E+33
        },
        {
            "hero_id": 10,  # Milo
            "level": 1000,
            "cost": 3.662E+40
        },
        {
            "hero_id": 10,  # Milo
            "level": 1010,
            "cost": 3.774E+40
        },
        {
            "hero_id": 10,  # Milo
            "level": 1025,
            "cost": 1.1168E+41
        },
        {
            "hero_id": 10,  # Milo
            "level": 1050,
            "cost": 6.811E+41
        },
        {
            "hero_id": 10,  # Milo
            "level": 1100,
            "cost": 2.533E+43
        },
        {
            "hero_id": 10,  # Milo
            "level": 1200,
            "cost": 3.503E+46
        },
        {
            "hero_id": 10,  # Milo
            "level": 1400,
            "cost": 6.701E+52
        },
        {
            "hero_id": 10,  # Milo
            "level": 1800,
            "cost": 2.122E+64
        },
        {
            "hero_id": 10,  # Milo
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 11,  # Macelord
            "level": 10,
            "cost": 9.71E+9
        },
        {
            "hero_id": 11,  # Macelord
            "level": 25,
            "cost": 28.75E+9
        },
        {
            "hero_id": 11,  # Macelord
            "level": 50,
            "cost": 175.35E+9
        },
        {
            "hero_id": 11,  # Macelord
            "level": 100,
            "cost": 6.52E+12
        },
        {
            "hero_id": 11,  # Macelord
            "level": 200,
            "cost": 9.01E+15
        },
        {
            "hero_id": 11,  # Macelord
            "level": 400,
            "cost": 1.725E+22
        },
        {
            "hero_id": 11,  # Macelord
            "level": 800,
            "cost": 6.313E+34
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1000,
            "cost": 2.4154E+41
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1010,
            "cost": 2.4891E+41
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1025,
            "cost": 7.365E+41
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1050,
            "cost": 4.49E+42
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1100,
            "cost": 1.6703E+44
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1200,
            "cost": 2.3102E+47
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1400,
            "cost": 4.4193E+53
        },
        {
            "hero_id": 11,  # Macelord
            "level": 1800,
            "cost": 1.3993E+65
        },
        {
            "hero_id": 11,  # Macelord
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 10,
            "cost": 70.48E+9
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 25,
            "cost": 208.56E+9
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 50,
            "cost": 1.27E+12
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 100,
            "cost": 47.30E+12
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 200,
            "cost": 6.542E+16
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 400,
            "cost": 1.2514E+23
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 800,
            "cost": 4.5794E+35
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1000,
            "cost": 1.75E+42
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1010,
            "cost": 1.8E+42
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1025,
            "cost": 5.34E+42
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1050,
            "cost": 3.257E+43
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1100,
            "cost": 1.21E+45
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1200,
            "cost": 1.67E+48
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1400,
            "cost": 3.2E+54
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 1800,
            "cost": 1.01E+66
        },
        {
            "hero_id": 12,  # Gertrude
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 10,
            "cost": 563.69E+9
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 25,
            "cost": 1.66E+12
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 50,
            "cost": 10.17E+12
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 100,
            "cost": 378.27E+12
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 200,
            "cost": 5.2318E+17
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 400,
            "cost": 1E+24
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 800,
            "cost": 3.66E+36
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1000,
            "cost": 1.401E+43
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1010,
            "cost": 1.443E+43
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1025,
            "cost": 4.272E+43
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1050,
            "cost": 2.6053E+44
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1100,
            "cost": 9.68E+45
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1200,
            "cost": 1.34E+49
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1400,
            "cost": 2.563E+55
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 1800,
            "cost": 8.12E+66
        },
        {
            "hero_id": 13,  # Twitterella
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 10,
            "cost": 8.45E+12
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 25,
            "cost": 25.00E+12
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 50,
            "cost": 152.47E+12
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 100,
            "cost": 5.67E+15
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 200,
            "cost": 7.84E+18
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 400,
            "cost": 1.5E+25
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 800,
            "cost": 5.489E+37
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1000,
            "cost": 2.1003E+44
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1010,
            "cost": 2.1644E+44
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1025,
            "cost": 6.4044E+44
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1050,
            "cost": 3.9E+45
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1100,
            "cost": 1.4525E+47
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1200,
            "cost": 2.0089E+50
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1400,
            "cost": 3.8429E+56
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 1800,
            "cost": 1.2168E+68
        },
        {
            "hero_id": 14,  # Master Hawk
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 15,  # Elpha
            "level": 10,
            "cost": 84.50E+12
        },
        {
            "hero_id": 15,  # Elpha
            "level": 25,
            "cost": 250.03E+12
        },
        {
            "hero_id": 15,  # Elpha
            "level": 50,
            "cost": 1.52E+15
        },
        {
            "hero_id": 15,  # Elpha
            "level": 100,
            "cost": 5.67E+16
        },
        {
            "hero_id": 15,  # Elpha
            "level": 200,
            "cost": 7.842E+19
        },
        {
            "hero_id": 15,  # Elpha
            "level": 400,
            "cost": 1.5003E+26
        },
        {
            "hero_id": 15,  # Elpha
            "level": 800,
            "cost": 5.4899E+38
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1000,
            "cost": 2.1E+45
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1010,
            "cost": 2.16E+45
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1025,
            "cost": 6.4E+45
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1050,
            "cost": 3.905E+46
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1100,
            "cost": 1.45E+48
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1200,
            "cost": 2E+51
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1400,
            "cost": 3.3252E+56
        },
        {
            "hero_id": 15,  # Elpha
            "level": 1800,
            "cost": 1.22E+69
        },
        {
            "hero_id": 15,  # Elpha
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 16,  # Poppy
            "level": 10,
            "cost": 1.69E+15
        },
        {
            "hero_id": 16,  # Poppy
            "level": 25,
            "cost": 5E+15
        },
        {
            "hero_id": 16,  # Poppy
            "level": 50,
            "cost": 3.049E+16
        },
        {
            "hero_id": 16,  # Poppy
            "level": 100,
            "cost": 1.13E+18
        },
        {
            "hero_id": 16,  # Poppy
            "level": 200,
            "cost": 1.56E+21
        },
        {
            "hero_id": 16,  # Poppy
            "level": 400,
            "cost": 3E+27
        },
        {
            "hero_id": 16,  # Poppy
            "level": 800,
            "cost": 1.098E+40
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1000,
            "cost": 4.2E+46
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1010,
            "cost": 4.328E+46
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1025,
            "cost": 1.2808E+47
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1050,
            "cost": 7.8112E+45
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1100,
            "cost": 2.905E+49
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1200,
            "cost": 4.017E+52
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1400,
            "cost": 6.65E+57
        },
        {
            "hero_id": 16,  # Poppy
            "level": 1800,
            "cost": 2.434E+70
        },
        {
            "hero_id": 16,  # Poppy
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 10,
            "cost": 1.69E+16
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 25,
            "cost": 5E+16
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 50,
            "cost": 3.0495E+17
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 100,
            "cost": 1.134E+19
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 200,
            "cost": 1.568E+22
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 400,
            "cost": 3E+28
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 800,
            "cost": 1.098E+41
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1000,
            "cost": 4.2007E+47
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1010,
            "cost": 4.3289E+47
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1025,
            "cost": 1.28E+48
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1050,
            "cost": 7.81E+48
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1100,
            "cost": 2.905E+50
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1200,
            "cost": 4.0178E+53
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1400,
            "cost": 6.65E+58
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 1800,
            "cost": 2.4335E+71
        },
        {
            "hero_id": 17,  # Skulptor
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 10,
            "cost": 5.0701E+17
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 25,
            "cost": 1.5E+18
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 50,
            "cost": 9.14E+18
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 100,
            "cost": 3.4023E+20
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 200,
            "cost": 4.7057E+23
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 400,
            "cost": 9.0017E+29
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 800,
            "cost": 3.29E+42
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1000,
            "cost": 1.26E+49
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1010,
            "cost": 1.298E+49
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1025,
            "cost": 3.842E+49
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1050,
            "cost": 2.3433E+50
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1100,
            "cost": 8.71E+51
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1200,
            "cost": 1.205E+55
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1400,
            "cost": 6.65E+58
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 1800,
            "cost": 2.4335E+71
        },
        {
            "hero_id": 18,  # Skulptor
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 19,  # Orba
            "level": 10,
            "cost": 2.535E+19
        },
        {
            "hero_id": 19,  # Orba
            "level": 25,
            "cost": 7.5E+19
        },
        {
            "hero_id": 19,  # Orba
            "level": 50,
            "cost": 4.5743E+20
        },
        {
            "hero_id": 19,  # Orba
            "level": 100,
            "cost": 1.701E+22
        },
        {
            "hero_id": 19,  # Orba
            "level": 200,
            "cost": 2.352E+25
        },
        {
            "hero_id": 19,  # Orba
            "level": 400,
            "cost": 4.5E+31
        },
        {
            "hero_id": 19,  # Orba
            "level": 800,
            "cost": 1.6469E+44
        },
        {
            "hero_id": 19,  # Orba
            "level": 1000,
            "cost": 6.3011E+50
        },
        {
            "hero_id": 19,  # Orba
            "level": 1010,
            "cost": 6.4934E+50
        },
        {
            "hero_id": 19,  # Orba
            "level": 1025,
            "cost": 1.92E+51
        },
        {
            "hero_id": 19,  # Orba
            "level": 1050,
            "cost": 1.171E+52
        },
        {
            "hero_id": 19,  # Orba
            "level": 1100,
            "cost": 4.3575E+53
        },
        {
            "hero_id": 19,  # Orba
            "level": 1200,
            "cost": 6.0267E+56
        },
        {
            "hero_id": 19,  # Orba
            "level": 1400,
            "cost": 9.976E+61
        },
        {
            "hero_id": 19,  # Orba
            "level": 1800,
            "cost": 3.6503E+74
        },
        {
            "hero_id": 19,  # Orba
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 20,  # Remus
            "level": 10,
            "cost": 7.6052E+20
        },
        {
            "hero_id": 20,  # Remus
            "level": 25,
            "cost": 2.25E+21
        },
        {
            "hero_id": 20,  # Remus
            "level": 50,
            "cost": 1.372E+22
        },
        {
            "hero_id": 20,  # Remus
            "level": 100,
            "cost": 5.1035E+23
        },
        {
            "hero_id": 20,  # Remus
            "level": 200,
            "cost": 7.0586E+26
        },
        {
            "hero_id": 20,  # Remus
            "level": 400,
            "cost": 1.35E+33
        },
        {
            "hero_id": 20,  # Remus
            "level": 800,
            "cost": 4.94E+45
        },
        {
            "hero_id": 20,  # Remus
            "level": 1000,
            "cost": 1.89E+52
        },
        {
            "hero_id": 20,  # Remus
            "level": 1010,
            "cost": 1.948E+52
        },
        {
            "hero_id": 20,  # Remus
            "level": 1025,
            "cost": 5.763E+52
        },
        {
            "hero_id": 20,  # Remus
            "level": 1050,
            "cost": 3.515E+53
        },
        {
            "hero_id": 20,  # Remus
            "level": 1100,
            "cost": 1.307E+55
        },
        {
            "hero_id": 20,  # Remus
            "level": 1200,
            "cost": 1.56E+57
        },
        {
            "hero_id": 20,  # Remus
            "level": 1400,
            "cost": 2.99E+63
        },
        {
            "hero_id": 20,  # Remus
            "level": 1800,
            "cost": 1.095E+76
        },
        {
            "hero_id": 20,  # Remus
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 21,  # Mickey
            "level": 10,
            "cost": 2.514E+22
        },
        {
            "hero_id": 21,  # Mickey
            "level": 25,
            "cost": 7.439E+22
        },
        {
            "hero_id": 21,  # Mickey
            "level": 50,
            "cost": 4.5371E+23
        },
        {
            "hero_id": 21,  # Mickey
            "level": 100,
            "cost": 1.687E+25
        },
        {
            "hero_id": 21,  # Mickey
            "level": 200,
            "cost": 2.333E+28
        },
        {
            "hero_id": 21,  # Mickey
            "level": 400,
            "cost": 4.464E+34
        },
        {
            "hero_id": 21,  # Mickey
            "level": 800,
            "cost": 1.6336E+47
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1000,
            "cost": 6.2499E+53
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1010,
            "cost": 6.4406E+53
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1025,
            "cost": 1.9E+54
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1050,
            "cost": 1.162E+55
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1100,
            "cost": 4.322E+56
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1200,
            "cost": 5.172E+58
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1400,
            "cost": 9.894E+64
        },
        {
            "hero_id": 21,  # Mickey
            "level": 1800,
            "cost": 3.6206E+77
        },
        {
            "hero_id": 21,  # Mickey
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 22,  # Peter
            "level": 10,
            "cost": 2.51E+24
        },
        {
            "hero_id": 22,  # Peter
            "level": 25,
            "cost": 7.43E+24
        },
        {
            "hero_id": 22,  # Peter
            "level": 50,
            "cost": 4.537E+25
        },
        {
            "hero_id": 22,  # Peter
            "level": 100,
            "cost": 1.68E+27
        },
        {
            "hero_id": 22,  # Peter
            "level": 200,
            "cost": 2.33E+30
        },
        {
            "hero_id": 22,  # Peter
            "level": 400,
            "cost": 4.46E+36
        },
        {
            "hero_id": 22,  # Peter
            "level": 800,
            "cost": 1.633E+49
        },
        {
            "hero_id": 22,  # Peter
            "level": 1000,
            "cost": 6.249E+55
        },
        {
            "hero_id": 22,  # Peter
            "level": 1010,
            "cost": 6.44E+55
        },
        {
            "hero_id": 22,  # Peter
            "level": 1025,
            "cost": 1.9057E+56
        },
        {
            "hero_id": 22,  # Peter
            "level": 1050,
            "cost": 1.16E+57
        },
        {
            "hero_id": 22,  # Peter
            "level": 1100,
            "cost": 3.74E+57
        },
        {
            "hero_id": 22,  # Peter
            "level": 1200,
            "cost": 5.17E+60
        },
        {
            "hero_id": 22,  # Peter
            "level": 1400,
            "cost": 9.89E+66
        },
        {
            "hero_id": 22,  # Peter
            "level": 1800,
            "cost": 3.621E+79
        },
        {
            "hero_id": 22,  # Peter
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 23,  # Teeny
            "level": 10,
            "cost": 5.0186E+26
        },
        {
            "hero_id": 23,  # Teeny
            "level": 25,
            "cost": 1.48E+27
        },
        {
            "hero_id": 23,  # Teeny
            "level": 50,
            "cost": 9.05E+27
        },
        {
            "hero_id": 23,  # Teeny
            "level": 100,
            "cost": 4.6579E+32
        },
        {
            "hero_id": 23,  # Teeny
            "level": 200,
            "cost": 4.6579E+32
        },
        {
            "hero_id": 23,  # Teeny
            "level": 400,
            "cost": 8.9103E+38
        },
        {
            "hero_id": 23,  # Teeny
            "level": 800,
            "cost": 3.26E+51
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1000,
            "cost": 5.8E+57
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1010,
            "cost": 1.11E+57
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1025,
            "cost": 3.29E+57
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1050,
            "cost": 2.007E+58
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1100,
            "cost": 7.4644E+59
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1200,
            "cost": 1.03E+63
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1400,
            "cost": 1.97E+69
        },
        {
            "hero_id": 23,  # Teeny
            "level": 1800,
            "cost": 7.23E+81
        },
        {
            "hero_id": 23,  # Teeny
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 24,  # Deznis
            "level": 10,
            "cost": 2.0095E+29
        },
        {
            "hero_id": 24,  # Deznis
            "level": 25,
            "cost": 5.9458E+29
        },
        {
            "hero_id": 24,  # Deznis
            "level": 50,
            "cost": 3.62E+30
        },
        {
            "hero_id": 24,  # Deznis
            "level": 100,
            "cost": 1.3485E+32
        },
        {
            "hero_id": 24,  # Deznis
            "level": 200,
            "cost": 1.8651E+35
        },
        {
            "hero_id": 24,  # Deznis
            "level": 400,
            "cost": 3.5677E+41
        },
        {
            "hero_id": 24,  # Deznis
            "level": 800,
            "cost": 1.3E+54
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1000,
            "cost": 2.32E+60
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1010,
            "cost": 4.4539E+59
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1025,
            "cost": 1.32E+60
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1050,
            "cost": 8.04E+60
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1100,
            "cost": 2.9888E+62
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1200,
            "cost": 4.1338E+65
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1400,
            "cost": 7.9075E+71
        },
        {
            "hero_id": 24,  # Deznis
            "level": 1800,
            "cost": 2.89E+84
        },
        {
            "hero_id": 24,  # Deznis
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 10,
            "cost": 2.2053E+32
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 25,
            "cost": 6.5252E+32
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 50,
            "cost": 3.97E+33
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 100,
            "cost": 1.4799E+35
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 200,
            "cost": 2.0468E+38
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 400,
            "cost": 3.9154E+44
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 800,
            "cost": 1.43E+57
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1000,
            "cost": 2.55E+63
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1010,
            "cost": 4.8878E+62
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1025,
            "cost": 1.45E+63
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1050,
            "cost": 8.82E+63
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1100,
            "cost": 3.28E+65
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1200,
            "cost": 4.5365E+68
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1400,
            "cost": 8.6779E+74
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 1800,
            "cost": 3.18E+87
        },
        {
            "hero_id": 25,  # Hamlette
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 26,  # Eistor
            "level": 10,
            "cost": 2.432E+37
        },
        {
            "hero_id": 26,  # Eistor
            "level": 25,
            "cost": 7.196E+37
        },
        {
            "hero_id": 26,  # Eistor
            "level": 50,
            "cost": 4.3884E+38
        },
        {
            "hero_id": 26,  # Eistor
            "level": 100,
            "cost": 1.632E+40
        },
        {
            "hero_id": 26,  # Eistor
            "level": 200,
            "cost": 2.257E+43
        },
        {
            "hero_id": 26,  # Eistor
            "level": 400,
            "cost": 4.317E+49
        },
        {
            "hero_id": 26,  # Eistor
            "level": 800,
            "cost": 1.4698E+62
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1000,
            "cost": 2.8115E+68
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1010,
            "cost": 5.39E+67
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1025,
            "cost": 1.5949E+68
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1050,
            "cost": 9.7264E+68
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1100,
            "cost": 3.617E+70
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1200,
            "cost": 5.003E+73
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1400,
            "cost": 9.57E+79
        },
        {
            "hero_id": 26,  # Eistor
            "level": 1800,
            "cost": 3.5019E+92
        },
        {
            "hero_id": 26,  # Eistor
            "level": 2000,
            "cost": 0
        },
        {
            "hero_id": 27,  # Flavius
            "level": 10,
            "cost": 2.669E+47
        },
        {
            "hero_id": 27,  # Flavius
            "level": 25,
            "cost": 7.8973E+47
        },
        {
            "hero_id": 27,  # Flavius
            "level": 50,
            "cost": 4.81E+48
        },
        {
            "hero_id": 27,  # Flavius
            "level": 100,
            "cost": 1.791E+50
        },
        {
            "hero_id": 27,  # Flavius
            "level": 200,
            "cost": 2.4772E+53
        },
        {
            "hero_id": 27,  # Flavius
            "level": 400,
            "cost": 4.4081E+59
        },
        {
            "hero_id": 27,  # Flavius
            "level": 800,
            "cost": 1.61E+72
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1000,
            "cost": 3.09E+78
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1010,
            "cost": 5.9156E+77
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1025,
            "cost": 1.75E+78
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1050,
            "cost": 1.067E+79
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1100,
            "cost": 3.9698E+80
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1200,
            "cost": 5.4905E+83
        },
        {
            "hero_id": 27,  # Flavius
            "level": 1400,
            "cost": 1.05E+90
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
            "cost": 2.7321E+62
        },
        {
            "hero_id": 28,  # Chester
            "level": 25,
            "cost": 8.0838E+62
        },
        {
            "hero_id": 28,  # Chester
            "level": 50,
            "cost": 4.93E+63
        },
        {
            "hero_id": 28,  # Chester
            "level": 100,
            "cost": 1.8334E+65
        },
        {
            "hero_id": 28,  # Chester
            "level": 200,
            "cost": 2.5357E+68
        },
        {
            "hero_id": 28,  # Chester
            "level": 400,
            "cost": 4.8506E+74
        },
        {
            "hero_id": 28,  # Chester
            "level": 800,
            "cost": 1.77E+87
        },
        {
            "hero_id": 28,  # Chester
            "level": 1000,
            "cost": 3.4E+93
        },
        {
            "hero_id": 28,  # Chester
            "level": 1010,
            "cost": 6.5095E+92
        },
        {
            "hero_id": 28,  # Chester
            "level": 1025,
            "cost": 1.93E+93
        },
        {
            "hero_id": 28,  # Chester
            "level": 1050,
            "cost": 1.175E+94
        },
        {
            "hero_id": 28,  # Chester
            "level": 1100,
            "cost": 4.3683E+95
        },
        {
            "hero_id": 28,  # Chester
            "level": 1200,
            "cost": 6.0416E+98
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
            "cost": 3.01E+82
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 25,
            "cost": 8.906E+82
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 50,
            "cost": 5.4314E+83
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 100,
            "cost": 2.02E+85
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 200,
            "cost": 2.794E+88
        },
        {
            "hero_id": 29,  # Mohacas
            "level": 400,
            "cost": 5.344E+94
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
            "cost": 3.01E+97
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 25,
            "cost": 8.906E+97
        },
        {
            "hero_id": 30,  # Jacqulin
            "level": 50,
            "cost": 5.4314E+98
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
    heroes_db = models.Hero.query.order_by(models.Hero.id).all()
    upgrades_db = models.Upgrade.query.order_by(models.Upgrade.id).all()

    for h in heroes:
        hero = None
        for h_db in heroes_db:
            if h['name'] == h_db.name:
                hero = h_db
                hero.basecost = str(h['base'])
                break

        if hero is None:
            hero = models.Hero(name=h['name'], basecost=str(h['base']))

        db.session.add(hero)
        msg += "Added " + hero.name + "<br />"

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
        msg += "Added " + str(upgrade.hero_id) + " for level " + str(upgrade.level) + "(" + str(
            hero_added_count) + ") <br />"

    db.session.commit()
    return msg
