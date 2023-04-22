# run w/
# python fire_example.py multi_args asdf sdfg dfgh

import random
import fire

class Story(object):
    greetings = ["Hello", "Sup", "Hi"]

    def read(self, name):
        return f'Hello {name}!'

    def multi_args(self, *args):
        new_output = ''
        for arg in args:
            new_output += f'{random.choice(Story.greetings)} {arg}\n'
        return new_output

if __name__ == '__main__':
    fire.Fire(Story)

