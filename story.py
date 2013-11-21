from collections import deque

class Story:
    """Holds current story"""
    def __init__(self):
        self.lines = deque(['Welcome to the internet.'], maxlen=25)

    def add_line(self, line):
        self.lines.append(line)

    def get_story(self):
        return self.lines

    def clear(self):
        self.lines.clear()
        self.lines.append('Welcome to the internet.')

    def __str__(self):
        output = ''
        for line in self.lines:
            output += line + '\n'
        return output