import pygame
from abc import ABC, abstractmethod
#ИСБ просто название несвязанное с проектом 
# Настройки окна
WIDTH = 800
HEIGHT = 600
FPS = 60

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (252, 15, 192)

class Shape(ABC):
    """Абстрактный класс формы."""
    def __init__(self, x, y, color=BLACK):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def draw(self, screen):
        pass

class Circle(Shape):
    """Круг"""
    def __init__(self, x, y, radius, color=BLACK):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class Square(Shape):
    """Квадрат"""
    def __init__(self, x, y, size, color=BLACK):
        super().__init__(x, y, color)
        self.size = size

    def draw(self, screen):
        rect = pygame.Rect(self.x - self.size // 2,
                           self.y - self.size // 2,
                           self.size,
                           self.size)
        pygame.draw.rect(screen, self.color, rect)

class Line(Shape):
    """Линия"""
    def __init__(self, start_pos=(0,0), end_pos=(0,0), width=1, color=BLACK):
        super().__init__(start_pos[0], start_pos[1], color)
        self.end_x = end_pos[0]
        self.end_y = end_pos[1]
        self.width = width

    def draw(self, screen):
        pygame.draw.line(screen,
                         self.color,
                         (self.x, self.y),
                         (self.end_x, self.end_y),
                         self.width)

def main():
    # Инициализация Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH , HEIGHT))
    clock = pygame.time.Clock()

    # Создаем фигуры по вашему описанию:

    # Чёрный квадрат в левом верхнем углу
    top_left_square = Square(50 + 35 , 50 + 35 ,70 , BLACK)

    # Розовый квадрат в правом нижнем углу
    bottom_right_square = Square(WIDTH -50 -35 , HEIGHT -50 -35 ,70 , PINK)

    # Синий круг справа сверху
    top_right_circle = Circle(WIDTH -50 -50 ,50 +50 ,50 , BLUE)

    # Жёлтый круг слева снизу
    bottom_left_circle= Circle(50 +50 , HEIGHT -50 -50 ,50 , YELLOW)

    arrow_line1 = Line(
        start_pos=(top_left_square.x , top_left_square.y),
        end_pos=(bottom_right_square.x , bottom_right_square.y),
        width=3,
        color=GREEN
    )

    arrow_line2= Line(
        start_pos=(top_right_circle.x , top_right_circle.y),
        end_pos=(bottom_left_circle.x , bottom_left_circle.y),
        width=3,
        color=RED
    )

    shapes=[
        top_left_square,
        bottom_right_square,
        top_right_circle,
        bottom_left_circle,
        arrow_line1,
        arrow_line2
    ]

    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        screen.fill(WHITE)

        for shape in shapes:
            shape.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__=="__main__":
    main()