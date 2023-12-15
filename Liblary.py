class liblaryman:
    def __init__(self, bookbor):
        self.bookbor = bookbor
        bookspresent = {
            "python": 50,
            "sudha murti": 70,
            "the toyota way": 80,
            "java": 45,
            "fullstack web devlopment":50
            }
        if bookbor=='b':
            bookname = input("Enter book name to Borrow: ")
            if bookname in bookspresent:
                print(f"here is {bookname}")
                bookspresent.pop(bookname)

            else:
                print("Sorry we don't have that book")
        if bookbor=='r':
            bookname = input("Enter book name to Retrun or to doante: ")
            bookprice = input("Enter book price to Retrun or to doante: ")
            if bookname not in bookspresent:
                bookspresent.update({bookname:bookprice})

            else:
                print("We already have that book")

        if bookbor=='s':
            print(bookspresent)

        if bookbor=='q':
            print("Thanks for using this app")
            quit()

while True:
    thingtodo = input('''Welcome to wonders liblary
        ShowBook(Enter s)
        BorrowBook(Enter b)
        RetrunBookOrToDonate(Enter r)
        Quit(Enter q)''')



    if thingtodo=='q':
            print("Thanks for coming.Please visit again")
            quit()
    caller = liblaryman(thingtodo)
