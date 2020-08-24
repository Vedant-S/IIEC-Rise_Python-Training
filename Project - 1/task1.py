import os
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')  
engine.setProperty('rate', 180)     

pyttsx3.speak("Hello Muskaan")
print()
pyttsx3.speak("I am your assistant Jack")
print(" \t\t!!!!!!!!WELCOME MUSKAN!!!!!!!")
pyttsx3.speak("How can I help you...?")
while True:
  print()
  p = input(" Hey user how can I help you: ")





  if ("date" in p): 
    pyttsx3.speak("showing todays date")
    os.system("date")
  elif ("time" in p): 
    pyttsx3.speak("showing current time")
    os.system("time")
  elif ("Hello" in p) or ("hy" in p) or ("hey" in p):
    pyttsx3.speak("Hello muskan")
 
  
  elif ("tell" in p) or ("about" in p) or ("yourself" in p):
    pyttsx3.speak("My name is jack im your assitant and i wil help you for your requirements")
  
  elif ("chrome" in p): 
    pyttsx3.speak("opening chrome for you")
    os.system("chrome")

  elif ("aws" in p) or ("aws cloud services" in p):
    pyttsx3.speak("opening amazon web services")
    os.system("chrome aws.amazon.com")

  elif ("gmail" in p):
    pyttsx3.speak("opening your G mail")
    os.system("chrome www.gmail.com") 

  elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("turbo c++" in p) :
         pyttsx3.speak("Opening turbo c++ for you plz wait")
         os.system("Turbo C++")

  elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("ms excel" in p) :
         pyttsx3.speak("Opening ms excel plz wait")
         os.system("Excel")

  elif ("yahoomail" in p) or ("yahoo mail" in p):
    pyttsx3.speak("opening yahoo mail")
    os.system("chrome www.yahoomail.com")

  elif ("youtube" in p):
    pyttsx3.speak("opening youtube for you plz wait")
    os.system("chrome www.youtube.com")

  elif ("twitter" in p):
    pyttsx3.speak("opening twitter for you plz wait")
    os.system("chrome www.twitter.com")

  

  elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("linkedin" in p) :
    pyttsx3.speak("opening your linkedin account plz wait")
    os.system("chrome www.linkedin.com")

  

  elif  (("run" in p) or ("open" in p) or  ("launch" in p))  and  (("notepad" in p) or  ("editor" in p)): 
    pyttsx3.speak("opening notepad")
    os.system("notepad")
 
 
  elif ("virtualbox" in p) or ("virtual box" in p) or ("VM" in p) or ("vbox" in p) or ("vm" in p): 
    pyttsx3.speak("opening Vitualbox")

    
  elif ("anydesk" in p): 
    pyttsx3.speak("opening anydesk")
    os.system("anydesk")
  elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  (("Feem " in p) or  ("Feem" in p)) :
         pyttsx3.speak("Opening feem for you plz wait")
         os.system("Feem")

  elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("codeblocks " in p):
      pyttsx3.speak("Opening codeblocks for you plz wait")
      os.system("codeblocks.exe")

  elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("Powerpoint " in p) :
         pyttsx3.speak("Opening Powerpoint  for you plz wait")
         os.system("PowerPoint")
  
  elif ("How" in p) or ("jack" in p):
    pyttsx3.speak("i can help you in following ways")
    print()
    print("!! I can help you in following ways !!")
    pyttsx3.speak("running window based commands")
    print()
    print(" - Window Based Commands")
    pyttsx3.speak("Entertainment")
    print()
    print(" - Entertainment")
    pyttsx3.speak("aws clouds")
    print()
    print(" - aws Clouds")
    pyttsx3.speak("emails")
    print()
    print(" - Emails")
    pyttsx3.speak("Social media")
    print()
    print(" - Social Media")
    
  
  elif ("exit" in p) or ("quit" in p) or ("bye" in p):
    pyttsx3.speak("see you soon,, have a nice day...!!!")
    break
  else: 
    print("\t \t \t \t don't support ")
    pyttsx3.speak("such application doesn't support try another")

  
