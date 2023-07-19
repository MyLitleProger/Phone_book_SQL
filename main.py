import sys
import models

if __name__ == '__main__':
    app = models.QApplication(sys.argv)
    window = models.GW()
    window.show()

    sys.exit(app.exec())

