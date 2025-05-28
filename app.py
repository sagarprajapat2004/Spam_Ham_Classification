from flask import Flask, render_template, request, redirect, url_for, session
import pickle
from text_transformer import txt_transformer

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/", methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        vectorizer = pickle.load(open('./models/vectorizer.pkl', 'rb'))
        ml_model = pickle.load(open('./models/model.pkl', 'rb'))
        message = request.form.get('message')
        message = txt_transformer(message)
        vector = vectorizer.transform([message])
        prediction = ml_model.predict(vector)[0]
        session['prediction'] = int(prediction)
        return redirect(url_for('predict'))

    p = session.pop('prediction', None)
    return render_template('index.html', p=p)

if __name__ == "__main__":
    app.run()