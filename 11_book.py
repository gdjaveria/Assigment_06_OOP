# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method 
# increment_book_count() to increase the count when a new book is added.

class Book:
   total_book = 0

   @classmethod
   def book_increment_count(cls):
      cls.total_book += 1

Book.book_increment_count()
Book.book_increment_count()
Book.book_increment_count()
print("Total books:", Book.total_book)



    
        