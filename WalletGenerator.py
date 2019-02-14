import blocksmith
import qrcode
from qrcode.image.pure import PymagingImage

from ethereumwalletgenerator_ui import *
key = "0x"
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.pushButton.setText("Generate Private Key")
        self.pushButton_2.setText("Generate Public Key")
        #self.label.setText("Your Ethereum Address:")


        self.pushButton.clicked.connect(self.generatePrivateKey)
        self.pushButton_2.clicked.connect(self.generatePublicKey)

    def generatePrivateKey(self):    
        global key   
        kg = blocksmith.KeyGenerator()
        kg.seed_input('Seeds words to generate random input')
        key = kg.generate_key()
        print(key)
        self.label.setText("Your Ethereum Address: ")


    def generatePublicKey(self):
        address = blocksmith.EthereumWallet.generate_address(key)
        checksum_address = blocksmith.EthereumWallet.checksum_address(address)
        print(checksum_address)
        self.label.setText("Your Ethereum Address: " + checksum_address)










if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()



