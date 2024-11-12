from flask import Flask, render_template, request

app = Flask(__name__)

import google.generativeai as palm
palm.configure(api_key="AIzaSyAo8hC7SLuSYlVZKD83iNe1rbO22a2e_C0")

# Default settings
defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024
}

@app.route('/', methods=['GET', 'POST'])


def index():
    response_text = ""

    if request.method == 'POST':
        # Get the prompt from the submitted form
        prompt = request.form['prompt']

        # Generate a response based on the entered prompt
        response = palm.generate_text(**defaults, prompt=prompt)
        response_text = response.result

    return render_template("index.html", response_text=response_text)

if __name__ == '__main__':
    app.run(debug=True)
