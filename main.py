from PySide6.QtWidgets import QApplication
from Controller.ControllerDisplay import MainController

if __name__ == "__main__":
    app = QApplication([])

    # 메인 컨트롤러 실행
    controller = MainController()
    controller.run()
    app.exec()