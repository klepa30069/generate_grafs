from generate_solver import Generate_Solver


class Generate_Solver_Task1:
    def get_task(self) -> Generate_Solver:
        return Generate_Solver('таск1\nпродолжение таск1', [
            [0, 1, 2, 3],
            [1, 0, 0, 4],
            [2, 0, 0, 1],
            [3, 4, 1, 0]
        ], ['A', 'B', 'C', 'D'], 'решение', 6)

    def __text_task(self) -> str:
        pass

    def __matrix_task(self) -> list[list[int]]:
        pass

    def __solving_task(self) -> str:
        pass

    def __ans_task(self) -> int:
        pass
