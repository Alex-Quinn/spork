from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from story import Story

app = Flask(__name__)
app.config.from_object(__name__)

story = Story()

@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        story.add_line(request.form['player_input'])
    return render_template('index.html', story=story.get_story())

if __name__ == '__main__':
    app.run()