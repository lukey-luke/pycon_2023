import pickle

class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

def pickle_in_3_11():
    d = Dog('Fido')
    d.add_trick('roll over')
    pickle.dump(d, open('dog_pickeled_in_3_11.pkl', 'wb'))

def unpickle_in_2_7():
    """
    Traceback (most recent call last):
      File "main.py", line 23, in <module>
        unpickle_in_2_7()
      File "main.py", line 17, in unpickle_in_2_7
        d = pickle.load(open('dog_pickeled_in_3_11.pkl', 'rb'))
      File "/Users/verdanceluke/.pyenv/versions/2.7.18/lib/python2.7/pickle.py", line 1384, in load
        return Unpickler(file).load()
      File "/Users/verdanceluke/.pyenv/versions/2.7.18/lib/python2.7/pickle.py", line 864, in load
        dispatch[key](self)
      File "/Users/verdanceluke/.pyenv/versions/2.7.18/lib/python2.7/pickle.py", line 892, in load_proto
        raise ValueError, "unsupported pickle protocol: %d" % proto
    ValueError: unsupported pickle protocol: 4
    """
    d = pickle.load(open('dog_pickeled_in_3_11.pkl', 'rb'))
    print(d.name)
    print(d.tricks)

if __name__ == '__main__':
    # pickle_in_3_11()
    unpickle_in_2_7()
