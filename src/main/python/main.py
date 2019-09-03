import json
import sys
from pathlib import Path

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialogButtonBox

from junction import Ui_Junction


here = Path(__file__).parent
python_src_dir = Path(here).parent


class MainWindow(QMainWindow, Ui_Junction):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.RPCSettingsDialog.button(QDialogButtonBox.Save).clicked.connect(
            lambda: self.update_settings()
        )

    def update_settings(self):
        with open(python_src_dir / "settings/settings.json") as settings:
            data = json.load(settings)
        data["rpc_username"] = self.rPCUsernameLineEdit.text()
        data["rpc_password"] = self.rPCPasswordLineEdit.text()
        data["rpc_host"] = self.rPCHostLineEdit.text()
        data["rpc_port"] = self.rPCPortLineEdit.text()
        with open(python_src_dir / "settings/settings.json", "w") as outfile:
            json.dump(data, outfile, indent=4)


if __name__ == "__main__":
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
