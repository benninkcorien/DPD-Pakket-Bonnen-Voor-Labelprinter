# DPD print 4 shipping labels op 1 pagina.
# dit script maakt daar 4 individuele labels van zodat ze uit te printen zijn met een labelprinter.

import os
# die hieronder kan weg
import time

pdf_dir = r"C:\Users\Username\Desktop\pdf"
pdf_files =  [pdf_file for pdf_file in os.listdir(pdf_dir) if pdf_file.endswith(".pdf")]

for pdf in pdf_files:

	input_pdf = pdf_dir + "\\" + pdf
	output_jpg =  pdf +".jpg"
	# command to convert files via imagemagick < v7 is convert input.pdf output.jpg
	# density is DPI, quality is JPG quality
	command = "magick -density 300 " + input_pdf + " -quality 100 " + output_jpg
	# use os.system to send that command..
	os.system(command)

	new_jpg = output_jpg
	cutinto4 = "magick " + new_jpg + " -crop 2x2-40-20@ +repage +adjoin " + new_jpg + "bon-%d.jpg"
	print(cutinto4)
	os.system(cutinto4)
  # de time hieronder kan weg
	time.sleep(1)	

print("ALLES IS KLAAR")
# de time hieronder kan weg
time.sleep(4)
