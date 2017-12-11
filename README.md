# DPD-Pakket-Bonnen-Voor-Labelprinter
DPD print 4 pakketbonnen op 1 A4 vel. 
Dit python script maakt daar 4 losse bonnen van, als jpg bestanden, zodat ze op een labelprinter uit te printen zijn.


Script en uitleg gebaseerd op 
https://glenbambrick.com/2017/01/10/pdf-to-jpg-conversion-with-python-for-windows/

# Installatie instructies

1. Installeer Python 3.x vanaf https://www.python.org/
# let op!
Voeg python toe aan je PATH (hokje aanvinken tijdens setup, als je dit vergeet kan je dit later handmatig doen)

2. Installeer ImageMagick van https://www.imagemagick.org/script/download.php
Huidige (dec 2017) laatste versie voor Windows 10 x64 is
https://www.imagemagick.org/download/binaries/ImageMagick-7.0.7-14-Q16-x64-dll.exe

# let op!
zorg dat Install development headers and libraries for C and C++ aangevinkt is.

3. Voeg ImageMagick to aan PATH
Ga naar de map waar ImageMagick geinstalleerd is (bijvoorbeeld  C:\Program Files\ImageMagick-7.0.7-14-Q16) en kopieer de adresbalk.
Klik op de Windows Start knop, typ *omgevingsvariabelen* (of als je Windows Engels is  'Path' en klik op het  zoekresultaat (is er maar 1). Klik op de Omgevingsvariabelen/ Environment Variables knop, dan User variables voor gebruikersnaam en op Path in de tabel daaronder klikken, en dan op Edit.  Dan Nieuw om een regel aan het Path toe te voegen. Plak hier het pad naar ImageMagick.

4. Even controleren of ImageMagick goed geinstalleerd is.
Willekeurige PDF in willekeurige map.
Command Prompt openen, 
> cd naar de map waar je net de pdf in gestopt hebt
>magick filenaam.pdf filenaam.jpg

Hij moet nu een jpg van de PDF gemaakt hebben. (De kwaliteit hiervan is wat beroerd nog, dit is in het python script opgelost).

5.
Maak een map aan waar je de DPD PDFs in op wilt slaan.
Zet die map als pdf_dir in dpd.py
(als je alles op de Desktop zet in een map die 'pdf' heet hoef je alleen de Username te veranderen).

Het bestand dpd.py in dezelfde pdf map zetten.
Dubbelklik op dpd.py en hij moet werken, en alle PDFs in de map in 4 stukjes hakken.

Als hij vraagt waar je het dpd.py bestand mee wilt openen, rechtsklikken op dpd.py, klik Eigenschappen, en voor openen met navigeer naar de python.exe  (waarschijnlijk C:\Program Files\Python36-32\,  of ergens in  C:\User\AppData\Local\ProgramFile0s\Python36-32)
Klik op python.exe om alle .py bestanden met python te openen.

(je kan de time.sleep() regels uit de code halen als je het zo snel mogelijk wilt hebben en niet hoeft te 'zien' wat hij doet, zoals het er in staat wacht hij na elk PDF bestand 1 seconde, en geeft hij 4 seconden het "ALLES IS KLAAR" bericht weer voor hij sluit).
