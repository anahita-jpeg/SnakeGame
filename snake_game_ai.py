import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()
font = pygame.font.Font(None, 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

# RGB Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20
SPEED = 40

# Snake color options
SNAKE_COLORS = [
    (255, 255, 0),    # Yellow
    (0, 255, 0),      # Green
    (255, 165, 0),    # Orange
    (0, 191, 255),    # Blue
    (255, 105, 180),  # Pink
]

class SnakeGameAI:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake AI')
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.direction = Direction.RIGHT
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [
            self.head,
            Point(self.head.x - BLOCK_SIZE, self.head.y),
            Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)
        ]
        self.score = 0
        self.food = None
        self.frame_iteration = 0
        self.snake_color = random.choice(SNAKE_COLORS)
        self._place_food()

    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self, action):
        self.frame_iteration += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Save old distance before move
        old_dist = abs(self.head.x - self.food.x) + abs(self.head.y - self.food.y)

        self._move(action)
        self.snake.insert(0, self.head)

        reward = 0
        game_over = False

        # Collision or timeout
        if self._is_collision() or self.frame_iteration > 150 * len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score

        # Ate food
        if self.head == self.food:
            self.score += 1
            reward = 15
            self._place_food()
        else:
            self.snake.pop()

            # Distance-based reward shaping
            new_dist = abs(self.head.x - self.food.x) + abs(self.head.y - self.food.y)
            if new_dist < old_dist:
                reward = 0.2
            else:
                reward = -0.2

            # Mild time penalty to discourage idling
            reward -= 0.01

        self._update_ui()
        self.clock.tick(SPEED)
        return reward, game_over, self.score

    def _is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        if pt.x >= self.w or pt.x < 0 or pt.y >= self.h or pt.y < 0:
            return True
        if pt in self.snake[1:]:
            return True
        return False

    def _update_ui(self):
        self.display.fill(BLACK)

        for idx, pt in enumerate(self.snake):
            pygame.draw.rect(self.display, self.snake_color, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            if idx == 0:
                eye_radius = 2
                offset_x = 5
                offset_y = 5
                pygame.draw.circle(self.display, BLACK, (pt.x + offset_x, pt.y + offset_y), eye_radius)
                pygame.draw.circle(self.display, BLACK, (pt.x + BLOCK_SIZE - offset_x, pt.y + offset_y), eye_radius)

        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.display, (0, 255, 0), pygame.Rect(self.food.x + BLOCK_SIZE // 2 - 1, self.food.y - 4, 4, 4))

        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def _move(self, action):
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx]  # No change
        elif np.array_equal(action, [0, 1, 0]):
            new_dir = clock_wise[(idx + 1) % 4]  # Right turn
        else:
            new_dir = clock_wise[(idx - 1) % 4]  # Left turn

        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)
