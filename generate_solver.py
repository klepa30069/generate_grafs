class Generate_Solver:
    __text_task: str
    __matrix_task: list[list[int]]
    __solving: str

    def __init__(self, text_task: str, matrix_task: list[list[int]], solving: str, ans: int) -> None:
        self.__text_task = text_task
        self.__matrix_task = matrix_task
        self.__solving = solving
        self.__ans = ans

    def get_text_task(self) -> str:
        return self.__text_task

    def get_matrix_task(self) -> list[list[int]]:
        return self.__matrix_task

    def get_solving_task(self) -> str:
        return self.__solving

    def get_ans_task(self) -> int:
        return self.__ans
