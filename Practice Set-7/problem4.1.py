class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return len(self.title)
    

book1 = Book("Atomic Habits", "James Clear")
book2 = Book("Deep Woork", "Cal Newport")

print(book1)
print(book2)

print("Length of book1 title: ", len(book1))
print("Length of book2 title: ", len(book2))