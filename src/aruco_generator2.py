import numpy as np
import cv2
import os

# Caminho base onde as imagens serão salvas
base_dict = os.path.expanduser('~/lognav_ws/src/freedom_vehicle/models/arucos/materials/textures/')

# Dicionário de tipos de ArUco
ARUCO_DICT = {
    "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
    "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
    "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
    "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
    "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
    "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
    "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
    "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
    "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
    "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
    "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
    "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
    "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL
}

# Definições iniciais
aruco_type = "DICT_4X4_1000"  # Tipo de ArUco a ser gerado
id = 0  # ID inicial
tag_size = 1000  # Tamanho da marca
border_size = 200  # Tamanho da borda
total_image = tag_size + 2 * border_size  # Tamanho total da imagem

# Loop para gerar as imagens
for i in range(id, tag_size):
    # Usar cv2.aruco.getPredefinedDictionary() para obter o dicionário correto
    aruco_dict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[aruco_type])
    tag = np.ones((total_image, total_image), dtype="uint8") * 255  # Criar imagem branca com borda
    marker_area = np.zeros((tag_size, tag_size), dtype="uint8")  # Área do marcador
    cv2.aruco.generateImageMarker(aruco_dict, id, tag_size, marker_area, 1)  # Desenhar o marcador

    # Colocar o marcador no centro da imagem com borda
    bordered_tag = tag.copy()
    start_row = border_size
    end_row = start_row + tag_size
    start_col = border_size
    end_col = start_col + tag_size
    bordered_tag[start_row:end_row, start_col:end_col] = marker_area

    # Nome do arquivo da imagem
    tag_name = os.path.join(base_dict, f"{id}.png")
    print(f"Salvando imagem: {tag_name}")
    
    # Salvar a imagem
    cv2.imwrite(tag_name, bordered_tag)
    
    # Incrementar o ID
    id += 1

cv2.destroyAllWindows()
