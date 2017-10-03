from flask import Flask, render_template, request
my_app = Flask(__name__)

@my_app.route('/')
def root():
    print request
    print my_app
    #print request.headers
    print request.args
    return render_template('forms.html')

@my_app.route('/hi/', methods=["GET", "POST"])
def hi():
    return render_template("hi.html", name = request.form["name"], reqMethod = request.method)

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
