hp = 100
def shoot(somenumber):
    global hp
    damage = ' 16'
    print( 'You dealt damage of' + damage)
    return hp

def fly_left():
    print(" You moved left")

def fly_right():
    print(" You moved right")

def fly_forward():
    print(" You moved forward")

def game_over(name):
    print(" Game over" + name)
    name = ' Sofija'

if __name__ == '__main__':
    fly_left()
    fly_right()
    fly_forward()
    shoot(16)
    game_over(' Sofija')
