#! /usr/bin/env python3
"""Copipasta"""
from pynput.keyboard import Key, Listener, KeyCode
import pyperclip, time, datetime, platform

def on_press(key):
    #copipasta code
    global cop_cells
    if key== KeyCode(char='c'):
        #evita que copie do clipboard antes de copiar para o clipboard
        time.sleep(0.25)
        #copia do clipboard
        cell=pyperclip.paste()
        #coloca na lista cop_cells
        cop_cells.append(cell)
        #confirma a copia
        print(cop_cells[-1],"copied")

def on_release(key):
    global cop_cells
    if key == Key.esc:
        # pára o listener
        return False
    elif key== KeyCode(char='0'):
        now=datetime.datetime.now()
        if platform.system()=='Darwin':
            #adaptar pasta pwd ao pc
            ficheiro='/Users/iamthesenate/Desktop/'+str(now.year)+'_'+str(now.month)+'_'+str(now.day)+'_'+str(now.hour)+'*'+str(now.minute)+'*'+str(now.second)+'.txt'
        elif platform.system()=='Linux':
            pass
        elif platform.system()=='Windows':
            pass
        with open(ficheiro,'w') as record:
            for cell in cop_cells:
                record.write(cell+'\n')
        # pára o listener
        return False

cop_cells=[]
print("Welcome to Copipasta.\nLet me help you copy several pieces of text and neatly give you all of them at the end!\nJust begin by copying all the text you want, and i'll confirm you've copied it as you go.\nWhen you're done, just press the Escape key.\nIf you want to create a file with your text on top of presenting it to you, press 0 instead of Escape.\nThank you.")

# Regista eventos
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

print('__________________')
for cell in cop_cells:
    print(cell)