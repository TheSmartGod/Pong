from pygame import *

WIDTH, HEIGHT = 700,700
window = display.set_mode((WIDTH,HEIGHT))
clock = time.Clock()

class Rectangle(sprite.Sprite):
    def __init__(self, color, position, size):
        super().__init__()
        self.image = Surface(size)
        self.image.fill(color)
        self.rect = Rect(position, size)
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

class ImageSprite(sprite.Sprite):
    def __init__(self, filename, position, size):
        super().__init__()
        self.rect = Rect(position, size)
        self.image = image.load(filename)
        self.image = transform.scale(self.image, size)
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

class Player1(Rectangle):
    def __init__(self, color, position, size, velocity):
        super().__init__(color, position, size)
        self.vel = Vector2(velocity)
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.vel.y
        if keys[K_s]:
            self.rect.y += self.vel.y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Player2(Rectangle):
    def __init__(self, color, position, size, velocity):
        super().__init__(color, position, size)
        self.vel = Vector2(velocity)
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.vel.y
        if keys[K_DOWN]:
            self.rect.y += self.vel.y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Ball(Rectangle):
    def __init__(self, color, position, size, velocity):
        super().__init__(color, position, size)
        self.vel = Vector2(velocity)
    def update(self):
        self.rect.topleft += self.vel
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.vel.y *= -1

P1 = Player1("green",(50,HEIGHT/2),(20,150), 9)
P2 = Player2("green",(650,HEIGHT/2),(20,150), 9)
P1W = ImageSprite("P1.png", (0,0), size = (WIDTH,HEIGHT))
P2W = ImageSprite("p2.png", (0,0), size = (WIDTH,HEIGHT))
Ball_ = Ball("yellow", (WIDTH/2,HEIGHT/2), (30,30), (4,4))

while not event.peek(QUIT):
    window.fill("blue")
    P1.update()
    P1.draw(window)
    P2.update()
    P2.draw(window)
    Ball_.update()
    Ball_.draw(window)
    if sprite.collide_rect(P1, Ball_):
        Ball_.vel.x *= -1
    if sprite.collide_rect(P2, Ball_):
        Ball_.vel.x *= -1
    if Ball_.rect.right > WIDTH:
        P1W.draw(window)
    if Ball_.rect.left < 0:
        P2W.draw(window)
    display.update()
    clock.tick(60)