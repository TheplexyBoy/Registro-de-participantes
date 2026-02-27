amount = int(input("Ingresa el numero de personas a registrar: "))
print(f"El numero de personas a resgistrar es: {amount}")

people = []

for i in range (amount):
    print(f"""
""") 
    print(f"Person {i+1}")
    name = str(input("Enter a name: "))
    while not name.isalpha():
        print("Error please enter a valid name")
        name = str(input("Enter a name again please: "))
    #Age
    age = (int(input("Enter a age: ")))
    while age <= 0:
        print("Error please enter a valid age.")
        age = (int(input("Enter your age again please: ")))
    #Question
    question = str(input("¿Tiene conocimientos básicos de computación? "))
    #Condicionals
    if age >= 15 and question.lower() == "si":
        print("""""")
        print("You participed in workshop")
    else:
        print("""""")
        print("Your not meet the requeriments")
    #Person
    person = {
         "name": name,
        "age": age
    }

    people.append(person)

print("""""")
print("Datos registrados: ")
print(people)
print("""""")
print("Proceso finalizado, gracias por su tiempo :)")

