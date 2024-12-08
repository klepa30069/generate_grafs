from turtledemo.penrose import start

import networkx as nx
import numpy as np
import string
from generate_solver import Generate_Solver
import random
from collections import Counter

class Generate_Solver_Task1(Generate_Solver):
    def __init__(self, type_task) -> None:
        self.type_task = type_task
        self.points = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.num_letters = random.randint(6, 8)
        self.letters = self.random_letter()
        self.start_point, self.end_point = self.random_start_letter()
        self.matrix = None
        self.add_one = False
        self.Counts = None
        self.anser = None
        self.anser_type2 = None

    def random_letter(self): #Рандомайзер букв в матрице
        letters = random.sample(self.points, self.num_letters)  # Выбирает num_letters уникальных букв
        return dict(enumerate(letters))

    def random_start_letter(self): #Рандомайзер стартовых буковок
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        point1, point2 = random.sample(numbers[:self.num_letters], 2)
        return point1, point2

    def shuffle_adjacency_matrix(self, adjacency_matrix):
        """Перемешивает вершины в матрице смежности, используя NumPy."""
        adjacency_matrix = np.array(adjacency_matrix)
        num_nodes = len(adjacency_matrix)
        permutation = np.random.permutation(num_nodes)  # Случайная перестановка индексов
        shuffled_matrix = adjacency_matrix[:, permutation][permutation,:]  # Применяем перестановку к строкам и столбцам
        self.anser = [self.letters[i] for i in permutation]

        return shuffled_matrix

    def get_text_task(self) -> str:
        pass

    def generate_random_matrix_with_edges(self, num_nodes, num_edges):
        """Генерирует случайную матрицу смежности с заданным количеством ребер."""
        adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]
        edges_added = 0
        if self.type_task == 0:
            while edges_added < num_edges:
                row = random.randint(0, num_nodes - 1)
                col = random.randint(0, num_nodes - 1)
                if row != col and adjacency_matrix[row][col] == 0:
                    adjacency_matrix[row][col] = 1
                    adjacency_matrix[col][row] = 1  # Для неориентированного графа
                    edges_added += 1
        elif self.type_task != 0:
            while edges_added < num_edges:
                row = random.randint(0, num_nodes - 1)
                col = random.randint(0, num_nodes - 1)
                if row != col and adjacency_matrix[row][col] == 0:
                    rand_val = random.randint(10, 100)
                    adjacency_matrix[row][col] = rand_val
                    adjacency_matrix[col][row] = rand_val  # Для неориентированного графа
                    edges_added += 1
                    if row == self.start_point or row == self.end_point and col == self.start_point or col == self.end_point:
                        self.anser_type2 = rand_val
        if adjacency_matrix[self.start_point][self.end_point] == 0:
            if self.type_task == 0:
                adjacency_matrix[self.start_point][self.end_point] = 1
                adjacency_matrix[self.end_point][self.start_point] = 1
            elif self.type_task != 0:
                rand_val = random.randint(10, 100)
                adjacency_matrix[self.start_point][self.end_point] = rand_val
                adjacency_matrix[self.end_point][self.start_point] = rand_val
                self.anser_type2 = rand_val
        return adjacency_matrix

    def add_node_list(self, adjacency_matrix):
        """Добавляет узел в матрицу смежности, представленную списком списков."""
        for row in adjacency_matrix:
            row.append(0)
        num_nodes = len(adjacency_matrix)
        new_row = [0] * (num_nodes + 1)
        adjacency_matrix.append(new_row)
        random_val, empty = self.random_start_letter()
        if self.type_task == 0:
            adjacency_matrix[num_nodes][random_val] = 1
            adjacency_matrix[random_val][num_nodes] = 1
        elif self.type_task != 0:
            rand_val = random.randint(10, 100)
            adjacency_matrix[num_nodes][random_val] = rand_val
            adjacency_matrix[random_val][num_nodes] = rand_val
        return adjacency_matrix

    def add_counter(self, all_el: list):
        self.Counts = Counter(all_el)

    def check_rows(self, matrix: list[list[int]]):
        all_el = []
        result = False
        for el in range(6):
            sum = 0
            for deep_el in matrix[el]:
                sum += deep_el
            all_el.append(sum)
        self.add_counter(all_el)
        for count in self.Counts.values():
            if count == 1:
                result = True
        if result == False:
            matrix = self.add_node_list(matrix)
            self.add_one = True
            self.letters[self.num_letters] = "I"
        return matrix

    def get_matrix_task(self) -> list[list[int]]:
        num_nodes = self.num_letters
        num_edges = num_nodes + num_nodes/2
        adjacency_matrix = self.generate_random_matrix_with_edges(num_nodes, num_edges)
        self.check_rows(adjacency_matrix)
        self.matrix = adjacency_matrix
        self.TaskMatrix = self.shuffle_adjacency_matrix(adjacency_matrix)
        return self.TaskMatrix

    def get_solving_task(self, type_task: int) -> str:
        num_nodes = len(self.matrix)
        iterations = 0
        anser = f'Ответ: '
        startP = 0
        endP = 0
        if type_task != 2:
            for i in range(num_nodes):
                iterations += 1
                anser += "Вершина {} = П{}. ".format(self.anser[i], iterations)
        else:
            start_letter = self.letters[self.start_point]
            end_letter = self.letters[self.end_point]
            for i in range(num_nodes):
                iterations += 1
                if self.anser[i] == start_letter:
                    startP = iterations
                elif self.anser[i] == self.end_point:
                    endP = iterations
            anser = "Вершина {} = П{}. Вершина {} = П{}. Расстояние между ними равно {}".format(start_letter, startP, end_letter, endP, self.anser_type2)
        return anser

    def get_ans_task(self, type_task: int) -> int:
        if type_task == 0 or type_task == 1:
            anser = (self.start_point + 1) * 10 + (self.end_point + 1)
        elif type_task == 2:
            anser = self.anser_type2
        return anser

Task1 = Generate_Solver_Task1(2)
type_task = 2
text = Task1.get_text_task()
matrix = Task1.get_matrix_task()
anser = Task1.get_ans_task(type_task)
text_anser = Task1.get_solving_task(type_task)
print(Task1.letters)
print(anser)
print(Task1.matrix)
print(matrix)
print(text_anser)
