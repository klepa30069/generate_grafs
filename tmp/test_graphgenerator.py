# This is first steps in creating beautiful editor for graph structures.
# Project now available on https://github.com/BrinzaBezrukoff/graphvisual

import pygame
import math
from abc import ABCMeta
from random import randint, random


A_ASCII = 65  # A ascii letter constant


def render_text(text, family, size, color=(0, 0, 0), aa=False):
    font = pygame.font.SysFont(family, size)
    return font.render(text, aa, color)


def near(p, center, radius):
    d2 = (p[0] - center[0])**2 + (p[1] - center[1])**2
    return d2 <= radius**2


class GraphObject (metaclass=ABCMeta):
    def draw(self, surface):
        pass

    def update(self):
        pass

    def get_event(self, ev):
        pass


class Vertex (GraphObject):
    def __init__(self, name, x, y, size=15, color=(0, 0, 0), width=1):
        self.__name, self.__name_surface = "", None
        self.set_name(name)
        self.x, self.y = x, y
        self.size, self.width, self.color = size, width, color
        self.__edges = []
        self.selected = False
        self.selection_color = (255, 0, 0)

    @property
    def edges(self):
        return self.__edges

    @property
    def name(self):
        return self.__name

    @property
    def pos(self):
        return self.x, self.y

    def set_name(self, name):
        self.__name = name
        self.__name_surface = render_text(name, "Arial", 16)

    def get_event(self, ev):
        if ev.type == pygame.MOUSEBUTTONDOWN and near(self.pos, ev.pos, self.size):
            self.select()
        elif ev.type == pygame.MOUSEMOTION and self.selected:
            self.x, self.y = ev.pos
        elif ev.type == pygame.MOUSEBUTTONUP and self.selected:
            self.deselect()

    def select(self, color=(255, 0, 0)):
        self.selected = True
        self.selection_color = color

    def deselect(self):
        self.selected = False

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.size, self.width)  # draw vertex circle
        if self.__name_surface:  # draw name
            x, y, w, h = self.__name_surface.get_rect()
            surface.blit(self.__name_surface, (self.x-w//2, self.y-h//2))
        if self.selected:  # draw selection
            pygame.draw.circle(surface, self.selection_color, self.pos, self.size-self.width)


class Edge (GraphObject):
    def __init__(self, v1, v2, weight=0, color=(0, 0, 0), width=1):
        self.v1, self.v2 = v1, v2
        self.__weight, self.__weight_surface = 0, None
        self.set_weight(weight)
        self.width, self.color = width, color

    @property
    def weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight
        self.__weight_surface = render_text(str(weight), "Arial", 16)

    @property
    def pos1(self):
        return self.v1.pos

    @property
    def pos2(self):
        return self.v2.pos

    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.pos1, self.pos2, self.width)  # draw edge line
        if self.__weight_surface:  # draw edge weight
            x1, y1 = self.pos1
            x2, y2 = self.pos2
            pos = (x2-x1)//2 + x1, (y2-y1)//2 + y1
            surface.blit(self.__weight_surface, pos)


class Graph:
    def __init__(self, matrix, verticies, edges):
        self.matrix = matrix
        self.verticies = verticies
        self.edges = edges
        self.objects = self.edges + self.verticies

    def __len__(self):
        return len(self.verticies)

    def draw(self, surface):
        [obj.draw(surface) for obj in self.objects]

    def update(self):
        [obj.update() for obj in self.objects]

    def get_event(self, ev):
        [obj.get_event(ev) for obj in self.objects]

    def set_width(self, width):
        [setattr(obj, "width", width) for obj in self.objects]

    @classmethod
    def random(cls, x, y, n, weights=(1, 10), radius=250, fill_factor=0.3, vsize=15, width=1, color=(0, 0, 0)):  # randomly generated Graph
        matrix = [[0]*n for _ in range(n)]
        verticies = []
        edges = []

        angle = 2 * math.pi / n
        for i in range(n):
            name = chr(A_ASCII + i % 33) * ((33 + i) // 33)
            vx, vy = radius*math.cos(angle*i)+x, radius*math.sin(angle*i)+y
            verticies.append(Vertex(name, int(vx), int(vy), vsize, color, width))

        for i in range(n-1):
            for j in range(i+1, n):
                if random() > fill_factor:
                    continue
                weight = randint(*weights)
                matrix[i][j] = matrix[j][i] = weight
                edges.append(Edge(verticies[i], verticies[j], weight, color, width))

        return cls(matrix, verticies, edges)


pygame.init()
SIZE = WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Graph visualizer")

g = Graph.random(300, 300, 8)


running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        g.get_event(ev)

    screen.fill((255, 255, 255))

    g.update()
    g.draw(screen)

    pygame.display.flip()


pygame.quit()