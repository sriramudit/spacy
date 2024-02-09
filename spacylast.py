from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

# Load your spaCy model
nlp = spacy.load("model-best")

@app.route('/api/annotate', methods=['POST'])
def annotate_text():
    try:
        data = request.json
        text = data['text']

        # Process the text with the spaCy model
        doc = nlp(text)

        # Extract relevant information from the spaCy Doc object
        entities = [{'start': ent.start_char, 'end': ent.end_char, 'label': ent.label_}
                    for ent in doc.ents]

        response = {'entities': entities}
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
