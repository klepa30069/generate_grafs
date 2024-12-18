from typing import Any
import networkx as nx
import numpy as np
from generate_solver import Generate_Solver
import random
from collections import Counter


class Generate_Solver_Task1:
    __type_task: int
    __points: list
    __num_letters: int
    __letters: dict
    __start_point: int
    __end_point: int
    __matrix: np.ndarray[Any, np.dtype]
    __add_one: bool
    __Counts: Counter
    __answer: int
    __text_task: str
    __solving_task: str
    __send_letter: list
    __senf_matrix: list[list[int]]
    __answer_type2: int

    def __init__(self) -> None:
        self.__Counts = None
        self.__answer = None
        self.__text_task = None
        self.__check_answer = None
        self.__send_letter = None
        self.__answer_type2 = None
        self.__original_matrix = None
        self.__type_task = self.__type_task_generate()
        self.__points = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
        self.__num_letters = random.randint(6, 8)
        self.__letters = self.__random_letter()
        self.__start_point, self.__end_point = self.__random_start_letter()
        self.__start_letter = self.__letters[self.__start_point]
        self.__end_letter = self.__letters[self.__end_point]
        self.__matrix = self.__get_matrix_task()
        self.__add_one = False
        self.__solving_task = self.__get_solving_task()
        self.__senf_matrix = [[int(x) for x in row] for row in self.__matrix]

    def get_task(self) -> Generate_Solver:
        self.__get_ans_task()
        self.__get_text_task()
        return Generate_Solver(self.__text_task, self.__original_matrix,
                               ['П' + str(i + 1) for i in range(len(self.__original_matrix))], self.__solving_task,
                               self.__answer)

    def __get_text_task(self) -> None:
        if self.__type_task == 0:
            self.__text_task = (f"На рисунке справа схема дорог Н-ского района изображена в виде графа, " +
                                "в таблице содержатся сведения о дорогах между населенными пунктами " +
                                "(звездочка означает, что дорога между соответствующими городами есть)." +
                                "Так как таблицу и схему рисовали независимо друг от друга, " +
                                "то нумерация населённых пунктов в таблице никак не связана с буквенными обозначениями на графе.\n" +
                                f"Определите номера населенных пунктов {self.__points[self.__start_point]} и {self.__points[self.__end_point]} в таблице. " +
                                "В ответе запишите числа в порядке возрастания без разделителей.")
        elif self.__type_task == 1:
            self.__text_task = ("На рисунке схема дорог изображена в виде графа, " +
                                "в таблице содержатся сведения о длине этих дорог в километрах. " +
                                "Поскольку таблицу и схему рисовали независимо друг от друга, " +
                                "нумерация населённых пунктов в таблице никак не связана с буквенными обозначениями на графе.\n" +
                                f"Определите длину дороги {self.__points[self.__start_point]}, {self.__points[self.__end_point]}. " +
                                "В ответе запишите целое число — длину дороги в километрах.")
        elif self.__type_task == 2:
            self.__text_task = ("На рисунке справа схема дорог Н-ского района изображена в виде графа, " +
                                "в таблице содержатся сведения о длинах этих дорог (в километрах)." +
                                "Так как таблицу и схему рисовали независимо друг от друга, " +
                                "то нумерация населённых пунктов в таблице никак не связана с буквенными обозначениями на графе.\n" +
                                f"Определите, какова длина дороги из пункта {self.__points[self.__start_point]} в пункт {self.__points[self.__end_point]}. В ответе запишите целое число — так, как оно указано в таблице.")

    def __type_task_generate(self) -> int:
        numbers = [0, 1, 2]
        weights = [0.25, 0.25, 0.5]
        choice = random.choices(numbers, weights=weights, k=1)[0]
        return choice

    def __random_letter(self) -> dict:  # Рандомайзер букв в матрице
        letters = random.sample(self.__points, self.__num_letters)  # Выбирает __num_letters уникальных букв
        return dict(enumerate(letters))

    def __random_start_letter(self) -> (int, int):  # Рандомайзер стартовых буковок
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        point1, point2 = random.sample(numbers[:self.__num_letters], 2)
        return point1, point2

    def __shuffle_adjacency_matrix(self, adjacency_matrix) -> np.ndarray[Any, np.dtype]:
        """Перемешивает вершины в матрице смежности, используя NumPy."""
        adjacency_matrix = np.array(adjacency_matrix)
        num_nodes = len(adjacency_matrix)
        permutation = np.random.permutation(num_nodes)  # Случайная перестановка индексов
        shuffled_matrix = adjacency_matrix[:, permutation][permutation,
                          :]  # Применяем перестановку к строкам и столбцам
        self.__check_answer = [self.__letters[i] for i in permutation]
        self.__send_letter = self.__check_answer
        self.__start_point = next((i for i, letter in enumerate(self.__check_answer) if letter == self.__start_letter),
                                  None)
        self.__end_point = next((i for i, letter in enumerate(self.__check_answer) if letter == self.__end_letter),
                                None)
        return shuffled_matrix

    def __generate_random___matrix_with_edges(self, num_nodes, num_edges) -> list[list[int]]:
        """Генерирует случайную матрицу смежности с заданным количеством ребер."""
        adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]
        edges_added = 0
        while True:  # Попытка генерации планарного графа
            adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]  # Обнуляем матрицу для новой попытки
            edges_added = 0

            # Генерируем начальные ребра с проверкой
            for i in range(num_nodes):
                if edges_added >= num_edges:
                    break

                neighbor = random.choice([j for j in range(num_nodes) if j != i])
                if self.__type_task == 0:
                    adjacency_matrix[i][neighbor] = 1
                    adjacency_matrix[neighbor][i] = 1
                else:
                    rand_val = random.randint(10, 100)
                    adjacency_matrix[i][neighbor] = rand_val
                    adjacency_matrix[neighbor][i] = rand_val

                    # Проверка ребра
                    if (i == self.__start_point or i == self.__end_point) and (
                            neighbor == self.__start_point or neighbor == self.__end_point):
                        self.__answer_type2 = rand_val
                edges_added += 1

            graph = nx.from_numpy_array(
                np.array(adjacency_matrix))  # Преобразовываем матрицу в граф networkx для проверки планарности
            if nx.check_planarity(graph)[0] and nx.is_connected(graph):
                break
        if self.__type_task == 0:
            if adjacency_matrix[self.__start_point][self.__end_point] == 0:
                adjacency_matrix[self.__start_point][self.__end_point] = 1
                adjacency_matrix[self.__end_point][self.__start_point] = 1
        elif self.__type_task != 0:
            if adjacency_matrix[self.__start_point][self.__end_point] == 0:
                rand_val = random.randint(10, 100)
                adjacency_matrix[self.__start_point][self.__end_point] = rand_val
                adjacency_matrix[self.__end_point][self.__start_point] = rand_val
                self.__answer_type2 = rand_val
        self.__original_matrix = adjacency_matrix
        return adjacency_matrix

    def __add_node_list(self, adjacency_matrix: list[list[int]]) -> list[list[int]]:
        """Добавляет узел в матрицу смежности, представленную списком списков."""
        for row in adjacency_matrix:
            row.append(0)
        num_nodes = len(adjacency_matrix)
        new_row = [0] * (num_nodes + 1)
        adjacency_matrix.append(new_row)
        random_val, empty = self.__random_start_letter()
        if self.__type_task == 0:
            adjacency_matrix[num_nodes][random_val] = 1
            adjacency_matrix[random_val][num_nodes] = 1
        elif self.__type_task != 0:
            rand_val = random.randint(10, 100)
            adjacency_matrix[num_nodes][random_val] = rand_val
            adjacency_matrix[random_val][num_nodes] = rand_val
        return adjacency_matrix

    def __add_counter(self, all_el: list) -> None:
        self.__Counts = Counter(all_el)

    def __check_rows(self, matrix: list[list[int]]) -> list[list[int]]:
        all_el = []
        result = False
        for el in range(self.__num_letters):
            sum = 0
            for deep_el in matrix[el]:
                sum += deep_el
            all_el.append(sum)
        self.__add_counter(all_el)
        for count in self.__Counts.values():
            if count == 1:
                result = True
        if not result:
            matrix = self.__add_node_list(matrix)
            self.__add_one = True
            self.__letters[self.__num_letters] = "I"
        return matrix

    def __get_matrix_task(self) -> np.ndarray[Any, np.dtype]:
        num_nodes = self.__num_letters
        num_edges = (3 * num_nodes / 2)
        adjacency_matrix = self.__generate_random___matrix_with_edges(num_nodes, num_edges)
        self.__check_rows(adjacency_matrix)
        self.Task__matrix = self.__shuffle_adjacency_matrix(adjacency_matrix)
        return self.Task__matrix

    def __get_solving_task(self) -> str:
        num_nodes = len(self.__matrix)
        answer = f'Ответ:\n'
        if self.__type_task != 2:
            for i in range(num_nodes):
                answer += "Вершина {} = П{}.\n".format(self.__points[i], i + 1)
            self.__get_text_task()
        else:
            for i in range(len(self.__original_matrix)):
                for j in range(len(self.__original_matrix[i])):
                    if self.__original_matrix[i][j] == self.__answer:
                        self.__start_point = i
                        self.__end_point = j
                        break
            answer += "Вершина {} = П{}.\nВершина {} = П{}.".format(
                self.__points[self.__start_point], self.__start_point + 1,
                self.__points[self.__end_point], self.__end_point + 1)
            self.__get_text_task()
        return answer

    def __get_ans_task(self) -> None:
        if self.__type_task == 0:
            self.__answer = int(str(self.__start_point) + str(self.__end_point)) + 11
        elif self.__type_task == 1:
            if self.__original_matrix[self.__start_point][self.__end_point] == 0:
                rand_val = random.randint(10, 100)
                self.__original_matrix[self.__start_point][self.__end_point] = rand_val
                self.__original_matrix[self.__end_point][self.__start_point] = rand_val
            self.__answer = self.__original_matrix[self.__end_point][self.__start_point]
        elif self.__type_task == 2:
            self.__answer = self.__answer_type2
