from flask import Flask, render_template, request

# Create the Flask app
app = Flask(__name__, template_folder='templates')  # Adjust template_folder to 'templates'

@app.route('/', methods=['GET', 'POST'])
def hate():
    if request.method == 'POST':
        text = request.form['text']
        # Perform prediction using your model
        prediction = model.predict([text])
        return render_template('hate.html', prediction=prediction[0])
    return render_template('hate.html', prediction=None)


if __name__ == '__main__':
    app.run(debug=True)
