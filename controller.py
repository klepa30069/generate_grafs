from generate_solver import Generate_Solver
from task import Task


class Controller:
    __tasks1: list[Generate_Solver]
    __tasks4: list[Generate_Solver]
    __tasks9: list[Generate_Solver]

    def __init__(self) -> None:
        self.__tasks1 = []
        self.__tasks4 = []
        self.__tasks9 = []

    def get_new_task(self, type_task: int) -> Generate_Solver:
        result = Task().get_task(type_task)
        if type_task == 1:
            if result in self.__tasks1:
                result = Task().get_task(type_task)
            self.__tasks1.append(result)
            return result
        elif type_task == 4:
            if result in self.__tasks4:
                result = Task().get_task(type_task)
            self.__tasks4.append(result)
            return result
        elif type_task == 9:
            if result in self.__tasks9:
                result = Task().get_task(type_task)
            self.__tasks9.append(result)
            return result

    def get_theory(self) -> str:
        pass
