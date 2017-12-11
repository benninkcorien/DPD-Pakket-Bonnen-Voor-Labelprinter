# DPD-Pakket-Bonnen-Voor-Labelprinter
DPD print 4 pakketbonnen op 1 A4 vel. 
Dit python script maakt daar 4 losse bonnen van zodat ze 1 voor 1 op een labelprinter uit te printen zijn.

Script gebaseerd op 
https://glenbambrick.com/2017/01/10/pdf-to-jpg-conversion-with-python-for-windows/

# Installatie instructies

1. Installeer Python 3.x vanaf https://www.python.org/

2. Installeer ImageMagick van https://www.imagemagick.org/script/download.php
Huidige (dec 2017) laatste versie voor Windows 10 x64 is
https://www.imagemagick.org/download/binaries/ImageMagick-7.0.7-14-Q16-x64-dll.exe

# let op!
zorg dat Install development headers and libraries for C and C++ aangevinkt is.

3. Voeg ImageMagick to aan PATH
Windows Start knop, typ 'omgevingsvariabelen (of Path als je Windows Engels is)'  
(Advanced System Settings > Environment Variables) 
Dan de omgevingsvariabelen knop, en dan User variables voor gebruikersnaam, op Path in de tabel daaronder klikken en dan op Edit, Dan New om een toe te voegen, en dan moet je het pad naar imageMagick daar in plakken (bijvoorbeeld  C:\Program Files\ImageMagick-7.0.7-14-Q16)

4. Even controleren of ImageMagick goed geinstalleerd is.
Willekeurige PDF in willekeurige map.
Command Prompt openen, 
> cd naar de map waar je net de pdf in gestopt hebt
>convert filenaam.pdf filenaam.jpg

Hij moet nog een jpg gemaakt hebben. (de kwaliteit hiervan is wat beroerd nog).

5.
Maak een map aan waar je de DPD PDFs in op wilt slaan.
Zet die map als pdf_dir in dpd.py
(als je hem op de Desktop zet in een map die 'pdf' heet hoef je alleen de Username te veranderen).

Deze dpd.py in dezelfde pdf map zetten.
Dubbelklikken en hij moet werken, en alle PDFs in de map in 4 stukjes hakken.
(je kan de time.sleep() regels uit de code halen als je het zo snel mogelijk wilt hebben en niet hoeft te 'zien' wat hij doet).
