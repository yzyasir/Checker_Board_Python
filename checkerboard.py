from flask import Flask, render_template  # added render_template!
app = Flask(__name__)

@app.route('/')
def game_checker():
    return render_template('checkerboard_index.html', rowoftimes = 4, columnoftimes = 4)
    
@app.route('/<numbertimes>')
def numstimes(numbertimes):
    x = int(numbertimes)//2
    return render_template('checkerboard_index.html', rowoftimes = x, columnoftimes = 4)

@app.route('/<numbertimes>/<columntimes>')
def columnstimes(numbertimes, columntimes):
    x = int(numbertimes)//2
    y = int(columntimes)//2
    return render_template('checkerboard_index.html', rowoftimes = x, columnoftimes = y)

if __name__=="__main__":
    app.run(debug=True)
# This is called the controller, where most logic is done, it will pass that logic into the html. Thats why I put the division into this file and not the html. Also // 