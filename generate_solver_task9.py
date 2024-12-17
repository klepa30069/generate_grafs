from generate_solver import Generate_Solver


class Generate_Solver_Task9:
    __text_task: str
    __matrix_task: list[list[int]]
    __solving_task: str
    __ans_task: int

    __num_for_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'H', 7: 'G', 8: 'K', 9: 'M', 10: 'N', 11: 'L'}

    def get_task(self) -> Generate_Solver:
        return Generate_Solver(self.__text_task, [
            [0, 1, 2, 3],
            [0, 0, 0, 4],
            [0, 0, 0, 1],
            [0, 0, 0, 0]
        ], ['A', 'B', 'C', 'D'], 'решение', 6)

    def __init__(self) -> None:
        self.__generate_text_task(1)
        pass

    def __generate_text_task(self, count: int) -> None:
        # str_vertex = ''
        # self.__names_vertex = []
        # for i in range(count):
        #     str_vertex += self.__num_for_letter[i] + ', '
        #     self.__names_vertex.append(self.__num_for_letter[i])
        # str_vertex = str_vertex[:-2]
        count = 5
        str_vertex = ['A','B','C','D']

        self.__text_task = (
                f'На рисунке - схема дорог, связывающих города {str_vertex}.' +
                f'По каждой дороге можно двигаться только в одном направлении, указанном стрелкой.\n' +
                f'Сколько существует различных путей из города {self.__num_for_letter[0]} в город {self.__num_for_letter[count - 1]}?')
