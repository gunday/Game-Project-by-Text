import dice
from time import sleep

won = 'You have won the fight!'
lost = 'You have lost the fight! GAME OVER'
wonr = 'You have won the round!'
lostr = 'You have lost the round!'
luckyh = 'You deal double damage!'
unluckyh = 'You only weakly hit your enemy!'
luckyd = 'You take half damage!'
unluckyd = 'You took extra damage!'
ehealth = 'Enemy stamina is now '
hhealth = 'Your stamina is now '
tie = 'You and your enemy trade blows without striking each other!'


def encounter():

    print 'Please enter your heroes stats:'

    hstam = int(raw_input('Stamina: '))
    hskill = int(raw_input('Skill: '))
    hluck = int(raw_input('Luck: '))

    print 'Please enter the enemies stats:'

    estam = int(raw_input('Stamina: '))
    eskill = int(raw_input('Skill: '))

    round(hstam, hskill, hluck, estam, eskill)


def h_e_rolls(hskill, eskill):

    total = []

    hroll = dice.roll('2d6')
    eroll = dice.roll('2d6')

    htotal = hroll[0] + hroll[1] + hskill
    etotal = eroll[0] + eroll[1] + eskill

    total.append(htotal)
    total.append(etotal)

    print total

    return total


def round(hstam, hskill, hluck, estam, eskill):

    total = h_e_rolls(hskill, eskill)

    if total[0] > total[1]:
        print wonr
        use_luck = raw_input('Feeling lucky?')
        if use_luck == 'yes':
            result = luck(hluck)
            hluck = hluck - 1
            if result == 'lucky':
                estam = estam - 4
                print luckyh
                print ehealth + str(estam)
            else:
                estam = estam -1
                print unluckyh
                print ehealth + str(estam)
        else:
            estam = estam - 2
            print ehealth + str(estam)

    elif total[0] == total[1]:
        print tie

    else:
        print lostr
        use_luck = raw_input('Feeling lucky?')
        if use_luck == 'yes':
            result = luck(hluck)
            hluck = hluck - 1
            if result == 'lucky':
                hstam = hstam - 1
                print luckyd
                print hhealth + str(hstam)
            else:
                hstam = hstam - 3
                print unluckyd
                print hhealth + str(hstam)
        else:
            hstam = hstam - 2
            print hhealth + str(hstam)

    check_life(hstam, hskill, hluck, estam, eskill)


def check_life(hstam, hskill, hluck, estam, eskill):
    print hluck
    if hstam and estam > 0:
        sleep(3)
        round(hstam, hskill, hluck, estam, eskill)

    elif estam <= 0:
        print won

    elif hstam <= 0:
        print lost


def luck(hluck):

    lroll = dice.roll('2d6')

    ltotal = lroll[0] + lroll[1]

    if ltotal <= hluck:
        return 'lucky'
    else:
        return 'unlucky'


if __name__ == '__main__':
    encounter()
