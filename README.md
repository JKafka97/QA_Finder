# QA_Finder

Sharing is nice

#!/usr/bin/python3

# python3 -m venv venv
# venv/bin/activate
# pip install pdftotext
# pip freeze > requirements.txt

## If you want to try my project:
# Clone this repository
# Create venv
# venv/bin/activate
# pip install -r requirements.txt
# run: ./main.py


import sys
import pdftotext  # pip install pdftotext
from pathlib import Path  # super knihovna na cesty

## --------- sys.args info (pokrocila je pak 'argparse')
# filename ... sys.args[0] = 'filename'
# filename A ... sys.args[0] = 'filename', sys.args[1] = A
# filename A B ... len(sys.args) = 3
#

## -------- Path info
# cd /home/jverner/TEST
# /home/jverner/TEST/data/faktury.txt
# PWD ... curdir = Path('.')  # PWD bude tam, kde spouštím skript
# SCRIPTDIR ... scriptdir = Path(__file__)  # SCRIPTDIR bude tam, kde je main.py
# FAKTURY ... faktury = cudrid / 'data' / 'faktury.txt'
# vytisknout: https://pbpython.com/pathlib-intro.html
# nejpouzivanejsi: faktury.name, faktury.stem, faktury.suffix, faktury.parrent, faktury.resolve() (misto absolute())


def main():
	"""
Usage: qa_finder SOURCE TARGET

Where:
	SOURCE: Excel file
    TARGET: Word/PDF file
"""
    pass
	# Přes sys.args načíst SOURCE a TARGET
    # Nezapomenout na případ, kdy SOURCE nebo TARGET není definován
    # Zkontrolovat SOURCE končí na xls/xlsx/xlsb/xlsm, TARGET pdf/doc/docx
	
    # Načíst SOURCE do paměti ... string object
    # Načíst TARGET (zatím nvm)
    
    # Printnout vnitřek SOURCE, TARGET
  
if __name__ == '__main__':
    main()
