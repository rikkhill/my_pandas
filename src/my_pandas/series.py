

class Series:

    def __init__(self, collection):

        # Tonnes of checks to identify the nature of the collection go here

        self.values = collection

        # Eventually the index will be its own all-singing, all-dancing object
        self.index = list(range(1, len(collection) + 1))

    def __getitem__(self, item):

        try:
            return self.values[self.index.index(item)]

        except (KeyError, IndexError):
            pass




