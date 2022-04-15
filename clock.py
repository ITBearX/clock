#!/usr/bin/python

import pygame
import datetime
import math
from pygame.locals import RESIZABLE, QUIT, KEYDOWN, K_ESCAPE

DOUBLE_PI = math.pi * 2

FPS = 50

BG_COLOR = (0, 20, 20)
DIAL_COLOR = (0, 0, 200)
ARROW_COLOR = (0, 200, 0)

DIAL_SIZE = 0.8
HR_SIZE = 0.45
MIN_SIZE = 0.75
SEC_SIZE = 0.75


def get_screen_params(screen):
    (width, height) = (screen.get_width(), screen.get_height())
    return {
        "width": width,
        "height": height,
        "size": min(width, height),
        "center": (width // 2, height // 2)
    }


def draw_dial(screen, size_ratio, color=DIAL_COLOR):
    params = get_screen_params(screen)
    radius = int(size_ratio * params["size"]) // 2
    pygame.draw.circle(screen, color, params["center"], radius, 3)


def draw_arrow(
    screen, val, num_units, size_ratio,
    color=ARROW_COLOR, thickness=2
):
    params = get_screen_params(screen)
    alpha = val * DOUBLE_PI / num_units
    length = int(size_ratio * params["size"]) // 2
    end_coord = (
        params["center"][0] + int(length * math.sin(alpha)),
        params["center"][1] - int(length * math.cos(alpha))
    )
    pygame.draw.line(screen, color, params["center"], end_coord, thickness)


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((600, 400), RESIZABLE, 32)

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        screen.fill(BG_COLOR)
        draw_dial(screen, DIAL_SIZE, DIAL_COLOR)

        now = datetime.datetime.now()
        draw_arrow(screen, now.hour + now.minute/60, 12, HR_SIZE, thickness=5)
        draw_arrow(screen, now.minute, 60, MIN_SIZE, thickness=3)
        draw_arrow(screen, now.second, 60, SEC_SIZE, thickness=1)

        pygame.display.update()

    pygame.quit()
