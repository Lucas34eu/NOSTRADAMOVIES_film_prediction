# NOSTRADAMOVIES (Film Prediction)
Bienvenue dans ce projet réalisé dans le cadre de ma formation à Epitech ! Notre objectif est de développer une IA capable de prédire le genre d'un film à partir de son affiche.
Voici les concepts utilisés pour mener à bien ce projet :

## OCR (Reconnaissance Optique de Caractères)
Nous avons mis en place un système sophistiqué de reconnaissance optique de caractères (OCR). Cette technologie nous permet d'extraire avec précision les informations textuelles cruciales telles que le titre du film, les noms des acteurs et des réalisateurs à partir des affiches de films.

![Nom de l'image](OCR/imgs/working_text_analyse.jpg)

## Face detection (Détection de Visages)
Dans cette partie de notre projet, nous avons intégré une fonctionnalité de détection faciale avancée. Pour parvenir à identifier les visages des acteurs sur l'affiche, nous nous appuyons sur une base de données de visages connus. Cette base de données contient des informations sur les visages d'acteurs populaires, ce qui nous permet de comparer les visages détectés sur l'affiche avec ceux de la base de données. En reconnaissant les visages des acteurs, nous pouvons ensuite déduire le genre du film en nous basant sur le genre des acteurs impliqués. Par exemple, si les visages reconnus appartiennent principalement à des acteurs connus pour jouer dans des films d'action, il est probable que le film soit également un film d'action. Cette approche nous permet d'exploiter les données sur les acteurs pour prédire le genre du film avec précision.

![Nom de l'image](Face_Detection/img/image_working.jpg)

## Colorimétrie
La colorimétrie joue un rôle crucial dans notre approche. Dans ce troisième paragraphe, nous examinons les schémas de couleurs utilisés dans l'affiche pour en déduire des informations sur le genre du film. Par exemple, les affiches de films d'horreur peuvent avoir des palettes de couleurs sombres et contrastées, tandis que les comédies peuvent utiliser des couleurs vives et des tons plus légers.

![Nom de l'image](Colorimetrie/color_analysis_report.png)

## Analyse de Texte
Enfin, dans le quatrième paragraphe, nous utilisons une analyse textuelle pour interpréter les éléments textuels restants sur l'affiche. Cela nous permet de détecter des mots-clés ou des phrases qui peuvent être associés à des genres spécifiques de films, tels que "action", "romance" ou "science-fiction".

![Nom de l'image](text_analyze/sentiment-result.png)

## Mise en relation de résultats
Dans notre projet, chaque étape est conçue pour fournir des informations précieuses qui alimentent un modèle d'intelligence artificielle global. La combinaison des résultats de la reconnaissance optique de caractères (OCR), de la détection faciale, de l'analyse colorimétrique et de l'analyse textuelle crée une vision holistique de l'affiche du film. En fusionnant ces données diverses, notre modèle peut établir des corrélations subtiles entre les éléments textuels, les visages d'acteurs reconnus et les schémas de couleurs, pour prédire avec une grande précision le genre du film. Cette approche intégrée garantit une analyse complète de l'affiche, tirant parti de chaque détail pour fournir des résultats plus fiables et précis.


