from generate_solver import Generate_Solver


class Controller:
    __tasks1: list[Generate_Solver]
    __tasks4: list[Generate_Solver]
    __tasks9: list[Generate_Solver]
    __type_tasks: int
    __index_tasks: int

    def __init__(self) -> None:
        pass

    def get_new_task(self, type_task: int) -> Generate_Solver:
        pass

    def get_solving_task(self, type_task: int) -> Generate_Solver:
        pass

    def get_theory(self) -> str:
        pass
