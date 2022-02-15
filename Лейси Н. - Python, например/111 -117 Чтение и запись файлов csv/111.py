
import csv

file = open("Books.csv", "w")
new_record = "To Kill a Mockingbird, Harper Lee, 1960\n"
file.write(str(new_record))
new_record = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(new_record))
new_record = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(new_record))
new_record = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(new_record))
new_record = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(new_record))
file.close()
