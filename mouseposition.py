import pyautogui
import time
anahtar =1
while (anahtar>=1):
    time.sleep(1)
    im=pyautogui.position(),"fare dolanıyor"
    ik=pyautogui.alert(im,"Fare Kordinatör","OK_TEXT","")
    print(im)
okey = open("kaydet.text", "w")
okey.write(str(all((im))))
okey.close()