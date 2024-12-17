import networkx as nx
import random
from generate_solver import Generate_Solver


class Generate_Solver_Task9:
    __text_task: str
    __matrix_task: list[list[int]]
    __solving_task: str
    __ans_task: int
    __names_vertex: list[str]

    __num_for_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'H', 7: 'G', 8: 'K', 9: 'M', 10: 'N',
                        11: 'L', 12: 'R'}

    def get_task(self) -> Generate_Solver:
        return Generate_Solver(self.__text_task, self.__matrix_task,
                               self.__names_vertex, self.__solving_task,
                               self.__ans_task)

    def __init__(self) -> None:
        # Создаёт по методам объект класса
        self.__generate_matrix()
        num_end = len(self.__matrix_task) - 1
        self.__generate_text_task(num_end + 1)
        self.__get_count_paths(self.__matrix_task)

    def __generate_matrix(self) -> None:
        # Введём ограничения по количеству вершин
        count_vertices = [7, 8, 9, 10, 11, 12]
        # Вероятности встречи количества вершин в задачах
        probabilities_vertices = [0.2, 0.1, 0.1, 0.2, 0.3, 0.1]

        # Зададим случайное число вершин
        num_vertices = random.choices(count_vertices, weights=probabilities_vertices, k=1)[0]

        # Создаём пустой граф
        G = nx.DiGraph()
        G.add_nodes_from(range(num_vertices))  # Добавляем вершины

        # Добавляем рёбра: каждая вершина может соединяться максимум с тремя последующими
        for i in range(num_vertices - 1):
            for j in range(i + 1, min(i + 4, num_vertices)):  # Ограничиваем переходы на 3 следующих
                if random.random() < 0.5:  # Вероятность 50%
                    G.add_edge(i, j)

        # Гарантируем связность: создаём путь от истока до стока
        for i in range(num_vertices - 1):
            if not G.has_edge(i, i + 1):
                G.add_edge(i, i + 1)

        # Проверяем планарность, добавляя дополнительные рёбра, если требуется
        for i in range(num_vertices):
            for j in range(i + 2, min(i + 4, num_vertices)):  # Снова ограничиваем переходы
                if random.random() < 0.3:  # Вероятность 30%
                    G.add_edge(i, j)
                    if not nx.check_planarity(G)[0]:  # Если граф перестаёт быть планарным
                        G.remove_edge(i, j)  # Удаляем последнее ребро

        # Перевод в обычный массив
        mas_np = nx.adjacency_matrix(G).todense()
        res = [[0] * len(mas_np) for _ in range(len(mas_np))]
        for i in range(len(mas_np)):
            for j in range(len(mas_np)):
                res[i][j] = int(mas_np[i][j])

        self.__matrix_task = res

    # TODO Генерирует только из первой в последнюю
    def __generate_text_task(self, count: int) -> None:
        str_vertex = ''
        self.__names_vertex = []
        for i in range(count):
            str_vertex += self.__num_for_letter[i] + ', '
            self.__names_vertex.append(self.__num_for_letter[i])
        str_vertex = str_vertex[:-2]

        self.__text_task = (
            f'На рисунке — схема дорог, связывающих города {str_vertex}. \nПо каждой дороге можно двигаться только в одном направлении, указанном стрелкой. \nСколько существует различных путей из города {self.__num_for_letter[0]} в город {self.__num_for_letter[count - 1]}?'
        )

    def __get_count_paths(self, matrix: list[list[int]]) -> None:
        # Матрица количества путей до всех вершин
        path_count = self.__count_paths(matrix)

        # Ответ - количество путей до последней вершины
        self.__ans_task = path_count[len(matrix) - 1]

        # Решение
        self.__solving_task = self.__solution_task(matrix, path_count)

    # Доп. методы
    # Cчитаем количество путей проходом по матрице
    def __count_paths(self, matrix: list[list[int]]) -> list[int]:
        distances = [0] * len(matrix)
        distances[0] = 1
        for j in range(len(distances)):
            for i, data in enumerate(matrix[j]):
                if data > 0:
                    distances[i] += distances[j]

        return distances

    # Вывод красивого решения
    def __solution_task(self, matrix: list[list[int]], mass_count_path: list[int]) -> str:
        ish_resh = 'Количество путей до города X = количество путей добраться в любой из тех городов, из которых есть дорога в Х.\nС помощью этого наблюдения посчитаем последовательно количество путей до каждого из городов:'

        mass_resh = [''] * len(mass_count_path)

        # В первую записываем 1
        mass_resh[0] += '1'

        for i in range(len(mass_count_path)):
            for j in range(1, len(mass_count_path)):
                if matrix[i][j] == 1:
                    if mass_resh[j] == '':
                        mass_resh[j] += str(self.__num_for_letter[i])
                    else:
                        mass_resh[j] += ' + ' + str(self.__num_for_letter[i])

        mass_resh[0] = str(self.__num_for_letter[0]) + ' = ' + mass_resh[0]
        for j in range(1, len(mass_count_path)):
            mass_resh[j] = str(self.__num_for_letter[j]) + ' = ' + mass_resh[j] + ' = '

        for i in range(len(mass_count_path)):
            for j in range(1, len(mass_count_path)):
                if matrix[i][j] == 1:
                    if mass_resh[j][-2] == '=':
                        mass_resh[j] += str(mass_count_path[i])
                    else:
                        mass_resh[j] += ' + ' + str(mass_count_path[i])

        for j in range(1, len(mass_count_path)):
            if mass_resh[j][-3] == '+' or mass_resh[j][-4] == '+' or mass_resh[j][-5] == '+':
                mass_resh[j] += ' = ' + str(mass_count_path[j])

        for row in mass_resh:
            # print(row)
            ish_resh += '\n' + row

        return ish_resh

