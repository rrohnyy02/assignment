from flask import Flask, render_template, request, jsonify
import requests
import openai
import os

openaikey =os.getenv('Open_AI_API_KEY')
deepgramtoken = os.getenv('Deepgram_Token')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/transcription', methods=['POST','GET'])
def transcribe_audio():
    audio_file = request.files['audio']

    deepgram_url = "https://api.deepgram.com/v1/listen?model=whisper&diarize=true&punctuate=true&utterances=true"
    headers = {
        'Authorization': deepgramtoken,
        'Content-Type': 'audio/wav'
    }
    response = requests.post(deepgram_url, headers=headers, files={'data': audio_file})
    transcription_data = response.json()
    s = ""
    for utterance in transcription_data['results']['utterances']:
        speaker = str(utterance['speaker'])
        transcript = utterance['transcript']
        s+= speaker + ": " +transcript + "\n"   


    openai.api_key = openaikey
    chat_completion = openai.chat.completions.create(
                                model="gpt-3.5-turbo",
                                messages=[

                                 {"role": "system", "content": '''you have to frame this conversation 
                                properly with correct speker detection and 
                                then his message, please do it carefully, i need proper diarization with correct names of speaker ''' },
    
                                {"role": "user", "content": '''you have to frame this conversation 
                                properly with correct speker detection and then his message, 
                                write correct names of sspeaker rather than digits.'''+ str(s)},]
            
    
                                )                            
    
    transcription_text = chat_completion.choices[0].message.content
    return jsonify({'result': transcription_text})

@app.route('/summary', methods=['POST'])
def summarize_audio():
    audio_file = request.files['audio']
    response = transcribe_audio()
    json_data = response.json
    text= str(json_data['result'])
    openai.api_key = openaikey
    
    chat_completion = openai.chat.completions.create(
                                model="gpt-3.5-turbo",
                                messages=[
                                {"role": "system", "content": "You will write a crisp and small summary of the conversation"},
                                {"role": "user", "content": text},]
                        
                                    )                            
    summarized_text = chat_completion.choices[0].message.content
    return jsonify({'result': summarized_text})


@app.route('/Insights', methods=['POST', 'GET'])
def GetInsights():
    audio_file = request.files['audio']
    response = transcribe_audio()
    json_data = response.json
    text= str(json_data['result'])
    openai.api_key = openaikey
    
    chat_completion = openai.chat.completions.create(
                                model="gpt-3.5-turbo",
                                temperature=  0,
                                messages=[
                                {"role": "system", "content": ''' you will tell me about what
                                 each speaker like , his favourte topics and interest and his disliking, 
                                 in general in psychological sense,
                                only print whats necessary in  format 
                                speaker name :
                                Likes: []
                                dislikes:[]
                                empty line
                                ..
                                similarily about other spekars 

                                '''},
                                {"role": "user", "content":  '''  you will tell me about what
                                 each speaker like , his favourte topics and interest and his disliking, 
                                 in general in psychological sense,
                                only print whats necessary in  format speaker name:
                                Likes: []
                                dislikes:[]
                                empty line

                                .. '''+text},]
                                )                            
    Insights = chat_completion.choices[0].message.content
    print (Insights)

    return jsonify({'result': Insights})


@app.route('/psychoanalysis', methods=['POST' , 'GET'])
def perform_psychoanalysis():
    audio_file = request.files['audio']
    
    response = transcribe_audio()
    json_data = response.json
    text= str(json_data['result'])
    
    openai.api_key = openaikey
    chat_completion = openai.chat.completions.create(
                                model="gpt-3.5-turbo",
                                messages=[
                                {"role": "system", "content": '''You Generate the pyschological insights 
                                of each speaker in 15 words from the conversation in the format ->
                                 speaker : pyschological insights'''},
                                {"role": "user", "content": text},]
                               
                                    )                            
    
    psychoanalyzed_text = chat_completion.choices[0].message.content
    return jsonify({'result': psychoanalyzed_text})






@app.route('/rating', methods = ['POST' , 'GET'])
def rating():

    audio_file = request.files['audio']
    response = transcribe_audio()
    json_data = response.json
    text= str(json_data['result'])
    combined_prompt = '''give me score of each author out of 10 
    for (Trust, empathy , courage, optimism, charisma) 
    in json form for the conversation:''' + text

    openai.api_key = openaikey
    chat_completion = openai.chat.completions.create(
                                messages=[
                                        {
                                        "role": "user",
                                        "content":combined_prompt ,
                                        }
                                        ],
                                        model="gpt-3.5-turbo"
                                        )
    
    rating = chat_completion.choices[0].message.content
    return jsonify({'result': rating})


@app.route('/analyze', methods=['POST', 'GET'])
def analyze_audio():

    audio_file = request.files['audio']
    transcription = transcribe_audio(audio_file)
    print("transcription")

    combined_prompt  = "Generate the psychological insights from :" + transcription

    openai.api_key = openaikey
    chat_completion = openai.chat.completions.create(
                                messages=[
                                        {
                                        "role": "user",
                                        "content":combined_prompt ,
                                        }
                                        ],
                                        max_tokens=10 ,
                                        model="gpt-3.5-turbo",
                                        )
    response = chat_completion.choices[0].message.content
  
     # Check if response is a string, if so, convert it to a dictionary
    if isinstance(response, str):
        summary = response  # Assuming response is already the summary string
    elif isinstance(response, dict):
        summary = response.get("summary", "Summary not available")
    else:
        summary = "Summary not available"

    # Perform any further processing or analysis here
    return jsonify({'transcription': transcription , 'summary': summary})


if __name__ == '__main__':
    app.run(debug=True)

