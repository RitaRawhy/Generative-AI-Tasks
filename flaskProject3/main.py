from flask import Flask, render_template, request
app = Flask(__name__)

import google.generativeai as palm
palm.configure(api_key="AIzaSyAdcaDwtJXYe7I3or5TppF2GQ2fapPoX9w")

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

num_examples = 0
training_data = []
Prof_Answers = []
stud_Answers = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/student', methods=['POST'])
def train():
    global num_examples
    num_examples += int(request.form['num_examples'])

    # Collect training inputs and outputs
    Questions = [request.form[f'train_input_{i}'] for i in range(1, num_examples + 1)]

    for i in range(1, num_examples + 1):
        Prof_Answers.append([request.form[f'train_output_{i}']])

    return render_template('test.html', num_examples=num_examples, Questions=Questions)


@app.route('/compare', methods=['POST'])
def test():
    for i in range(0, num_examples):
        stud_Answers.append([request.form[f'train_output_{i}']])

    # Store training data in a list
    for profAns, studAns in zip(Prof_Answers, stud_Answers):
        training_data.append({'profAns': profAns, 'studAns': studAns})

    OverAllScore = len(training_data) * 2
    TotalStudScore = 0

    for item in training_data:
        prompt = f"Text 1: {item['profAns']} \n Text 2: {item['studAns']}   \n Do the two texts have the same meaning \n"
        response = palm.generate_text(
            **defaults,
            prompt=prompt
        )
        Ques_score = 0  # Default score if no similarity indication is found
        similarity_text = response.result.lower()
        if 'yes' in similarity_text:
            Ques_score += 2
        elif 'no' in similarity_text:
            Ques_score += 0

        TotalStudScore += Ques_score

    return render_template('result.html', TotalStudScore=TotalStudScore, OverAllScore=OverAllScore)

if __name__ == '__main__':
    app.run()
