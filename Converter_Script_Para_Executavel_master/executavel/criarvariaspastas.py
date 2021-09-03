import os
#  no terminal usar pyinstaller onefile --noconsole caminho do seu arquivo
# na sua pasta desse arquivo tem uma pasta chamada dist e estara lá o executavel

class FileGenerator:
    def __init__(self):
        pass

    def Start(self):
        self.make_initial_folders()
        self.create_files_per_folders()

    def make_initial_folders(self):
        os.mkdir('Number 1')
        os.mkdir('Number 2')
        os.mkdir('Number 3')
        os.mkdir('Number 4')

    def create_files_per_folders(self):
        base_directory = os.getcwd()
        os.chdir('Number 1')
        with open('text_file.txt', 'w') as file:
            file.write('Hello Pythonista')
            pass

        os.chdir(base_directory)
        os.chdir('Number 2')
        with open('text_file.txt', 'w') as file:
            file.write('oi eu sou goku')
            pass

        os.chdir(base_directory)
        os.chdir('Number 3')
        with open('text_file.txt', 'w') as file:
            file.write('nani')
            pass

        os.chdir(base_directory)
        os.chdir('Number 4')
        with open('text_file.txt', 'w') as file:
            file.write('Inevitavel')
            pass


generator = FileGenerator()
generator.Start()