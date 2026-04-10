from flask import Flask,render_template,request
import pickle
from feature_extraction import extract_features

app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))

@app.route("/",methods=["GET","POST"])
def index():
    result=""
    if request.method=="POST":
        url=request.form["url"]
        features=extract_features(url)
        pred=model.predict([features])
        result="Phishing 🚨" if pred[0]==1 else "Safe ✅"
    return render_template("index.html",result=result)

if __name__=="__main__":
    app.run(debug=True)
