try:
    marks = {"Alice": 80, "John": 65, "Mark": 95, "Sandra": 60, "Micheal": 45}

    while True:

        name = input("Enter student name")

        if name in marks:
            print(f"{name} marks is {marks[name]}")

        score = (marks[name])
        if 80 <= (score) <= 100:
            print('A')
        elif 69 <= (score) <= 79:
            print('B')
        elif 60 <= (score) <= 68:
            print('C')
        elif 49 <= (score) <= 59:
            print('D')
        else:
            print('F')
        break
except KeyError:
    print('Name not found')
    

    

