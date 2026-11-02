from google import genai
from dotenv import load_dotenv
import os 
import io
from gtts import gTTS

#loading the evironment variable 
load_dotenv()

my_api_key=os.getenv("GEMINI_API_KEY")

#initializing a client

client=genai.Client(api_key=my_api_key)


#note generate
def note_generator(images) :
    prompt ="""summarize the picture in note format at max 100 words
                make sure to add necessary markdown to differentiate different section """


    response= client.models.generate_content(
        ##############################################################################################
       #model="gemini-3.5-live-translate-preview"   ,
       model="gemini-3.8-flash",
       ######################################################################
       contents=[images , prompt ] 
        #contents=[*images, prompt] 
        #contents=images + [prompt]                                 
                                   )
    return response.text 


def audio_transcription(text):
    speech = gTTS(text , lang ='en',slow=False)
                                                   # speech.save("Welcome.mp3")
                                                   # st.audio("Welcome.mp3")       Locally save kora ata // 
    audio_buffer=io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer


def quiz_generator(image , difficulty):

    prompt =f"Generate 3 quizzes based on the {difficulty}. Make sure to add markdown to the options. "
   
    response= client.models.generate_content(
          model="gemini-3.8-flash",
          contents=[image , prompt ] 
                                         
                                      )
    return response.text 
   
