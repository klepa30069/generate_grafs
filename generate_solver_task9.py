from generate_solver import Generate_Solver


class Generate_Solver_Task9:
    __text_task: str
    __matrix_task: list[list[int]]
    __solving_task: str
    __ans_task: int

    __num_for_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'H', 7: 'G', 8: 'K', 9: 'M', 10: 'N'}

    def get_task(self) -> Generate_Solver:
        return Generate_Solver(self.__text_task, self.__matrix_task, self.__solving_task, self.__ans_task)

    def __text_task(self) -> str:
        pass

    def __matrix_task(self) -> list[list[int]]:
        pass

    def __solving_task(self) -> str:
        pass

    def __ans_task(self) -> int:
        pass
