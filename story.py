from collections import deque

class Story:
    """Holds current story"""
    def __init__(self):
        self.lines = deque(['Welcome to the internet...'], maxlen=50)

    def add_line(self, line):
        self.lines.append([line])

    def get_story(self):
        return self.lines