from param import Parameter


class DatasetGenerator:
    def __init__(self, filename, nb_lignes, *params):
        self.filename = filename
        self.create_file()
        while range(nb_lignes):
            with open(filename, "w") as file:
                for param in params:
                    if isinstance(param, Parameter):


    def create_file(self):
        with open(self.filename, "x") as file:
            file.close()
        pass
