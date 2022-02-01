#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 21:37:54 2021

@author: vandam
"""
import random
import re
import functions as f
import config as c


while c.cError:
    f.Cipher()  # Choose Cipher Mode

if c.cMode == "E" or c.cMode == "D":
    while c.rError:
        f.Rotation()  # Choose Rotation Mode

    if c.rMode == 'M':
        while c.sError:
            f.Shift()  # Choose Shift Value

    if c.rMode == 'R':  # Random rotation value - Part 1.2
        rotation = random.randint(1, 25)
        print("\nYour random shift value is:", rotation)

while c.iError:
    f.Entry()  # Choose Message Entry Mode

if c.inputMode == 'm':
    while c.mError:
        f.enterMsg()  # Function to enter message

if c.inputMode == "f":
    while c.fError:
        f.findFile()  # See if file exists and opens it

if c.cMode == 'E':
    # Removes numbers and punctuation from message to analyse
    c.infoMessage = re.sub(r'[0-9]|[""'';:,.!?(+*)]+', '', c.message.lower())
    f.analyse()  # Analyses infoMessage
    f.sort()  # Sort words by frequency
    f.commonPrint()  # Prints up to five of the most frequent words with their frequency
    f.encrypt()  # Encrypts message and outputs the result
    f.chart()  # Produces a bar chart

elif c.cMode == 'D':
    f.decrypt()  # Decrypts the message and outputs it
    # Removes numbers and punctuation from decrypted message
    c.infoMessage = re.sub(r'[0-9]|[""'';:,.!?(+*)]+', '', c.decrypted.lower())
    f.analyse()
    f.sort()
    f.commonPrint()
    f.chart()

if c.cMode == 'A':
    # First ten words of the message inputted
    c.first_ten = ' '.join(c.message.split()[:10])
    f.auto_decrypt()  # Auto-decrypts!
    if c.unknown_rot <= 26:  # If Autodecryption is successful
        c.infoMessage = re.sub(
            r'[0-9]|[""'';:,.!?(+*)]+', '', c.decrypted_full.lower())
        f.analyse()
        f.sort()
        f.commonPrint()
        f.chart()
    elif c.unknown_rot > 26:
        print()
