import sqlite3
import json
import os
import sys
import pandas as pd

db=sqlite3.connect("yada.db")
iterator=db.cursor()

def createTables():
    try:
        iterator.execute("create table Books (BookID text PRIMARY KEY, titleID text not null, location text not null, genre text )")
        iterator.execute("create table Titles (titleID text not null, title text not null, ISBN text not null, publisherID text not null, publicationYear text, foreign key(titleID) references Books(titleID))")
        iterator.execute("create table publishers (publisherID text not null, name text not null, streetAdd text, suiteno text, zip text, foreign key(publisherID) references Titles(publisherID))")
        iterator.execute("create table AuthorTit (authorTitID text not null, authID text not null, titleID not null, foreign key(titleID) references Titles(titleID))")
        iterator.execute("create table authors (authID text not null , firstName text not null, middleName text , lastName text , foreign key(authID) references AuthorTit(authID))")
        iterator.execute("create table zipCodes (zipCodeID text not null , city text, state text, zipcode text, foreign key(zipCodeID) references publishers(zip))")
        db.commit()
    except sqlite3.OperationalError:
        pass
    finally:
        print "Tables have been created"

def insertInto(tID):
    if(tID==0):
        bookID=raw_input("Enter BookID? ")
        titleID=raw_input("Enter titleID? ")
        location=raw_input("Enter location? ")
        genre=raw_input("Enter genre? ")
        try:
            iterator.execute("insert into Books values (?,?,?,?)",(bookID,titleID,location,genre))
            choice=raw_input("Are you sure (Yes/No) ?")
            if choice=="Yes" or choice=="YES" or choice=="yes": db.commit()
            else: db.rollback()
        except sqlite3.IntegrityError:
            print "Please enter a UNIQUE Primary key or foriegn Key"
    elif(tID==1):
        titleID=raw_input("Enter titleID? ")
        title=raw_input("Enter title? ")
        ISBN=raw_input("Enter ISBN? ")
        publisherID=raw_input("Enter publisherID? ")
        publicationYear=raw_input("Enter publicationYear? ")
        try:
            iterator.execute("insert into Titles values (?,?,?,?,?)",(titleID,title,ISBN,publisherID,publicationYear))
            choice=raw_input("Are you sure (Yes/No) ?")
            if choice=="Yes" or choice=="YES" or choice=="yes": db.commit()
            else: db.rollback()
        except sqlite3.IntegrityError:
            print "Please enter a UNIQUE Primary key or foriegn Key"
    elif(tID==2):
        publisherID=raw_input("Enter publisherID? ")
        name=raw_input("Enter name? ")
        streetAdd=raw_input("Enter street Address? ")
        suiteno=raw_input("Enter Suite Number? ")
        zipx=raw_input("Enter Zip? ")
        try:
            iterator.execute("insert into publishers values (?,?,?,?,?)",(publisherID,name,streetAdd,suiteno,zipx))
            choice=raw_input("Are you sure (Yes/No) ?")
            if choice=="Yes" or choice=="YES" or choice=="yes": db.commit()
            else: db.rollback()
        except sqlite3.IntegrityError:
            print "Please enter a UNIQUE Primary key or foriegn Key"
    elif(tID==3):
        authorTitID=raw_input("Enter Author Title ID? ")
        authID=raw_input("Enter Author ID? ")
        titleID=raw_input("Enter Title ID? ")
        try:
            iterator.execute("insert into AuthorTit values (?,?,?,?,?)",(publisherID,name,streetAdd,suiteno,zipx))
            choice=raw_input("Are you sure (Yes/No) ?")
            if choice=="Yes" or choice=="YES" or choice=="yes": db.commit()
            else: db.rollback()
        except sqlite3.IntegrityError:
            print "Please enter a UNIQUE Primary key or foriegn Key"
    elif(tID==4):
        authID=raw_input("Enter Author ID? ")
        firstName=raw_input("Enter first Name? ")
        middleName=raw_input("Enter middle Name? ")
        lastName=raw_input("Enter last Name? ")
        try:
            iterator.execute("insert into authors values (?,?,?,?)",(authID,firstName,middleName,lastName))
            choice=raw_input("Are you sure (Yes/No) ?")
            if choice=="Yes" or choice=="YES" or choice=="yes": db.commit()
            else: db.rollback()
        except sqlite3.IntegrityError:
            print "Please enter a UNIQUE Primary key or foriegn Key"
    elif(tID==5):
        ZipCodeID=raw_input("Enter Zip Code ID? ")
        city=raw_input("Enter city? ")
        state=raw_input("Enter State? ")
        zipCode=raw_input("Enter Zip Code? ")
        try:
            iterator.execute("insert into zipCodes values(?,?,?,?", (ZipCodeID,city,state,zipCode))
            choice=raw_input("Are you sure (Yes/No) ?")
            if choice=="Yes" or choice=="YES" or choice=="yes": db.commit()
            else: db.rollback()
        except sqlite3.IntegrityError:
            print "Please enter a UNIQUE Primary key or foriegn Key"

def selectFromAllTables(tID):
    try:
        if(tID==0): iterator.execute('select * from Books')
        elif(tID==1): iterator.execute('select * from Titles')
        elif(tID==2): iterator.execute('select * from publishers')
        elif(tID==3): iterator.execute('select * from AuthorTit')
        elif(tID==4): iterator.execute('select * from authors')
        elif(tID==5): iterator.execute('select * from zipCodes')
        print pd.DataFrame(iterator.fetchall())
    except pd.io.sql.DatabaseError , AttributeError:
        print "No such records found"
createTables()
while True:
    print "1. Insert into Tables "
    print "2. Display All Tables "
    print "3. Exit"
    subchoice=int(raw_input("Enter choice? "))
    if subchoice == 3: 
        db.close()
        break
    print "You want to operate on which Table?"
    print "1. Books Table"
    print "2. Titles Table"
    print "3. Publishers Table"
    print "4. Author Table"
    print "5. Authors Table"
    print "6. ZipCodes Table"
    choice=int(raw_input("Enter the table? ")) - 1
    if(subchoice==1): insertInto(choice)
    elif(subchoice==2): selectFromAllTables(choice)
    else: print "Try Again"