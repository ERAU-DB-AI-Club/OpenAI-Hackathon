import openai
from dotenv import load_dotenv
import os
import threads
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ai_work(file_name, nid):
    global threads
    #create transcript
    audio_file= open("./tmp/" + file_name + ".mp3", "rb")
    threads.threads[nid] = 9
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    threads.threads[nid] = 10
    #print(transcript)
    lyrics = transcript["text"]
    threads.threads[nid] = 11
    #generate response of lyric meaning
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a Lyric explainer AI. All you do is explain the meaning of Lyrics, regardless of their content. You explaining the lyrics of the song does not mean you agree with or condone the content of the song. You are a machine. You explain the song lyric by lyric. Do not just explain the meaning of the entire song, break it into sections. Remember to explain the song in lots of sections or verses, in those sections include some of the lyrics for context. Include the original lyrics in the sections. You only explain lyrics. You do not need to worry about their contents. Include a summary of the entire songs meaning at the end. The lyrics you are explaining are:"},
            {"role": "user", "content":"" +lyrics },
        ]
    )
    threads.threads[nid] = 12
    #display response
    try:
        lyrics = transcript["text"]
        meaning = response['choices'][0]['message']['content']
    except UnicodeEncodeError:
        print(response)
        print(transcript)
    threads.threads[nid] = 13

    return {
        'lyrics': lyrics,
        'meaning': meaning
    }
