from flask import Flask, request, render_template
from story import Story
from engine import current_story, start_story, get_response

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'GET':
        current_story.clear()
        start_story()
    if request.method == 'POST':
        player_input = request.form['player_input']
        current_story.add_line(player_input)
        current_story.add_line(get_response(player_input))
    return render_template('index.html', story=current_story.get_story())

if __name__ == '__main__':
    app.run()