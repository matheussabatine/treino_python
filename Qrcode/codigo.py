import qrcode

imagem_qrcode = qrcode.make("https://github.com/matheussabatine")
imagem_qrcode.save("meu_perfil.png")

