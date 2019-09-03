import json
import sys
from collections import OrderedDict
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
        self.update_RPCSettingsDialogue()

    def update_RPCSettingsDialogue(self):
        self.currentRPCSettingsTextBrowser.setPlainText(self.read_rpc_settings())

    def read_rpc_settings(self):
        with open(python_src_dir / "settings/settings.json") as settings:
            set_d = json.load(settings, object_pairs_hook=OrderedDict)
            set_str = ""
            for k, v in set_d.items():
                set_str += f"{k}: {v}\n"
            return set_str

    def update_settings(self):
        with open(python_src_dir / "settings/settings.json") as settings:
            data = json.load(settings)
        data["rpc_username"] = self.rPCUsernameLineEdit.text()
        data["rpc_password"] = self.rPCPasswordLineEdit.text()
        data["rpc_host"] = self.rPCHostLineEdit.text()
        data["rpc_port"] = self.rPCPortLineEdit.text()
        with open(python_src_dir / "settings/settings.json", "w") as outfile:
            json.dump(data, outfile, indent=4)
        self.update_RPCSettingsDialogue()


if __name__ == "__main__":
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
