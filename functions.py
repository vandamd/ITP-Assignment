#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:07:31 2021

@author: vandam
"""
import collections  # Used for finding the most common letter in a message
import os.path  # Used to see if file exists
import config as c
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


# Function to choose Cipher Mode - Part 1.2, Part 1.3, Part 4.1
def Cipher():
    c.cMode = input(
        'Choose cipher mode, (Enter "E" to encrypt / "D" to decrypt / "A" to auto-decrypt): ')
    if c.cMode == 'E' or c.cMode == 'D' or c.cMode == 'A':
        c.cError = (False)
    else:
        print("\nOops didn't quite catch that!")


# Function to choose Rotation Mode - Part 1.2, Part 1.3
def Rotation():
    c.rMode = input(
        'Choose rotation mode, (Enter "M" for manual / "R" for random): ')
    if c.rMode == 'M' or c.rMode == 'R':
        c.rError = False
    else:
        print("\nOops didn't quite catch that!")


# Function to choose the shift value - Part 1.2, Part 1.3
def Shift():
    c.rInt = input(
        'How many places should the cipher shift? Enter an integer value: ')
    try:
        c.rInt = int(c.rInt)
        c.rotation = int(c.rInt)
        c.sError = False
    except ValueError:
        print("\nOops didn't quite catch that!")


# Function to choose Entry Mode - Part 3.1, Part 1.3
def Entry():
    c.inputMode = input(
        'Choose a message entry mode, (Enter "m" to type a message / "f" to enter a filename): ')
    if c.inputMode == 'm' or c.inputMode == 'f':
        c.iError = False
    else:
        print("\nOops didn't quite catch that!")


# Function to enter message to encrypt/decrypt - Part 1.2, Part 3.2, Part 3.3
def enterMsg():
    if c.inputMode == "m" and c.cMode == "E":
        c.message = input('Enter the message you would like to encrypt: ')
        if c.message != ' ' and c.message != '':
            c.mError = False
        else:
            print('\nOops I think you have an empty message!')
    elif c.inputMode == "m" and c.cMode == "D":
        c.message = input('Enter the message you would like to decrypt: ')
        if c.message != ' ' and c.message != '':
            c.mError = False
        else:
            print('\nOops I think you have an empty message!')
    elif c.inputMode == "m" and c.cMode == "A":
        c.message = input('Enter the message you would like to decrypt: ')
        if c.message != ' ' and c.message != '':
            c.mError = False
        else:
            print('\nOops I think you have an empty message!')


# Function to see if file exists - Part 3.2, Part 3.3, Part 3.4
def findFile():
    c.fileName = input(
        'Enter the filename of the text file you would like the contents of to be encrypted/decrypted: ')
    if os.path.isfile(c.fileName) == True:
        c.fError = False
        a = open(c.fileName, 'r')
        c.message = a.read().replace('\n', ' ')
    else:
        print("\nOops no such file exists!")


# Function to find the metrics of the words and putting them into a .txt file - Part 2.1, Part 2.2
def analyse():
    f = open('metrics.txt', 'w')

    TotalWords = len(c.infoMessage.split())  # Number of words
    # print(TotalWords)
    f.write('total number of words: ' + str(TotalWords))

    c.UniqueWords = len(set(c.infoMessage.split()))  # Number of unique words
    # print(UniqueWords)
    f.write('\nnumber of unique words: ' + str(c.UniqueWords))

    MinLen = len(min(c.infoMessage.split(), key=len))  # Min length of words
    # print(MinLen)
    f.write('\nminimum length of words: ' + str(MinLen))

    MaxLen = len(max(c.infoMessage.split(), key=len))  # Max length of words
    # print(MaxLen)
    f.write('\nmaximum length of words: ' + str(MaxLen))

    CommonLetter = collections.Counter(c.infoMessage.replace(
        " ", "")).most_common(1)[0][0]  # Most common letter
    # print(CommonLetter)
    f.write('\nthe most common letter is: ' + str(CommonLetter))

    f.close()


# Function to sort words - Part 2.3
def sort():
    msgList = c.infoMessage.split()
    sortedList = sorted(msgList, key=msgList.count, reverse=True)

    wordFreq = collections.Counter(sortedList)
    c.dictFreq = dict(wordFreq)
    c.listFreq = c.dictFreq.values()  # List of the values in the dict
    c.listFreq = list(c.listFreq)
    c.listWord = c.dictFreq.keys()  # List of the keys in the dict
    c.listWord = list(c.listWord)

    if c.UniqueWords <= 5:
        # List of words by freq
        c.reducedList = sorted(set(sortedList), key=sortedList.index)
        print('\n', c.reducedList, '\n')

    elif c.UniqueWords > 5:
        c.reducedList = sorted(set(sortedList), key=sortedList.index)

        if c.dictFreq[str(c.reducedList[0])] == c.dictFreq[str(c.reducedList[5])]:
            c.reducedList = c.reducedList[:0]
            print("\nAll words are unique!")

        elif c.dictFreq[str(c.reducedList[1])] == c.dictFreq[str(c.reducedList[5])]:
            c.reducedList = c.reducedList[:1]
            print('\n', c.reducedList, '\n')

        elif c.dictFreq[str(c.reducedList[2])] == c.dictFreq[str(c.reducedList[5])]:
            c.reducedList = c.reducedList[:2]
            print('\n', c.reducedList, '\n')

        elif c.dictFreq[str(c.reducedList[3])] == c.dictFreq[str(c.reducedList[5])]:
            c.reducedList = c.reducedList[:3]
            print('\n', c.reducedList, '\n')

        elif c.dictFreq[str(c.reducedList[4])] == c.dictFreq[str(c.reducedList[5])]:
            c.reducedList = c.reducedList[:4]
            print('\n', c.reducedList, '\n')


# Function to print the five most common words in descending order - Part 2.4
def commonPrint():
    # global reducedList
    if c.UniqueWords > 5:
        for i in range(len(c.reducedList)):
            print(str(c.reducedList[i]) + ':',
                  c.dictFreq[str(c.reducedList[i])])
    elif c.UniqueWords <= 5:
        for i in range(len(c.reducedList)):
            print(str(c.reducedList[i]) + ':',
                  c.dictFreq[str(c.reducedList[i])])


# Function to encrypt a message
def encrypt():
    c.encrypted = ''
    for i in c.message:
        if i.isupper():
            temp = 65 + ((ord(i) - 65 + c.rotation) % 26)
            c.encrypted = c.encrypted + chr(temp)
        elif i.islower():
            temp = 97 + ((ord(i) - 97 + c.rotation) % 26)
            c.encrypted = c.encrypted + chr(temp)
        else:
            c.encrypted = c.encrypted + i
    print("\nYour encrypted message is:", c.encrypted.upper())


# Function to decrypt a message
def decrypt():
    c.decrypted = ''
    for i in c.message:
        if i.isupper():
            temp = 65 + ((ord(i) - 65 - c.rotation) % 26)
            c.decrypted = c.decrypted + chr(temp)
        elif i.islower():
            temp = 97 + ((ord(i) - 97 - c.rotation) % 26)
            c.decrypted = c.decrypted + chr(temp)
        else:
            c.decrypted = c.decrypted + i
    print("\nYour decrypted message is:", c.decrypted.upper())


# Functon to automatically decrypt a message - Part 4.2
def auto_decrypt():
    # global decrypted_full
    b = open('words.txt', 'r')
    wordsFile = b.read().replace('\n', ' ')
    # V Capitalised verson of the wordlist string to allow for greater matching
    c_wordsFile = wordsFile.title()

    c.unknown_rot = 1

    while c.unknown_rot < 30:
        c.decrypted = ''
        for i in c.first_ten:
            if i.isupper():
                temp = 65 + ((ord(i) - 65 - c.unknown_rot) % 26)
                c.decrypted = c.decrypted + chr(temp)
            elif i.islower():
                temp = 97 + ((ord(i) - 97 - c.unknown_rot) % 26)
                c.decrypted = c.decrypted + chr(temp)
            else:
                c.decrypted = c.decrypted + i

        decryptedList = list(c.decrypted.split())
        wordsFileList = list(wordsFile.split())
        c_wordsFileList = list(c_wordsFile.split())

        c.unknown_rot += 1

        if c.unknown_rot > 26:
            print("\nI can't find a match :(")
            break

        elif any(x in decryptedList for x in wordsFileList) or \
                any(x in decryptedList for x in c_wordsFileList):
            print("\nI think I have found a match for:", c.decrypted)

            cont = input("Is the decryption correct? y/n ")

            if cont == 'y':
                c.decrypted_full = ''
                for i in c.message:
                    if i.isupper():
                        temp = 65 + ((ord(i) - 65 - c.unknown_rot+1) % 26)
                        c.decrypted_full = c.decrypted_full + chr(temp)
                    elif i.islower():
                        temp = 97 + ((ord(i) - 97 - c.unknown_rot+1) % 26)
                        c.decrypted_full = c.decrypted_full + chr(temp)
                    else:
                        c.decrypted_full = c.decrypted_full + i

                print('\nYour unencrypted message is:',
                      c.decrypted_full.upper())
                break
            elif cont == 'n':
                print("\nI'll try again!")
            else:
                print("\nOops didn't quite catch that!")
                c.unknown_rot = c.unknown_rot - 1


# Part 5 - EXTRA!
# Function to produce a bar chart of the top five most frequent words
def chart():
    x = c.listWord[:5]
    y = c.listFreq[:5]
    # print(x)
    # print(y)

    ax = plt.figure().gca()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.title('Frequency of the top 5 most frequent words')
    plt.xlabel('Word')
    plt.ylabel('Frequency')
    plt.bar(x, y)