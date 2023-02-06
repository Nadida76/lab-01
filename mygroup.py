groupmates = [
    {
        "name": "Сениксон Сандро",
        "surname": "Лопеш",
        "exams": ["Информатика", "Философия", "АиГ"],
        "marks": [5, 5, 3]
    },
    {
        "name": "Франк",
        "surname": "Мателама",
        "exams": ["Информатика", "Философия", "АиГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Настия",
        "surname": "Груздева",
        "exams": ["Информатика", "Философия", "АиГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Озил",
        "surname": "Давасурен ",
        "exams": ["Информатика", "Философия", "АиГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Алина",
        "surname": "Золоева",
        "exams": ["Информатика", "Философия", "АиГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Дидо",
        "surname": "Елонго",
        "exams": ["Информатика", "Философия", "АиГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Полин",
        "surname": "Ндзила",
        "exams": ["Информатика", "Философия", "АиГ"],
        "marks": [5, 5, 5]
    }

]

#ljust(15) - é um método de corda que adiciona o número necessário de espaços de modo que o comprimento da corda
# é igual ao parâmetro que está sendo passado. resumindo criacao da tabulacao
def print_students(students):
    print(u"Num".ljust(5), u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(35), u"Оценки".ljust(20))
    i=1
    for student in students:
        print(i,"-".ljust(3), student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
        i = i + 1


print_students(groupmates)#chamada da função


