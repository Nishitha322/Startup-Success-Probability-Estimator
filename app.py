from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    experience = int(request.form['experience'])
    funding = int(request.form['funding'])
    team_size = int(request.form['team_size'])

    probability = (experience * 0.3 + funding * 0.4 + team_size * 0.3)
    if probability > 100:
        probability = 100

    return render_template('result.html', probability=round(probability, 2))

# ✅ THIS PART IS IMPORTANT TO RUN THE APP
if __name__ == '__main__':
    app.run(debug=True)

    