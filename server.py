from flask import Flask, render_template, request, make_response
from download_song import download_song
from ai_work import ai_work
import threads
app = Flask(__name__)

app.secret_key = 'super secret key'
threads.threads = {}

@app.route('/', methods=['GET'])
def server():
    return render_template('index.html', title='Welcome')

    
# https://itecnote.com/tecnote/python-flask-app-update-progress-bar-while-function-runs/
@app.route('/progress/<int:nid>')
def progress(nid):
    global threads
    if str(nid) in threads.threads:
        res = str(threads.threads[str(nid)])

        response = make_response(res, 200)
        response.mimetype = "text/plain"

        return response
    else:
        return str(0)

@app.route('/upload', methods=['POST'])
def upload_song():
    global threads
    if request.method == 'POST':
        song_url = request.form.to_dict()['song_url']
        nid = request.form.to_dict()['nid']

        threads.threads[nid] = 0
        song_name = download_song(song_url, nid)
    
        ai_result = ai_work(song_name, nid)

        del threads.threads[nid]

        return {
            'song_name': song_name,
            'song_meaning': ai_result['meaning'],
            'song_lyrics': ai_result['lyrics']
        }


app.run(host='0.0.0.0', port=81)