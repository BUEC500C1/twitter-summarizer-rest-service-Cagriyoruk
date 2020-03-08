from flask import Flask, flash, request, redirect, url_for, render_template, send_file
import TweetToVideo

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home_page():
   if request.method == 'POST':
      handle = request.form['handle']
      TweetToVideo.VideoSummary('keys',[handle])
      return redirect(url_for('download', filename = handle))
   return render_template('homepage.html')

@app.route('/downloads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    file = '/home/ece-student/Desktop/EC500_HW5/VideoSummary/'+ filename + '_daily.mp4'
    if request.method == 'POST':
        return send_file(file, as_attachment=True)
    return render_template('result.html', filename=filename)

if __name__ == '__main__':
   app.run(debug = True)