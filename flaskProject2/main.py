from flask import Flask, render_template, request

app = Flask(__name__)

import google.generativeai as palm
palm.configure(api_key="AIzaSyAKnWwc0R1eamUpSTTT_LKkB34E9K-Yl90")

defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.7,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024,
    'stop_sequences': [],
    'safety_settings': [
        {"category": "HARM_CATEGORY_DEROGATORY", "threshold": 1},
        {"category": "HARM_CATEGORY_TOXICITY", "threshold": 1},
        {"category": "HARM_CATEGORY_VIOLENCE", "threshold": 2},
        {"category": "HARM_CATEGORY_SEXUAL", "threshold": 2},
        {"category": "HARM_CATEGORY_MEDICAL", "threshold": 2},
        {"category": "HARM_CATEGORY_DANGEROUS", "threshold": 2},
    ],
}

training_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train():
    num_examples = int(request.form['num_examples'])

    # Collect training inputs and outputs
    training_inputs = [request.form[f'train_input_{i}'] for i in range(1, num_examples + 1)]
    training_outputs = [request.form[f'train_output_{i}'] for i in range(1, num_examples + 1)]

    # Store training data in a list
    for input_text, output_text in zip(training_inputs, training_outputs):
        training_data.append({'input': input_text, 'output': output_text})

    training_result = f"Model trained with {num_examples} training examples."
    return render_template('index.html', training_result=training_result)

@app.route('/test', methods=['POST'])
def test():
    test_input = request.form['test_input']

    # Combine training data with the current test input
    prompt = '\n'.join(f"input: {data['input']}\noutput: {data['output']}" for data in training_data)
    prompt += f"\ninput: {test_input}\noutput:"

    # Generate response
    response = palm.generate_text(**defaults, prompt=prompt)
    generated_response = response.result

    return render_template('index.html', test_input=test_input, generated_response=generated_response)

if __name__ == '__main__':
    app.run(debug=True)