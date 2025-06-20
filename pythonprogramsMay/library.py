def addbook():
    book_id=int(input("Enter Book_id"))
    if book_id in books:
        print('Already book with id exist')
    else:
        t=input("Enter the title")
        a=input("Enter the author")
        y=int(input("Enter the year"))
        p=int(input("Enter the price"))
        books[book_id]={'title':t,'author':a,'year':y,'price':p}
        print("Added Book details")

def showbooks():
    for i,j in books.items():
        print(i,j)
def showbookdetail():
    book_id=int(input("Enter the book id"))
    if book_id in books:
        print(books[book_id])
    else:
        print("Book does not exist")
def updatebookdetails():
    book_id = int(input("Enter the book id"))
    if book_id in books:
        # attr=input("Enter the attribute to be changed title/author/price/year/all")
        # if attr=="title":
        #     books['title']=input("new title")
        # else:
        #     print('invalid attribute')

        books[book_id]['title']=input("Enter the new title")
        books[book_id]['author']=input("Enter the new author name")
        books[book_id]['year']=int(input("Enter the year"))
        books[book_id]['price']=int(input("Enter the price"))
        print(books)
    else:
        print("Book Does not Exist")

def deletebookdetails():
    book_id=int(input("Enter the book id"))
    if book_id in books:
        books.pop(book_id,None)
    else:
        print("Book does not Exist")




books={}
while(1):

    print("Library Operations")
    print('1.Add Book Details')
    print('2.Show all book details')
    print('3.show a specific book')
    print('4.Update a specific book')
    print('5.Delete a specific book')
    print('6.Exit')


    ch=int(input("Enter the Choice"))
    if ch==1:
        addbook()
        #print(books)
    elif ch==2:
        showbooks()
    elif ch==3:
        showbookdetail()
    elif ch==4:
        updatebookdetails()
    elif ch==5:
        deletebookdetails()
    else:
        exit()
