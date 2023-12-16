from flask import Flask,jsonify,request,render_template
import pickle
app=Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=='POST':
        carat = request.form.get('carat')
        table = request.form.get('table')
        x = request.form.get('x')
        y = request.form.get('y')
        z = request.form.get('z')
        color_encoded = request.form.get('color_encoded')
        # Load the model from the file
        with open('model.pkl', 'rb') as model_file:
            mlmodel = pickle.load(model_file)
        pred = mlmodel.predict([[float(carat),float(table),float(x),float(y),float(z),float(color_encoded)]])
        return render_template('Success.html',data = {'Diamond Price':round(pred[0],2)})
    else:
        return render_template('prediction.html')
    
if __name__=="__main__":
    app.run()