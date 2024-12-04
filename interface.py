from controller import Controller
from generate_solver import Generate_Solver
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QWidget, QFrame
)
import sys


class Interface:
    __name: str
    __height: int
    __weight: int
    __show_second_block: bool
    __show_third_block: bool
    __answer_click: bool
    __task: Generate_Solver
    # Поля необходимые для работы с интерфейсом между функциями
    __window: QWidget
    __main_layout: QVBoxLayout
    __answer_input: QLineEdit
    __task_display: QLabel
    __solution_display: QLabel

    def __init__(self) -> None:
        self.__name = "Генерация и решение задач на графы по ОГЭ и ЕГЭ"
        self.__height = 100
        self.__weight = 800
        self.__show_second_block = False
        self.__show_third_block = False
        self.__answer_click = False

    def __add_second_block(self) -> None:
        # Создание второго блока
        # Поле отображения задания
        # TODO нормальное отображение задачи
        self.__task_display = QLabel(f'{self.__task.get_text_task()} {self.__task.get_matrix_task()}')
        self.__task_display.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.__task_display.setAlignment(Qt.AlignCenter)

        # Средняя панель с полем ввода и кнопками
        self.__answer_input = QLineEdit()
        button_answer = QPushButton("Ответить")
        button_show_solving = QPushButton("Показать решение")

        # Обработка нажатий на кнопки
        button_answer.clicked.connect(self.click_button_answer)
        button_show_solving.clicked.connect(self.click_button_solving)

        # Создание отображения второго блока
        center_layout = QVBoxLayout()
        center_layout.addWidget(self.__task_display)
        middle_layout = QHBoxLayout()
        middle_layout.addWidget(self.__answer_input)
        middle_layout.addWidget(button_answer)
        middle_layout.addWidget(button_show_solving)
        center_layout.addLayout(middle_layout)

        # Добавления второго блока в основной лэйаут
        self.__main_layout.addLayout(center_layout)

        # Изменение размера окна
        self.__show_second_block = True
        self.__height = 350
        self.__window.setFixedHeight(self.__height)

    def __add_third_block(self) -> None:
        # Создание третьего блока
        # Поле отображения решения
        # TODO нормальное отображение решения
        self.__solution_display = QLabel(self.__task.get_solving_task())
        self.__solution_display.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.__solution_display.setAlignment(Qt.AlignCenter)

        # Создание отображения третьего блока
        bottom_layout = QVBoxLayout()
        bottom_layout.addWidget(self.__solution_display)

        # Добавления третьего блока в основной лэйаут
        self.__main_layout.addLayout(bottom_layout)

        # Изменение размера окна
        self.__show_third_block = True
        self.__height = 600
        self.__window.setFixedHeight(self.__height)

    def __click_button_task(self, type_task: int) -> None:
        if not self.__show_second_block:
            self.__task = Controller().get_new_task(type_task)
            self.__add_second_block()
        elif self.__answer_click:
            self.__task = Controller().get_new_task(type_task)
            self.__show_third_block = False
            self.__solution_display.hide()

            # Изменение размера окна
            self.__height = 350
            self.__window.setFixedHeight(self.__height)

            self.__answer_click = False
            self.__answer_input.setText('')
            self.__answer_input.setStyleSheet("background-color: white")
            # TODO нормальное отображение задачи
            self.__task_display.setText(f'{self.__task.get_text_task()} {self.__task.get_matrix_task()}')

    def click_button_1task(self) -> None:
        self.__click_button_task(1)

    def click_button_4task(self) -> None:
        self.__click_button_task(4)

    def click_button_9task(self) -> None:
        self.__click_button_task(9)

    def click_button_theory(self) -> None:
        pass

    def click_button_answer(self) -> None:
        self.__answer_click = True
        answer = self.__answer_input.text()
        if not answer.isnumeric():
            self.__answer_input.setStyleSheet("background-color: red")
        else:
            if self.__task.get_ans_task() == int(answer):
                self.__answer_input.setStyleSheet("background-color: green")
            else:
                self.__answer_input.setStyleSheet("background-color: red")

    def click_button_solving(self) -> None:
        if not self.__show_third_block:
            if self.__answer_click:
                self.__add_third_block()

    def show(self) -> None:
        # Создание приложения
        app = QApplication([])  # sys.argv)

        # Создание окна
        self.__window = QWidget()
        self.__window.setWindowTitle(self.__name)
        self.__window.resize(self.__weight, self.__height)
        # self.window.setStyleSheet("background-color:red;border-radius:15px;")

        # Главный вертикальный лейаут
        self.__main_layout = QVBoxLayout()

        # Создание первого блока
        # Создание кнопок первого блока
        button_theory = QPushButton("Теория")
        button_4_OGE = QPushButton("4 задача ОГЭ")
        button_9_OGE = QPushButton("9 задача ОГЭ")
        button_1_EGE = QPushButton("1 задача ЕГЭ")

        # Обработка нажатий на кнопки
        button_theory.clicked.connect(self.click_button_theory)
        button_1_EGE.clicked.connect(self.click_button_1task)
        button_4_OGE.clicked.connect(self.click_button_4task)
        button_9_OGE.clicked.connect(self.click_button_9task)

        # Создание отображения первого блока
        top_layout = QHBoxLayout()
        top_layout.addWidget(button_theory)
        top_layout.addWidget(button_4_OGE)
        top_layout.addWidget(button_9_OGE)
        top_layout.addWidget(button_1_EGE)

        # Добавления первого блока в основной лэйаут
        self.__main_layout.addLayout(top_layout)

        # Установка основного лэйаута
        self.__window.setLayout(self.__main_layout)

        # Отображать окно
        self.__window.show()

        # Оставлять приложение открытым
        # sys.exit(app.exec_())
        app.exec_()
