from flask import Flask,request,render_template
import regression as reg

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])

def regression():
    if request.method == "GET":
        regre=reg.regression_test()
        r=regre
        
        return render_template("index.html",regression_result=r)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)