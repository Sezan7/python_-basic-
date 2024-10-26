x = ( 2, 4 , 53, " nr","kr", "mango")
print(x[3])
print(x.index("mango"))
print(x.count("mango"))
print(len(x))
print("mango" in x)
for y in x :
    print(x)

# ------------------------------------------------------------
students = [
    ("Alice", 101, 95),
    ("Bob", 102, 88),
    ("Charlie", 103, 102)
]
name, roll_no, marks = students[0]
print(f"Name: {name}, Roll No: {roll_no}, Marks: {marks}")

highest_marks = 0
topper_name = ""
topper_roll = ""
for name, roll_no, marks in students:
    if marks > highest_marks:
        highest_marks = marks
        topper_name = name
        topper_roll = roll_no

print(f"Topper: {topper_name} with {highest_marks} marks and roll{roll_no}")

#------------------------------------------------------------------
books = [
    ("The Lord of the Rings", "J.R.R. Tolkien", 1954, "9780547991029"),
    ("Pride and Prejudice", "Jane Austen", 1813, "9780141439485"),
    ("To Kill a Mockingbird", "Harper Lee", 1960, "9780061120084")
]

def search_by_author(author_name):
    for book in books:
        if author_name.lower() in book[1].lower():
            print(book)

def search_by_title(title_part):
    for book in books:
        if title_part.lower() in book[0].lower():
            print(book)

def add_book(title, author, year, isbn):
    books.append((title, author, year, isbn))
    print("Book added successfully!")

# Example usage:
search_by_author("tolkien")
search_by_title("pride")
add_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, "9780345391803")
# print(book)
search_by_author("jane")

''' 

### this is sezans practice * test _______ ___________ __________


def search_by_author(self):
    for book in books:
        if self.lower() in book[1].lower():
            print(book)


search_by_author("jane")

sezan = search_by_author("harper")
print( sezan)

'''
