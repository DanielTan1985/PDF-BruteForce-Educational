PDF-BruteForce-Educational v1.0.0 (Python)

![Image00](https://github.com/DanielTan1985/PDF-BruteForce-Educational/blob/main/Image00.jpg?raw=true)

This is a fairly simple localized Brute Force tool for decrypting PDF files that you might have forgotten the password for.

For ease of use, you may just run [Application] in the folder which is compile via cx_Freeze and Dependencies as below

import tkinter as tk <br>
from tkinter import ttk, scrolledtext<br>
from tkinter import *<br>
from tkinter.filedialog import askopenfilename<br>
import itertools<br>
import string<br>
import pikepdf<br>
from tqdm import tqdm<br>
import os<br>


Dependencies
To run the program, make sure you have the necessary dependencies installed. If any dependencies are missing, you can install them using pip. Here are the steps:

-> Open your terminal or command prompt.
Run the following command to install the associated dependencies:
pip install {associated_dependencies}

If you already have the dependencies installed but need to upgrade them, use the following command:
pip install --upgrade {associated_dependencies}

Usage
The program provides two options for decryption: All Permutation or Potential Wordlist (suggestive).

All Permutation
If the password is fairly long (for example, 6 characters), the total number of permutations will be 586,236,072,240. Even at a speed of 1000 characters per second (depending on your computer's processing speed), it will take a while to try all the combinations.

Potential Wordlist (suggestive)
You can also provide your own potential wordlist. Simply place the wordlist file in the same folder as the program and load it into the graphical user interface (GUI). This allows you to use a customized list of passwords to attempt decryption.

Feel free to explore the program and decrypt your PDF files which you have lost the password with the provided options.
