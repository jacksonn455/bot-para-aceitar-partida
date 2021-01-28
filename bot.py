# Imports
# -*- encoding: utf-8 -*-
from pyautogui import *
import pyautogui
from time import sleep

#pip2 install opencv-python==4.2.0.32
#pip install pyautogui

def click(x, y):
  pyautogui.moveTo(x, y)
  pyautogui.click()

def check_screen():
  button_pos = (pyautogui.locateOnScreen('imagem.png', confidence=0.7))
  if button_pos != None:
    click(button_pos.left, button_pos.top)
    return True
  
  return False

def main():
    print('Estou de olho na fila...')
    
    while True:
      if check_screen():       
        print("Cliquei")           
        sleep(6)

main() 