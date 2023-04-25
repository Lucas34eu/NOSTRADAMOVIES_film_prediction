from paddleocr import PaddleOCR

# Instanciation de PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Chemin de l'image à traiter
img_path = 'imgs_en/tt5022418.jpg'

# Traitement de l'image avec PaddleOCR
result = ocr.ocr(img_path, cls=True)

# Parcours des résultats et écriture dans un fichier texte
with open('resultats.txt', 'w') as f:
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            #f.write(line[0] + '\n')
            print(line[0])
