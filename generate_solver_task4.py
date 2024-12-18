from generate_solver import Generate_Solver
import random
import heapq


class Generate_Solver_Task4:
    __text_task: str
    __matrix_task: list[list[int]]
    __solving_task: str
    __ans_task: int
    __names_vertex: list[str]

    __num_for_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'H', 7: 'G', 8: 'K', 9: 'M', 10: 'N'}

    def get_task(self) -> Generate_Solver:
        return Generate_Solver(self.__text_task, self.__matrix_task,
                               self.__names_vertex, self.__solving_task,
                               self.__ans_task)

    def __init__(self) -> None:
        self.__generate_matrix()
        num_end = len(self.__matrix_task) - 1
        self.__generate_text_task(num_end + 1)

        # Находим все возможные маршруты
        all_routes, shortest_distance = self.__find_all_routes(self.__matrix_task, 0, num_end)

        # Находим маршрут с минимальной длиной
        shortest_route = min(all_routes, key=lambda x: x[1])

        # Формируем строку с путями
        self.__solving_task = "Все возможные маршруты:\n"
        for route, _ in all_routes:
            self.__solving_task += f"Существует маршрут: {' -> '.join(route)}\n"

        # Добавляем самый короткий маршрут в конец
        self.__solving_task += f"\nСамый короткий маршрут: {' -> '.join(shortest_route[0])}"

        # Устанавливаем правильное расстояние в переменную __ans_task
        self.__ans_task = shortest_distance  # Сохраняем расстояние самого короткого маршрута

    # Вспомогательные алгоритмы
    def __generate_matrix(self) -> None:
        # Максимальное значение веса ребра
        max_weight_edge = 10

        # Введём ограничения по количеству вершин
        count_vertices = [4, 5, 6]
        # Вероятности встречи количества вершин в задачах
        probabilities_vertices = [0.1, 0.6, 0.3]

        # Зададим случайное число вершин
        num_vertices = random.choices(count_vertices, weights=probabilities_vertices, k=1)[0]
        # num_vertices = random.randint(min_vertices, max_vertices)

        # Создадим матрицу смежности с нулями
        matrix = [[0] * num_vertices for _ in range(num_vertices)]

        # Для того, чтобы граф был связным
        # Создадим минимальное остовное дерево
        # TODO Можно подумать как усложнить условие связности, чтобы вершины были соединены не только 1 -> 2 -> ...
        for i in range(1, num_vertices):
            # Генерим с небольшим ограничением сверху, чтобы было выгоднее идти через большее количество вершин
            weight = random.randint(1, max_weight_edge - 3)
            matrix[i - 1][i] = weight
            matrix[i][i - 1] = weight

        # TODO Можно подумать, чтобы добавить зависимость и ограничение количества рёбер от количества вершин (ввести счётчик рёбер)

        # OLD solver
        # Добавляем дополнительные рёбра с вероятностью, чтобы увеличить плотность
        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                if num_vertices == 4:  # Для 4-х вершин заполняем все рёбра
                    if matrix[i][j] == 0:
                        weight = random.randint(2, max_weight_edge)
                        matrix[i][j] = weight
                        matrix[j][i] = weight
                else:
                    if matrix[i][j] == 0 and random.random() < 0.5:  # Вероятность 50%
                        weight = random.randint(2, max_weight_edge)
                        matrix[i][j] = weight
                        matrix[j][i] = weight

        # Добавляем вероятность соединения первой вершины с последней с большим весом
        if matrix[num_vertices - 1][0] != 0:
            weight = random.randint((max_weight_edge // 2) * num_vertices, max_weight_edge * 3 + 1)
            matrix[num_vertices - 1][0] = weight
            matrix[0][num_vertices - 1] = weight

        # Сохраняем в объект класса сгенерированную матрицу
        self.__matrix_task = matrix

    # TODO Генерирует только из первой в последнюю

    def __generate_text_task(self, count: int) -> None:
        str_vertex = ''
        self.__names_vertex = []
        for i in range(count):
            str_vertex += self.__num_for_letter[i] + ', '
            self.__names_vertex.append(self.__num_for_letter[i])
        str_vertex = str_vertex[:-2]

        self.__text_task = (
                f'Между населенными пунктами {str_vertex} построены дороги, протяженность которых (в километрах) приведена в таблице:\n' +
                f'Определите длину кратчайшего пути между пунктами {self.__num_for_letter[0]} и {self.__num_for_letter[count - 1]} - первым и последним. ' +
                'Передвигаться можно только по дорогам, протяженность которых указана в таблице.')

    def __find_all_routes(self, graph: list[list[int]], start: int, end: int) -> tuple[
        list[tuple[list[str], int]], int]:
        all_routes = []
        shortest_distance = float('inf')

        # Вспомогательная функция для поиска маршрутов
        def dfs(current, path, current_distance, visited):
            nonlocal shortest_distance
            if current == end:
                # Если дошли до конечной вершины, сохраняем путь и его длину
                all_routes.append((path[:], current_distance))  # Копируем путь
                shortest_distance = min(shortest_distance, current_distance)
                return

            # Проходим по всем соседям
            for neighbor, weight in enumerate(graph[current]):
                if weight > 0 and neighbor not in visited:  # Если существует ребро и вершина еще не в пути
                    visited.add(neighbor)  # Добавляем вершину в посещённые
                    path.append(self.__num_for_letter[neighbor])
                    dfs(neighbor, path, current_distance + weight, visited)
                    path.pop()  # Убираем вершину из пути
                    visited.remove(neighbor)  # Убираем вершину из посещённых

        # Инициализация с начальной вершины
        visited = set([start])  # Множество посещённых вершин
        dfs(start, [self.__num_for_letter[start]], 0, visited)

        return all_routes, shortest_distance
 # TODO могут быть несколько путей одинаковой длины