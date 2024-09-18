from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/')
def home():
    prompts = story.prompts
    return render_template("form.html", prompts=prompts)

@app.route('/story')
def show_story():
    answers = {prompt: request.args.get(prompt) for prompt in story.prompts}
    result_story = story.generate(answers)
    return render_template("story.html", story=result_story)

if __name__ == '__main__':
    app.run(debug=True)
