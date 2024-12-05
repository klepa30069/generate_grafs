from matplotlib import pyplot as plt


class Generate_Solver:
    __text_task: str
    __matrix_task: list[list[int]]
    __solving: str
    __headers: list[str]

    def __init__(self, text_task: str,
                 matrix_task: list[list[int]], headers: list[str],
                 solving: str, ans: int) -> None:
        self.__text_task = text_task
        self.__matrix_task = matrix_task
        self.__headers = headers
        self.__solving = solving
        self.__ans = ans

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
        # Создание изображения таблицы с помощью matplotlib
        fig, ax = plt.subplots(figsize=(3, 3))  # Размер изображения подгоняется под таблицу
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
        table.auto_set_column_width(col=list(range(len(self.__headers))))

        # Сохранение таблицы как изображения
        table_image_path = "image_task_graf.png"
        plt.tight_layout()
        plt.savefig(table_image_path, bbox_inches="tight", dpi=200)  # Увеличен DPI для чёткого изображения
        plt.close(fig)

        # Возврат имени файла
        return table_image_path

    def get_matrix_task(self) -> list[list[int]]:
        return self.__matrix_task

    def get_solving_task(self) -> str:
        return self.__solving

    def get_ans_task(self) -> int:
        return self.__ans
