from model import model, tokenizer
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/feedback', methods=['POST'])
def opinion_mining():
    data = request.get_json()
    text = data.get('text')

    # Tokenize and predict sentiment/opinion
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    outputs = model(**inputs)
    predictions = outputs.logits.softmax(dim=1).tolist()[0]

    # Format the response
    response = {
        'text': text,
        'disappointment': predictions[0],
        'sadness': predictions[1],
        'annoyance': predictions[2],
        'neutral': predictions[3],
        'disapproval': predictions[4],
        'realization': predictions[5],
        'nervousness': predictions[6],
        'approval': predictions[7],
        'joy': predictions[8],
        'anger': predictions[9],
        'embarrassment': predictions[10],
        'caring': predictions[11],
        'remorse': predictions[12],
        'disgust': predictions[13],
        'grief': predictions[14],
        'confusion': predictions[15],
        'relief': predictions[16],
        'desire': predictions[17],
        'admiration': predictions[18],
        'optimism': predictions[19],
        'fear': predictions[20],
        'love': predictions[21],
        'excitement': predictions[22],
        'curiosity': predictions[23],
        'amusement': predictions[24],
        'surprise': predictions[25],
        'gratitude': predictions[26],
        'pride': predictions[27],
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)