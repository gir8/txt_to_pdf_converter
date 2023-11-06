#!/usr/bin/env python3
"""A program to convert a file with a txt extension to PDF"""

from fpdf import FPDF
from os import strerror

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        # setup
        self.path = None
        self.file = None
        self.add_page()
        self.set_font("Times", size=12)

        # file read and write
        self.open_txtfile()
        self.create_pdf()

    def open_txtfile(self):
        # source file
        self.path = input("Input the .txt file path without the file extension (ex. - C:\\Users\\account\\OneDrive\\Desktop\\resume):  ")
        try:
            self.file = open(self.path + ".txt", mode="rt")
        except Exception as e:
            print("The file could not be opened:  ", strerror(e.errno))

    def create_pdf(self):
        # read and write
        try:
            words = self.file.readline().replace("\t", "        ")
            while words != "":
                line_counter = 0
                line = ""
                word = ""
                for character in words:
                    if len(line + word) < 107:
                        if character.isspace():
                            line += (word + character)
                            word = ""
                        else:
                            word += character
                    else:
                        if character.isspace():
                            line_counter += 1
                            self.cell(250, 7, txt=line, ln=line_counter, align="left")
                            if word != "":
                                line = word + character
                                word = ""
                            else:
                                line = ""
                        else:
                            word += character
                if len(line + word) < 107:
                    line_counter += 1
                    line += word
                    self.cell(250, 7, txt=line, ln=line_counter, align="left")
                else:
                    line_counter += 1
                    self.cell(250, 7, txt=line, ln=line_counter, align="left")
                    line_counter += 1
                    self.cell(250, 7, txt=word, ln=line_counter, align="left")
                words = self.file.readline().replace("\t", "        ")
            self.file.close()
            self.output(self.path + ".pdf")
        except IOError as e:
            print("I/O error occured:  ", strerror(e.errno))

if __name__ == "__main__":
    pdf = PDF()
