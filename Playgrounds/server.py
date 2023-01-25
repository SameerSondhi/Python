from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/')                           
def boxes():
    return render_template('index.html', color = "coral", times=3)  

@app.route('/play/<times>')                           
def many_boxes(times):
    return render_template('index.html', color = "coral", times = int(times))  

@app.route('/play/<times>/<color>')                           
def colorful_boxes(times, color):
    return render_template('index.html', color = color,  times = int(times))  
    
if __name__=="__main__":
    app.run(debug=True) 