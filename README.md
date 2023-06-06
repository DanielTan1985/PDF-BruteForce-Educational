PDF-BruteForce-Educational v1.0.0



This is a fairly simple localized Brute Force tool for decrypting PDF files that you might have forgotten the password for.

Dependencies
To run the program, make sure you have the necessary dependencies installed. If any dependencies are missing, you can install them using pip. Here are the steps:

Open your terminal or command prompt.
Run the following command to install the associated dependencies:
Copy code
pip install {associated_dependencies}
If you already have the dependencies installed but need to upgrade them, use the following command:
css
Copy code
pip install --upgrade {associated_dependencies}
Usage
The program provides two options for decryption: All Permutation or Potential Wordlist (suggestive).

All Permutation
If the password is fairly long (for example, 6 characters), the total number of permutations will be 586,236,072,240. Even at a speed of 1000 characters per second (depending on your computer's processing speed), it will take a while to try all the combinations.

Potential Wordlist (suggestive)
You can also provide your own potential wordlist. Simply place the wordlist file in the same folder as the program and load it into the graphical user interface (GUI). This allows you to use a customized list of passwords to attempt decryption.

Feel free to explore the program and decrypt your PDF files which you have lost the password with the provided options.
