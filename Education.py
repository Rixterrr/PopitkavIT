def main():
    books = [
    {"title": "Мастер и Маргарита", "author": "Булгаков", "year": 1967, "status": "в наличии"},
    {"title": "Преступление и наказание", "author": "Достоевский", "year": 1866, "status": "в наличии"},
    {"title": "Война и мир", "author": "Толстой", "year": 1869, "status": "выдана"},
    {"title": "Евгений Онегин", "author": "Пушкин", "year": 1833, "status": "в наличии"},
    {"title": "Мёртвые души", "author": "Гоголь", "year": 1842, "status": "выдана"},
    {"title": "Герой нашего времени", "author": "Лермонтов", "year": 1840, "status": "в наличии"},
    {"title": "Отцы и дети", "author": "Тургенев", "year": 1862, "status": "выдана"},
    {"title": "Тихий Дон", "author": "Шолохов", "year": 1940, "status": "в наличии"}
]
    boo(books)



def boo(kniga):
    x = input("Введите название книги: ")
    correct = None
    
    for i in kniga:
        if i["title"].lower() == x.lower():
            correct = i
            break
    if correct is not None:
        if correct["status"] == "выдана":
            print("Книга уже выдана!")
        elif i["status"] == "в наличии":
            print(f"Найдена книга: Название: {correct["title"]}, Автор: {correct["author"]}, Год: {correct["year"]}, Книга выдана!")
    else: print("Введённой книги нет в библиотеке!")

main()