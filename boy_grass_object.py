from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

    def update(self): pass
class Boy:
    def __init__(self):
        self.x , self.y = random.randint(100, 700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class smallBallon():
    def __init__(self):
        self.x, self.y = random.randint(30,750), 90
        self.image = load_image('ball21x21.png')
        self.speed = random.randint(3, 5)
    def update(self):
        self.y += self.speed
        if(self.y > 550):
            self.y = 550
    def draw(self):
        self.image.draw(self.x, self.y)

class bigBallon():
    def __init__(self):
        self.x, self.y = random.randint(30,750), 90
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(3, 5)
    def update(self):
        self.y += self.speed
        if(self.y > 550):
            self.y = 550
    def draw(self):
        self.image.draw(self.x, self.y)

def reset_world():
    global world
    world = []

    # 땅 객체를 생성하고 WORLD LIST에 추가한다
    grass = Grass()
    world.append(grass)

    # 팀을 생성하고, WORLD list에 추가한다.
    team = [Boy() for i in range(11)]
    world += team

    smallballons = [smallBallon() for i in range(10)]
    world += smallballons

    bigballons = [bigBallon() for i in range(10)]
    world += bigballons

    global running
    running = True

    # 세계에 존재하는 객체들을 담는 word list를 만든다. 


def update_world():
    for o in world:
        o.update()

    

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

 


open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)


close_canvas()
