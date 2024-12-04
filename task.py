from generate_solver import Generate_Solver
from generate_solver_task1 import Generate_Solver_Task1
from generate_solver_task4 import Generate_Solver_Task4
from generate_solver_task9 import Generate_Solver_Task9


class Task:
    def get_task(self, type_task: int) -> Generate_Solver | None:
        if type_task == 1:
            return Generate_Solver_Task1().get_task()
        elif type_task == 4:
            return Generate_Solver_Task4().get_task()
        elif type_task == 9:
            return Generate_Solver_Task9().get_task()
