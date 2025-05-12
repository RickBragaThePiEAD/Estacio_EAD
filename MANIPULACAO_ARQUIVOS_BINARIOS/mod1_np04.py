from PIL import Image
import numpy as np

def main():
    # Carregar a imagem original
    img = Image.open('/workspaces/Estacio_EAD/MANIPULACAO_ARQUIVOS_BINARIOS/simple_icon.png')
    img.show()

    # Converter a imagem em dados binários
    img_data = np.array(img)
    binary_data = img_data.tobytes()

    #Salvar os dados binários em um arquivo
    with open('Original_img.bin', 'wb') as file:
        file.write(binary_data)
    
    #Copiar o arquivo binário
    with open('Original_img.bin', 'rb') as Original_file:
        binary_data = Original_file.read()
    
    with open('Copy_img.bin', 'wb') as Copy_file:
        Copy_file.write(binary_data)

    #Manipulaçao dos dados dos arquivos binários cópia
    #Exemplo: inverter os bytes
    with open('Copy_img.bin', 'rb') as file:
        data = bytearray(file.read())

    # Inverter os bytes
    data = data[::-1]

    with open('Copy_img.bin', 'wb') as file:
        file.write(data)
    
    #Carregar e mostrar a imagem manipulada
    modified_img_data = np.frombuffer(binary_data, dtype=np.uint8).reshape(img_data.shape)
    modified_img = Image.fromarray(modified_img_data)
    modified_img.show()

if __name__ == "__main__":
    main()