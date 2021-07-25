import sqlite3
from sqlite3 import Error
import os.path
from os import path



database = sqlite3.connect("#database")
cursor = database.cursor()

sql_command = """ CREATE TABLE HAPPY (
NAME		    TEXT	PRIMARY KEY NOT NULL,
ARTIST			TEXT 	NOT NULL,
LENGTH 			TEXT 	NOT NULL)
;"""

sql_command = """ CREATE TABLE SAD (
NAME		    TEXT	PRIMARY KEY NOT NULL,
ARTIST			TEXT 	NOT NULL,
LENGTH 			TEXT 	NOT NULL)
;"""
sql_command = """ CREATE TABLE ANGRY (
NAME		    TEXT	PRIMARY KEY NOT NULL,
ARTIST			TEXT 	NOT NULL,
LENGTH 			TEXT 	NOT NULL)

;"""sql_command = """ CREATE TABLE FOCUSED (
NAME		    TEXT	PRIMARY KEY NOT NULL,
ARTIST			TEXT 	NOT NULL,
LENGTH 			TEXT 	NOT NULL)
;"""

sql_command = """ CREATE TABLE STRESSED (
NAME		    TEXT	PRIMARY KEY NOT NULL,
ARTIST			TEXT 	NOT NULL,
LENGTH 			TEXT 	NOT NULL)
;"""


mood = input("Please enter your mood: 1)Happy 2)Sad 3)Angry 4)Focused 5)Stressed ") # only used for this code, will be replaced by GUI when integrated
i=1
while i = 1:

    current_song_Name = # current song being played 
    current_song_Artist = # curent song's artist
    current_song_Length = # currrent song's lenght

    if mood == 1:
           if # skip is presed:
               current_song_Name = #next song qued
               current_song_Artist = #next song's artist
               current_song_Length = #next song's length
            elif #song finshes:
                cursor.excecute(""" INSERT INTO HAPPY VALUES ('%s', '%s', '%s');"""(current_song_Name, current_song_Artist,current_song_Length))
                current_song_Name = #next song qued
                current_song_Artist = #next song's artist
                current_song_Length = #next song's length
    elif mood == 2:
        if # skip is presed:
            current_song_Name = #next song qued
            current_song_Artist = #next song's artist
            current_song_Length = #next song's length
        elif #song finshes:
            cursor.excecute(""" INSERT INTO SAD VALUES ('%s', '%s', '%s');"""(current_song_Name, current_song_Artist,current_song_Length))
            current_song_Name = #next song qued
            current_song_Artist = #next song's artist
            current_song_Length = #next song's length
    elif mood == 3: 
        if # skip is presed:
            current_song_Name = #next song qued
            current_song_Artist = #next song's artist
            current_song_Length = #next song's length
        elif #song finshes:
            cursor.excecute(""" INSERT INTO ANGRY VALUES ('%s', '%s', '%s');"""(current_song_Name, current_song_Artist,current_song_Length))
            current_song_Name = #next song qued
            current_song_Artist = #next song's artist
            current_song_Length = #next song's length
    elif mood == 4:
        if # skip is presed:
            current_song_Name = #next song qued
            current_song_Artist = #next song's artist
            current_song_Length = #next song's length
        elif #song finshes:
            cursor.excecute(""" INSERT INTO FOCUSED VALUES ('%s', '%s', '%s');"""(current_song_Name, current_song_Artist,current_song_Length))
            current_song_Name = #next song qued
            current_song_Artist = #next song's artist
            current_song_Length = #next song's length
    elif mood == 5:
        if # skip is presed:
            current_song_Name = #next song qued
            current_song_Artist = #next song's artist
            current_song_Length = #next song's length
        elif #song finshes:
            cursor.excecute(""" INSERT INTO STRESSED VALUES ('%s', '%s', '%s');"""(current_song_Name, current_song_Artist,current_song_Length))
            current_song_Name = #next song qued
            current_song_Artist = #next song's artist
            current_song_Length = #next song's length