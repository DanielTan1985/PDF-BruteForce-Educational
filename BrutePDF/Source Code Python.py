import tkinter as tk 
from tkinter import ttk, scrolledtext
from tkinter import *
from tkinter.filedialog import askopenfilename
import itertools
import string
import pikepdf
from tqdm import tqdm
import os, sys



class CustomException(Exception):
    pass

class GUI:
    def __init__(self):
        self._root = tk.Tk()
        self._root.title('Daniel - Educational PDF Brute Force')
        self._stop = False
        self.create_widgets()
        self._root.mainloop()
        

    def joinStr(self, tup):
        joined_strings = []
        for i in tup:
            joined_strings.append("".join(i))
        joined_result = ' & '.join(joined_strings)
        self.writeToScrollText(joined_result)
        joined_strings = []

    def on_brute_type_change(self, *args):
        if self.brute_type.get() == "0":
            self._numChars.config(state=NORMAL)
            self._openFile2.config(state=tk.DISABLED)
        else:
            self._numChars.config(state=DISABLED)
            self._openFile2.config(state=NORMAL)



    def start(self):
        fileName = str(self._lblFileName['text'])
        wordList = str(self._lblPwPhrase['text'])
        brute_type = int(self.brute_type.get())
        try:
            wordLists = [ line.strip() for line in open(wordList) ]
        except FileNotFoundError:
            self.writeToScrollText('wordlist.txt not found in current directory')
            return

        if brute_type == 1:
            for _ in tqdm(wordLists, "Decrypting PDF"):
                self.progress["value"] += 1
                self.progress["value"] = 0 if self.progress["value"] >= 5000 else self.progress["value"] + 1
                self._root.update_idletasks()

                try:
                    with pikepdf.open(fileName, password=_) as pdf:
                        self.writeToScrollText(f"[+] Password found: {_}")
                        output_filename = "decrypted"
                        output_ext = ".pdf"
                        if os.path.exists(output_filename + output_ext):
                            i = 1
                            while True:
                                new_filename = output_filename + str(i)
                                if not os.path.exists(new_filename + output_ext):
                                    output_filename = new_filename
                                    break
                                i += 1
                        else:
                            i = ""
                        pdf.save(output_filename + output_ext)
                        self.writeToScrollText(f"file saved as {output_filename}{output_ext}")
                        break
                except pikepdf._core.PasswordError as e:
                    continue

            else:
                self.clearScroll()
                self.progress["value"] = 5000
                self.writeToScrollText(f"Failed to decrypt file")
                self.writeToScrollText(f"Please try again with a more comprehensive word list")


        else:
            numChars = int(self.numChars.get())
            char_type = int(self.char_type.get())
            if char_type == 0:
                chars = string.ascii_letters + string.digits + string.punctuation
            elif char_type == 1:
                chars = string.ascii_letters
            elif char_type == 2:
                chars = string.digits
            elif char_type == 3:
                chars = string.punctuation
            else:
                raise CustomException("Invalid character type")

            for guess in tqdm(itertools.product(chars, repeat=numChars), "Decrypting PDF"):
                self.progress["value"] = 0 if self.progress["value"] >= 4999 else self.progress["value"] + 1
                self.joinStr(guess)
                self._root.update_idletasks()
                if self._stop:
                    self.clearScroll()
                    self.writeToScrollText('Program stopped')
                    break
                #self.writeToScrollText(self.progress["value"])
                try:
                    with pikepdf.open(fileName, password="".join(guess)) as pdf:
                        self.writeToScrollText(f"[+] Password found: {''.join(guess)}")
                        output_filename = "decrypted"
                        output_ext = ".pdf"
                        if os.path.exists(output_filename + output_ext):
                            i = 1
                            while True:
                                new_filename = output_filename + str(i)
                                if not os.path.exists(new_filename + output_ext):
                                    output_filename = new_filename
                                    break
                                i += 1
                        else:
                            i = ""
                        pdf.save(output_filename + output_ext)
                        self.writeToScrollText(f"file saved as {output_filename}{output_ext}")


                        break
                except pikepdf._core.PasswordError as e:
                    continue
            else:
                self.clearScroll()
                self.writeToScrollText(f"failed to decrypt file")


    def stop(self):
        self._stop = True
        sys.exit()

    def clearScroll(self):
        self.output.config(state=NORMAL)
        self.output.delete('1.0', END)
        self.output.config(state=DISABLED)

    def clearAll(self):
        self.progress["value"] = 0
        self.output.config(state=NORMAL)
        self.output.delete('1.0', END)
        self.output.config(state=DISABLED)
        self._numChars.delete(0, 'end')
        self.char_type.set(0)
        self._lblFileName.config(text="Please have the .pdf in same folder and select file to start")
        self._lblPwPhrase.config(text="Password Phrase .txt in same folder and select to start")
    
    def writeToScrollText(self, message):
        self.output.config(state=NORMAL)
        self.output.insert('end', f'{message}'+'\n')
        self.output.see('end')
        self.output.config(state=DISABLED)

    def open_file(self,arg):
        filename = askopenfilename()
        if arg == self._lblFileName:
            self._lblFileName['text'] = filename.split('/')[-1]
        else:
            self._lblPwPhrase['text'] = filename.split('/')[-1]

        

    def create_widgets(self):

        layer1frame = ttk.Frame(self._root)
        layer1frame.grid(row=0, column=0, sticky="W", padx=10, pady=10)
        self._openFile = tk.Button(layer1frame, text="Open File to Decrypt")
        self._openFile['command'] = lambda: self.open_file(self._lblFileName)
        self._openFile.grid(row=0, column=0, sticky="W", padx=10, pady=10)
        self._lblFileName = ttk.Label(layer1frame, text="Please have the .pdf in same folder and select file to start")
        self._lblFileName.grid(row=0, column=1, sticky="W", padx=10, pady=0)

        layer2frame = ttk.Frame(self._root)
        layer2frame.grid(row=1, column=0, sticky="W", padx=10, pady=10)
        self._openFile2 = tk.Button(layer2frame, text="   Open Pw List .txt   ")
        self._openFile2['command'] = lambda: self.open_file(self._lblPwPhrase)
        self._openFile2.grid(row=0, column=0, sticky="W", padx=10, pady=10)
        self._lblPwPhrase = ttk.Label(layer2frame, text="Password Phrase .txt in same folder and select to start")
        self._lblPwPhrase .grid(row=0, column=1, sticky="W", padx=10, pady=0)

        layer3frame = ttk.Frame(self._root)
        layer3frame.grid(row=2, column=0, sticky="W", padx=10, pady=10)
        self._lblFileName2 = ttk.Label(layer3frame, text="Brute Force Type:")
        self._lblFileName2.grid(row=0, column=0, sticky="W", padx=10, pady=0)
        self.brute_type = StringVar()
        tk.Radiobutton(layer3frame , text="All Permutation", variable=self.brute_type, value=0).grid(row=0, column=1, padx=23, pady=10)
        tk.Radiobutton(layer3frame , text="Potential word list", variable=self.brute_type, value=1).grid(row=0, column=2, padx=30, pady=10)
        self.brute_type.set(1)
        self.brute_type.trace("w", self.on_brute_type_change)

        layer4frame = ttk.Frame(self._root)
        layer4frame.grid(row=3, column=0, sticky="W", padx=10, pady=0)
        self._lblNumChars = ttk.Label(layer4frame, text="Number of characters:")
        self._lblNumChars.grid(row=0, column=0, sticky="W", padx=10, pady=0)
        self.numChars = IntVar()
        self._numChars = tk.Entry(layer4frame, width=20, textvariable=self.numChars)
        self._numChars.grid(row=0, column=1, sticky="W")
        self._numChars.delete(0, 'end')
        self._numChars.config(state=DISABLED)

        layer5frame = ttk.Frame(self._root)
        layer5frame.grid(row=4, column=0, sticky="W", padx=10, pady=10)
        self._lblFileName2 = ttk.Label(layer5frame, text="Type of Language set:")
        self._lblFileName2.grid(row=0, column=0, sticky="W", padx=10, pady=0)
        self.char_type = StringVar()
        tk.Radiobutton(layer5frame , text="All        ", variable=self.char_type, value=0).grid(row=0, column=1, padx=0, pady=10)
        tk.Radiobutton(layer5frame , text="ASCII      ", variable=self.char_type, value=1).grid(row=0, column=2, padx=30, pady=10)
        tk.Radiobutton(layer5frame , text="Digits     ", variable=self.char_type, value=2).grid(row=0, column=3, padx=30, pady=10)
        tk.Radiobutton(layer5frame , text="Punctuation", variable=self.char_type, value=3).grid(row=0, column=4, padx=30, pady=10)
        self.char_type.set(0)

        layer6frame = ttk.Frame(self._root)
        layer6frame.grid(row=5, column=0, columnspan=2)
        ttk.Button(layer6frame, text="Start",command=self.start).grid(row=0, column=1, padx=30, pady=10)
        self.stop_button = ttk.Button(layer6frame, text="Stop", command=self.stop)
        self.stop_button.grid(row=0, column=2, padx=30, pady=10)
        self.stop_button.bind("<Button-1>", self.stop)
        ttk.Button(layer6frame, text="ClearAll",command = self.clearAll).grid(row=0, column=3, padx=30, pady=10)

        layer7frame = ttk.Frame(self._root)
        layer7frame.grid(row=6, column=0, columnspan=2, sticky="W")
        self.progress = ttk.Progressbar(layer7frame, length=610)
        self.progress["maximum"] = 5000
        self.progress["value"] = 0
        self.progress["variable"] = 0
        self.progress.grid(row=0, column=1, sticky="W", padx=20, pady=20)


        self.output = scrolledtext.ScrolledText(self._root, width=80, height=18)
        self.output.config(state=tk.DISABLED)
        self.output.grid(row=7, column=0, columnspan=10, sticky="W")
        self.output.focus()


if __name__ == "__main__":
    GUI()

