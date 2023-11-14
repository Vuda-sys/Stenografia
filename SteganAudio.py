import os
from sys import platform,stdin
import wave
from colorama import init
from termcolor import colored


init()


def clearTerminal():
    if 'win32' in platform:
        os.system('cls')
    else:
        os.system('clear')


def embed_into_audio(input_audio,message,output_audio):
    print(colored("\n[PROCESSING]","yellow"),"The Audio is being processed, Please Wait...")
    waveObject = wave.open(input_audio, mode='rb')
    frameBytes = bytearray(list(waveObject.readframes(waveObject.getnframes())))    
    message += '\0'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in message])))
    for i, bit in enumerate(bits):
        frameBytes[i] = (frameBytes[i] & 254) | bit
    frameModified = bytes(frameBytes)
    with wave.open(output_audio,'wb') as output:
        output.setparams(waveObject.getparams())
        output.writeframes(frameModified)
    waveObject.close()
    print(colored("\n[SUCCESS]","green"),"Embedded message into Audio File successfully!")


def extract_from_audio(input_audio):
    print(colored("\n[PROCESSING]","yellow"),"The Audio is being processed, Please Wait...")
    waveObject = wave.open(input_audio, mode='rb')
    frameBytes = bytearray(list(waveObject.readframes(waveObject.getnframes())))
    extracted = bits_to_bytes([frameBytes[i] & 1 for i in range(len(frameBytes))])
    message = ''
    for i in extracted:
        byte_data = i.to_bytes(1, byteorder='big')
        char = byte_data.decode('utf-8')
        message += char
        if char == '\0':
            break
    print(colored("\n[SUCCESS]","green"),"Your embedded message is as follows:\n\n{}\n".format(message))


def bits_to_bytes(bits):
    # Pad the bit array with zeros if its length is not a multiple of 8
    bits += [0] * (8 - len(bits) % 8) if len(bits) % 8 != 0 else []
    
    # Group bits into bytes
    byte_array = []
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            byte = (byte << 1) | bits[i + j]
        byte_array.append(byte)
    
    return bytes(byte_array)


def multiLineInput():
    print(colored("\n[NOTE]","yellow"),"Multi Line Input has started, to stop Input, Enter a new Blank Line\nand press CTRL+Z (or CTRL+D if that doesn't work) and press Enter")
    msg = stdin.readlines()
    output = ""
    for i in range(len(msg)):
        output = output + msg[i]
    return output[:-2]


if __name__=="__main__":
    print(colored("[CHOICE]","yellow"),"What would you like to do?\n   [1] Embed Message into an Audio File\n   [2] Extract Message from Audio File")
    choice = int(input("Selection > "))
    if choice == 1:
        audiofile = input("\n[INPUT] Complete Location of Input Audio File: ").replace('"','')
        typechoice = int(input("\n[CHOICE] Choose type of Message:\n  [1] Single Line Message\n  [2] Multiline Message\n > "))
        if typechoice == 1:
            message = input("\n[INPUT] Enter the message you want to hide: ")
        elif typechoice == 2:
            message = multiLineInput()
        else:
            print(colored("\n[ERROR]","red"),"{} is not a valid option".format(typechoice))
        outputfile = input("\n[INPUT] Complete Location for Output Audio File: ").replace('"','')
        embed_into_audio(audiofile,message,outputfile)
    elif choice == 2:
        audiofile = input("\n[INPUT] Complete Location of Input Audio File: ").replace('"','')
        extract_from_audio(audiofile)
    elif choice == 99:
        print(" Exit code received, Thank you for using SteganAudio!\n")
    else:
        print(colored("\n[ERROR]","red"), choice, "isn't a valid choice, exiting program...")