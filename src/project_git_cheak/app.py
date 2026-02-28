from flask import Flask

app = Flask(__name__)

def predict_price(area):
    return area * 5000

@app.route('/predict/<int:area>')
def predict(area):
    return {'area': area, 'predicted_price': predict_price(area)}

if __name__ == "__main__":
    app.run(debug=True)