import pyttsx3
import os

pyttsx3.speak("Welcome user ...How can I help you? ")


while True:
       print("How can I help you :" , end=' ' )
       p= input()
       #print(p)
       #os.system(x)

       if  (("run" in p) or  ("open" in p) or ("launch" in p))  and  (("chrome " in p) or  ("browser" in p)) :
         pyttsx3.speak("Opening chrome for you plz wait")
         os.system("chrome")
       elif  (("run" in p) or ("open" in p) or  ("launch" in p))  and  (("notepad" in p) or  ("editor" in p)):
         pyttsx3.speak("Opening notepad for you plz wait")
         os.system("notepad")

       elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  (("Feem " in p) or  ("Feem" in p)) :
         pyttsx3.speak("Opening feem for you plz wait")
         os.system("Feem")

       elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("codeblocks " in p):
         pyttsx3.speak("Opening codeblocks for you plz wait")
         os.system("codeblocks.exe")

       elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("Powerpoint " in p) :
         pyttsx3.speak("Opening Powerpoint  for you plz wait")
         os.system("PowerPoint")

       elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("linkedin" in p) :
         pyttsx3.speak("Opening your linked account  you plz wait")
         os.system("chrome linked.in")
        
       elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("ms excel" in p) :
         pyttsx3.speak("Opening ms excel plz wait")
         os.system("Excel")
     
       elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("turbo c++" in p) :
         pyttsx3.speak("Opening turbo c++ for you plz wait")
         os.system("Turbo C++")

       elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("virtual box" in p) :
         pyttsx3.speak("Opening virtual box for you plz wait")
         os.system(" Oracle VM VirtualBox")

        
       elif (("hii" in p) or ("hello" in p) or ("hey" in p)):
         pyttsx3.speak("hiii user now tell me how can I help you")

  

       elif ("exit" in p) or ("stop" in p):
         pyttsx3.speak("Exiting")
         break
       else:
         pyttsx3.speak("such application dont support in your computer plz tell again")