from generate_solver import Generate_Solver


class Generate_Solver_Task9:
    __text_task: str
    __matrix_task: list[list[int]]
    __solving_task: str
    __ans_task: int

    __num_for_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'H', 7: 'G', 8: 'K', 9: 'M', 10: 'N', 11: 'L'}

    def get_task(self) -> Generate_Solver:
        return Generate_Solver('таск9\nпродолжение таск9', [
            [0, 1, 2, 3],
            [1, 0, 0, 4],
            [2, 0, 0, 1],
            [3, 4, 1, 0]
        ], ['A', 'B', 'C', 'D'], 'решение', 6)

    def __init__(self) -> None:
        pass
