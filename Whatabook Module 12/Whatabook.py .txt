import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}

#this is where we establish the connection with mysql
db = mysql.connector.connect(**config) 
cursor = db.cursor()


print('HELLO! And Welcome To WhatABook!')

# i only needed to make some defined classes so they can loop into themselves, in hindsite it would have been cleaner to make everything a defined class


def wishlist(userid):
    #We need to connect the wishlist table with the user and book tables
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
        "FROM wishlist " +
        "INNER JOIN user ON wishlist.user_id = user.user_id " + 
        "INNER JOIN book ON wishlist.book_id = book.book_id " + 
        "WHERE user.user_id = {}".format(userid))

        #The output will need to print 'book_id', 'book_name', 'author', and 'details' along with the user tables
    wishlist = cursor.fetchall()

    #this is how we output everything
    for w in wishlist:
        print (f" BookID# :{w[3]}\n Book Name: {w[4]}\n Author: {w[5]}\n")
    usermenu(userid)


def addbooks(userid):
        availableBooks = ("SELECT book_id, book_name, author, details FROM book " +
                          "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(userid))
        
        cursor.execute(availableBooks)

        addable = cursor.fetchall()
        print('Here are the books you can still add to your wishlist')
        for a in addable:
            print(f"\n Book ID: {a[0]}\n Book Name: {a[1]}\n")
        validbook = ['1','2','3','4','5','6','7','8','9']
        add = input('please input the id number of the book: ')
        while add not in validbook:
            print('im sorry that was not one of the options please try again\n')
            addbooks(userid)
        if add in validbook:
            print('ok great choice')
            cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(userid, add))
            usermenu(userid)

  

#this is where the user needs to sign in
def validateuser():
            print('log in by inputing your user id')
            validUserIds = ['1', '2', '3']
            userid = input('valid user ID: 1, 2, or 3 \n')

            while userid not in validUserIds:
                print('im sorry that was not one of the options please try again\n')
                #we need to loop the user until they input a authorized user id
                validateuser()
            if userid in validUserIds:
                print('thank you and welcome')

                #notice we send the 'userid' term to the next definition so it knows hwo we are talking about
                usermenu(userid)


#the user may only end up here once they have been validated
def usermenu(userid):
            menu = {}
            menu ['1:'] = 'My Wishlist'
            menu ['2:'] = 'Add Book to Wishlist'
            menu ['3:'] = 'Main Menu'
            options = menu.keys()
            for entry in options:
                print (entry, menu[entry])
            choice2 = input(': ')

            if choice2 == '1':
                print('\nok here are your wished books\n')
                wishlist(userid)

            if choice2 == '2':
                print('\nwhich book would you ike to add to your list?\n')
                #now add the book into the wishlist database#
                addbooks(userid)

            if choice2 == '3':
                MainMenu()
   
            else:
                print('cant you just follow directions')
                usermenu(userid)


#this is the main hub a user ends up here right when booting up the program
def MainMenu():
    print('what would you like to do?')
    menu = {}
    menu['1']="Veiw Books"
    menu['2']="Veiw Store Locations"
    menu['3']="Log Into My Account"
    menu['4']="Exit Program."
    options = menu.keys()
    for entry in options:
        print (entry, menu[entry])
    choice1 = input(':  ')

    if choice1 == '1':
        print('here is a list of our books at the moment\n')
        #print all books here 
        cursor.execute("SELECT book_id, book_name, author, details FROM book")
        books = cursor.fetchall()
        for b in books:
            print(f" Book ID Number: {b[0]}\n Book Name: {b[1]}\n Book Author: {b[2]}\n Book Details: {b[3]}\n")
        MainMenu()


    if choice1 == '2':
        print('here are our store locations, feel free to stop by\n')
        #print 'store' table
        cursor.execute("SELECT store_id, locale FROM store")
        store = cursor.fetchall()
        for s in store:
            print(f'Store Location: {s[1]}\n')
        MainMenu()

    if choice1 == '3':
        validateuser()

    if choice1 == '4':
        print('\nOk Bye Bye')
        quit()

    if choice1 == '999':
        print('dude I only gave like four options...')
        MainMenu()

    else:
        print('im sorry that is not an option')
        MainMenu()



MainMenu()          