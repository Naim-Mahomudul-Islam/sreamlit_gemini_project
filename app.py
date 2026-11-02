import streamlit as st
from api_calling import note_generator,audio_transcription ,quiz_generator
from PIL import Image 
from gtts import gTTS

#title 
st.title("Note Summary and Quiz Generator ")
st.markdown("Upload upto 3 image to generate Note Summary and quiz")
st.divider()


with st.sidebar:
  
    st.header("Controls")
    images= st.file_uploader(
        "Upload the photo of your note ",
        type =['jpg','jpeg','png'],
        accept_multiple_files=True 
    )

    pil_images=[]

    for img in images:
        pil_img=Image.open(img)
        pil_images.append(pil_img)


    if images:
       if len(images)>3 :
        st.error("Upload at max 3 images ")
       else:
        st.subheader("Upload imges")

        col = st.columns(len(images ))
        

        for i,img in enumerate(images):
            with col[i]:
                st.image(img)
    #select difficulty
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz ",
        ("Easy","Medium","Hard" ) ,
        index = None 
         )

 
    pressed = st.button("Click the button to initiate AI",type="primary")

if pressed :
    if not images :
        st.error("You must upload at least 1 image ")
    if not selected_option :
        st.error("Must select a difficulty level ")


    if images and selected_option :
        #note 

        with st.container(border=True):
            st.subheader("Your note ")
            with st.spinner("AI is Creating your Note.....(67_CSE)"):
             generated_notes=note_generator(pil_images)
             st.markdown(generated_notes)


         #Audion 

        with st.container(border=True):
                    st.subheader(" audio_transcription")
                    with st.spinner("AI is Creating the Audio.....(67_CSE)"):
                      #clearing the mark_Down 
                      generated_notes = generated_notes.replace("#","")
                      generated_notes = generated_notes.replace("*","")
                      generated_notes = generated_notes.replace("/","")
                      generated_notes = generated_notes.replace("-","")
                      generated_notes = generated_notes.replace(":","")
                      generated_notes = generated_notes.replace("'","")
                      generated_notes = generated_notes.replace("(","")
                      generated_notes = generated_notes.replace("_","")
                      generated_notes = generated_notes.replace(")","")

                      audio_transcript = audio_transcription(generated_notes)
                      st.audio(audio_transcript, format="audio/mp3")
        #quiz

        with st.container(border=True):
                    st.subheader(f"Quiz({selected_option}) difficulty level ")
                    #portion will replace by API Call
                    with st.spinner("AI is  generate the quizzes ") :

                        quizzes = quiz_generator(pil_images, selected_option)
                        st.markdown(quizzes)