# Python program to translate
# speech to text and text to speech
 
 
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
     
# Loop infinitely for user to
# speak
i=0
while(i<5):
    if(i==0):
        howr=int(datetime.datetime.now().hour)
        if howr>=0 and howr<12:
            print("Good Morning!")
            SpeakText("good morning!")
        elif howr>=12 and howr<18:
            print("Good Afternoon!")
            SpeakText("Good Afternoon!")
        else:
            print("Good Evening!")
            SpeakText("Good Evening!")
        print("Hello! How cane I help you?")
        SpeakText("hello! how cane i help you?")

    print("listening....")
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            # open a text file and write the output text there.

            if("creat" in MyText):
                print("give a file name")
                SpeakText("give a file name")
                print("lestening....")
                audio2 = r.listen(source2)
                MyText2 = r.recognize_google(audio2)
                MyText2 = MyText2.lower()
                filename=(MyText2+".txt")
                fp=open(MyText2,"w")
                print("what you wanna to write?")
                SpeakText("what you wanna to write?")
                print("lestening....")
                audio2 = r.listen(source2)
                text2 = r.recognize_google(audio2)
                text2 = text2.lower()
                fp.write(text2)
                print("The file is created!")
                SpeakText("the file is created!")
                fp.close()

            elif("open file" in MyText):
                print("Give the file name")
                SpeakText("give the file name")
                print("lestening....")
                audio2 = r.listen(source2)
                MyText1 = r.recognize_google(audio2)
                MyText1 = MyText1.lower()
                fp=open(MyText1,"r")
                print("the file contant is....")
                SpeakText("the file contant is")
                text = fp.read()
                print(text)
                SpeakText(text)
                fp.close()

            # opening Websit......


            elif "website" in MyText:
                print("Give the website name")
                SpeakText("Give the website name")
                print("listening....")
                audio2 = r.listen(source2)
                MyText3 = r.recognize_google(audio2)
                MyText1 = MyText3.lower()
                print("opening "+MyText3)
                SpeakText("opening "+MyText3)
                c=".com"
                web=MyText3+c
                webbrowser.open(web)

            elif("stop"or"bye" in MyText):
                print("Thank you!\nHave a nice Day!")
                SpeakText("Thank you!! have a nice day!")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        SpeakText("I'm not online. Trying to connect automaticly to the network.")
        SpeakText("Sorry,i can't! You have to do it manualy!")
         
    except sr.UnknownValueError:
        print("I can not recognize you please say again ")
    i+=1