import networkx as nx
from matplotlib import pyplot as plt


class Generate_Solver:
    __text_task: str
    __matrix_task: list[list[str]]
    __solving: str
    __headers: list[str]
    __num_for_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'H', 7: 'G', 8: 'K', 9: 'M', 10: 'N',
                        11: 'L', 12: 'R'}

    def __init__(self, text_task: str,
                 matrix_task: list[list[int]], headers: list[str],
                 solving: str, ans: int) -> None:
        self.__text_task = text_task
        self.__matrix_int_str(matrix_task)
        self.__headers = headers
        self.__solving = solving
        self.__ans = ans

    def __matrix_int_str(self, matrix_task: list[list[int]]) -> None:
        maxsis = max(matrix_task)
        self.__matrix_task = [['' for _ in range(len(matrix_task))] for _ in range(len(matrix_task))]
        for i in range(len(matrix_task)):
            for j in range(len(matrix_task)):
                self.__matrix_task[i][j] = '' if matrix_task[i][j] == 0 else '*' if maxsis == 1 else str(matrix_task[i][j])

    def get_text_task(self) -> str:
        return self.__text_task

    def get_image_matrix(self) -> str:
        # Создание изображения таблицы с помощью matplotlib
        fig, ax = plt.subplots(figsize=(3, 1.8))  # Размер изображения подгоняется под таблицу
        ax.axis("tight")
        ax.axis("off")
        table = ax.table(
            cellText=self.__matrix_task,
            colLabels=self.__headers,
            rowLabels=self.__headers,
            cellLoc="center",
            loc="center",
        )
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        # table.auto_set_column_width(col=list(range(len(self.__headers))))

        # Сохранение таблицы как изображения
        table_image_path = "image_task_table.png"
        plt.tight_layout()
        plt.savefig(table_image_path, bbox_inches="tight", dpi=200)  # Увеличен DPI для чёткого изображения
        plt.close(fig)

        # Возврат имени файла
        return table_image_path

    # TODO graf to image
    def get_image_graf(self) -> str:
        G = nx.Graph()
        num_nodes = len(self.__matrix_task)
        for i in range(num_nodes):
            for j in range(i, num_nodes):  # Начинаем с j=i, чтобы избежать дублирования ребер
                if self.__matrix_task[i][j] != self.__matrix_task[j][i]:
                    G = nx.DiGraph()
                    break
        # Добавляем узлы в граф
        G.add_nodes_from(self.__num_for_letter[i] for i in range(num_nodes))
        # Добавляем ребра в граф на основе матрицы смежности
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):  # Начинаем с j=i, чтобы избежать дублирования ребер
                if self.__matrix_task[i][j] != 0 and self.__matrix_task[i][j] != '':
                    G.add_edge(self.__num_for_letter[i], self.__num_for_letter[j])
        # Сохранение таблицы как изображения
        table_image_path = "image_task_graf.png"

        plt.clf()
        if type(G) == nx.DiGraph:
            plt.figure(figsize=(4, 2))
        else:
            plt.figure(figsize=(2, 2))

        # TODO изменяем отображение в зависимости от количества вершин
        pos = nx.planar_layout(G)  # Используем расположение для графа
        # Указываем фиксированное расположение вершин
        if type(G) == nx.DiGraph:
            if len(self.__matrix_task) == 7:
                pos = {
                    'A': (0, 0),
                    'B': (2, 3),
                    'C': (2, -3),
                    'D': (5, 3),
                    'E': (5, -3),
                    'F': (7, 0),
                    'H': (9, 0)
                }
            elif len(self.__matrix_task) == 8:
                pos = {
                    'A': (0, 0),
                    'B': (2, 3),
                    'C': (2, -3),
                    'D': (3, 1),
                    'E': (3, -1),

                    'F': (5, 3),
                    'H': (5, -3),
                    'G': (7, 0)
                }
            # TODO ?
            elif len(self.__matrix_task) == 9:
                pos = {
                    'A': (0, 0),
                    'B': (2, 3),
                    'C': (2, -3),
                    'D': (3, 0),
                    'E': (5, 3),
                    'F': (5, -3),
                    'H': (6, 0),
                    'G': (8, 3),
                    'K': (9, 0)
                }
            elif len(self.__matrix_task) == 10:
                pos = {
                    'A': (0, 0),
                    'B': (2, 3),
                    'C': (2, -3),
                    'D': (3, 0),
                    'E': (5, 3),
                    'F': (5, -3),
                    'H': (6, 0),
                    'G': (8, 3),
                    'K': (8, -3),
                    'M': (9, 0)
                }
            elif len(self.__matrix_task) == 11:
                pos = {
                    'A': (0, 0),
                    'B': (2, 3),
                    'C': (2, -3),
                    'D': (3, 1),
                    'E': (3, -1),
                    'F': (5, 3),
                    'H': (5, -3),
                    'G': (6, 0),
                    'K': (8, 3),
                    'M': (8, -3),
                    'N': (9, 0)
                }
            elif len(self.__matrix_task) == 12:
                pos = {
                    'A': (0, 0),
                    'B': (2, 3),
                    'C': (2, -3),
                    'D': (3, 1),
                    'E': (3, -1),
                    'F': (5, 3),
                    'H': (5, -3),
                    'G': (6, 0),
                    'K': (8, 0),
                    'M': (10, 3),
                    'N': (10, -3),
                    'L': (12, 0),
                }
        nx.draw(G, pos, with_labels=True, node_size=100, node_color='lightblue', font_size=8, font_weight='bold')
        plt.savefig(table_image_path, bbox_inches="tight", dpi=200)  # Увеличен DPI для чёткого изображения
        plt.close()
        plt.clf()
        # Возврат имени файла
        return table_image_path

    def get_matrix_task(self) -> list[list[str]]:
        return self.__matrix_task

    def get_solving_task(self) -> str:
        return self.__solving

    def get_ans_task(self) -> int:
        return self.__ans
