class Parameter:
    def __init__(self, type, range=None, book=None):
        if type == "INT":
            start = range[0]
            end = range[1]
            print(f"start : {start} \n"
                  f"end : {end}")
        elif type == "STRING":
            print(book)

