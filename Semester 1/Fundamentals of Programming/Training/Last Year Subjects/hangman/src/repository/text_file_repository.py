from src.repository.repository import Repository


class TextFileRepository(Repository):
    def __init__(self):
        super().__init__()
        self.__file_name = "D:\\_DOCUMENTE_RARES\\Desktop\\Semester 1\\Fundamentals of Programming\\Training\\Last Year Subjects\\hangman\\src\\sentences"
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                line = line.strip()
                try:
                    super().add(line)
                except ValueError:
                    continue

    def add(self, sentence):
        super().add(sentence)
        with open(self.__file_name, "a") as f:
            f.write(sentence + "\n")
