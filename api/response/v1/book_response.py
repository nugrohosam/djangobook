import array

class BookResponse():

    def one(bookModel):
        title = bookModel.title
    
    def many(self, booksModel):
        bookArr = array()
        for bookModel in booksModel:
            bookFormated = self.one(bookModel)
            bookArr.append(bookFormated)
        return bookArr
