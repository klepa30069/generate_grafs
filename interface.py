from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QWidget, QFrame
)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Генерация и решение задач на графы по ОГЭ и ЕГЭ")
        self.setGeometry(100, 100, 800, 600)

        # Основной виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Главный вертикальный лейаут
        main_layout = QVBoxLayout()

        # Верхние кнопки
        top_buttons_layout = QHBoxLayout()
        top_buttons_layout.addWidget(QPushButton("Теория"))
        top_buttons_layout.addWidget(QPushButton("4 задача ОГЭ"))
        top_buttons_layout.addWidget(QPushButton("9 задача ОГЭ"))
        top_buttons_layout.addWidget(QPushButton("1 задача ЕГЭ"))
        main_layout.addLayout(top_buttons_layout)

        # Поле отображения задания
        self.task_display = QLabel("Отображение задания")
        self.task_display.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.task_display.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.task_display)

        # Средняя панель с полем ввода и кнопками
        middle_layout = QHBoxLayout()
        self.answer_input = QLineEdit()
        middle_layout.addWidget(self.answer_input)
        middle_layout.addWidget(QPushButton("Ответить"))
        middle_layout.addWidget(QPushButton("Показать решение"))
        main_layout.addLayout(middle_layout)

        # Поле отображения решения
        self.solution_display = QLabel("Отображение решения")
        self.solution_display.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.solution_display.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.solution_display)

        # Установка главного лейаута
        central_widget.setLayout(main_layout)


class Interface:
    def __init__(self) -> None:
        pass

    def click_button_1task(self) -> None:
        pass

    def click_button_4task(self) -> None:
        pass

    def click_button_9task(self) -> None:
        pass

    def click_button_theory(self) -> None:
        pass

    def click_button_answer(self) -> None:
        pass

    def click_button_solving(self) -> None:
        pass

    def show(self) -> None:
        pass

    def main(self) -> None:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
