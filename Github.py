class Estudiante:
    def __init__(self, nombre, apellido, numero, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.curso = curso
        self.materias = {
            'Español': [],
            'Naturales': [],
            'Matemáticas': [],
            'Sociales': []
        }
    
    def agregar_notas(self, materia, notas):
        if materia in self.materias:
            if len(self.materias[materia]) == 4:
                print(f"Ya se han ingresado 4 notas para {materia}.")
            else:
                self.materias[materia] = notas
                print(f"Notas agregadas correctamente a {materia}.")

    def calcular_promedio(self, materia):
        if materia in self.materias and len(self.materias[materia]) == 4:
            return sum(self.materias[materia]) / 4
        return 0
    
    def mostrar_registro(self):
        print(f"\nRegistro del estudiante: {self.nombre} {self.apellido} ({self.numero}) - Curso: {self.curso}")
        for materia, notas in self.materias.items():
            promedio = self.calcular_promedio(materia)
            print(f"Materia: {materia} | Notas: {notas} | Promedio: {promedio:.2f}")


registro_estudiantes = []

def agregar_estudiante():
    nombre = input("Nombre del estudiante: ")
    apellido = input("Apellido del estudiante: ")
    numero = input("Número de estudiante: ")
    curso = input("Curso: ")
    estudiante = Estudiante(nombre, apellido, numero, curso)
    registro_estudiantes.append(estudiante)
    print("Estudiante agregado correctamente.")

def seleccionar_estudiante():
    if not registro_estudiantes:
        print("No hay estudiantes registrados.")
        return None
    
    print("\nLista de estudiantes:")
    for i, est in enumerate(registro_estudiantes):
        print(f"{i + 1}. {est.nombre} {est.apellido} ({est.numero})")
    
    while True:
        try:
            opcion = int(input("Selecciona un estudiante por número: "))
            if 1 <= opcion <= len(registro_estudiantes):
                return registro_estudiantes[opcion - 1]
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

def agregar_notas_menu():
    estudiante = seleccionar_estudiante()
    if estudiante:
        print("\nMaterias disponibles:")
        for i, materia in enumerate(estudiante.materias.keys()):
            print(f"{i + 1}. {materia}")
        
        while True:
            try:
                opcion = int(input("Selecciona una materia por número: "))
                materias_lista = list(estudiante.materias.keys())
                if 1 <= opcion <= len(materias_lista):
                    materia_seleccionada = materias_lista[opcion - 1]
                    notas = []
                    for i in range(1, 5):
                        while True:
                            try:
                                nota = float(input(f"Ingrese la nota del periodo {i} para {materia_seleccionada}: "))
                                if 0 <= nota <= 100:
                                    notas.append(nota)
                                    break
                                else:
                                    print("La nota debe estar entre 0 y 100.")
                            except ValueError:
                                print("Entrada inválida. Ingresa un número válido.")
                    estudiante.agregar_notas(materia_seleccionada, notas)
                    break
                else:
                    print("Número fuera de rango.")
            except ValueError:
                print("Entrada inválida. Ingresa un número válido.")

def mostrar_registros():
    if not registro_estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    for estudiante in registro_estudiantes:
        estudiante.mostrar_registro()
        print("-" * 40)

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar estudiante")
        print("2. Agregar notas a un estudiante")
        print("3. Mostrar registros de estudiantes")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            agregar_notas_menu()
        elif opcion == "3":
            mostrar_registros()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


menu()
