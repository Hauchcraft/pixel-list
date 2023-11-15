from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Configurar la ventana principal
        self.setWindowTitle("Lista de Tareas")
        self.setGeometry(100, 100, 400, 300)

        # Barra de navegación para agregar tareas
        add_navbar = QToolBar("Agregar Tarea")
        self.addToolBar(add_navbar)

        # Acción para agregar nueva tarea
        add_action = QAction("Agregar Tarea", self)
        add_action.triggered.connect(self.add_task)
        add_navbar.addAction(add_action)

        # Barra de navegación para acciones en tareas
        task_navbar = QToolBar("Acciones en Tareas")
        self.addToolBar(task_navbar)

        # Acciones para la barra de navegación de tareas
        delete_action = QAction("Eliminar Tareas", self)
        delete_action.triggered.connect(self.delete_tasks)
        task_navbar.addAction(delete_action)

        # Barra de herramientas para mostrar las tareas
        show_tasks_toolbar = QToolBar("Tareas Actuales")
        self.addToolBar(show_tasks_toolbar)

        # Etiqueta para mostrar las tareas
        self.tasks_label = QLabel("Tareas:\n", self)
        show_tasks_toolbar.addWidget(self.tasks_label)

        # Aplicar estilos a las barras de navegación
        self.setStyleSheet("""
            QToolBar {
                background-color: #455A64;
                color: white;
                border: 1px solid #37474F;
            }
            QToolBar QToolButton {
                background-color: #607D8B;
                border: 1px solid #546E7A;
            }
            QToolBar QToolButton:hover {
                background-color: #78909C;
            }
            QLabel {
                color: #263238;
                font-size: 14px;
            }
            QLabel:hover {
                color: #37474F;
            }
        """)

        # Lista de tareas
        self.task_list = []

    def add_task(self):
        text, ok = QInputDialog.getText(self, "Agregar Tarea", "Ingrese la nueva tarea:")
        if ok and text:
            self.task_list.append(text)
            self.update_show_tasks_toolbar()

    def delete_tasks(self):
        # Puedes realizar acciones relacionadas con la eliminación de tareas aquí si es necesario
        self.task_list = []
        self.update_show_tasks_toolbar()

    def update_show_tasks_toolbar(self):
        tasks_text = '\n'.join(self.task_list)
        self.tasks_label.setText(f"Tareas:\n{tasks_text}")

if __name__ == '__main__':
    app = QApplication([])

    # Aplicar estilos globales a la aplicación
    app.setStyleSheet("""
        QMainWindow {
            background-color: #ECEFF1;
        }
    """)

    main_window = MainWindow()
    main_window.show()
    app.exec_()
