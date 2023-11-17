class liblaryman:
    def __init__(self, bookbor):
        self.bookbor = bookbor
        bookspresent = ["python", "sudha murti", "the toyota way", "java", "fullstack web devlopment"]
        if bookbor=='b':
            bookname = input("Enter book name to Borrow: ")
            if bookname in bookspresent:
                print(f"here is {bookname}")
                bookspresent.remove(bookname)

            else:
                print("Sorry we don't have that book")
        if bookbor=='r':
            bookname = input("Enter book name to Retrun: ")
            if bookname not in bookspresent:
                bookspresent.append(bookname)

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
                  RetrunBook(Enter r)
                  Quit(Enter q)''')



    if thingtodo=='q':
            print("Thanks for coming.Please visit again")
            quit()
    caller = liblaryman(thingtodo)
