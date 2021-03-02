# pip install pyqrcode

import pyqrcode

# Digite o link
link1 = input("Digite o link: ")

# Criando o Qrcode
url = pyqrcode.create(link1)
# Informando formato/tamanho
url.svg('gabrielGitHub-url.svg', scale=8)
url.eps('gabrielGitHub-url.eps', scale=2)
# Imprimindo
print(url.terminal(quiet_zone=1))