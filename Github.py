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
    
    def agregar_nota(self, materia, nota):
        if materia in self.materias and len(self.materias[materia]) < 4:
            self.materias[materia].append(nota)
        else:
            print(f"No se puede agregar más notas a {materia} o la materia no existe.")

    def calcular_promedio(self, materia):
        if materia in self.materias and self.materias[materia]:
            return sum(self.materias[materia]) / len(self.materias[materia])
        return 0
    
    def mostrar_registro(self):
        print(f"\nRegistro del estudiante: {self.nombre} {self.apellido} ({self.numero}) - Curso: {self.curso}")
        for materia, notas in self.materias.items():
            promedio = self.calcular_promedio(materia)
            print(f"Materia: {materia} | Notas: {notas} | Promedio: {promedio:.2f}")

# Solicitar datos del estudiante
nombre = input("Nombre del estudiante: ")
apellido = input("Apellido del estudiante: ")
numero = input("Número de estudiante: ")
curso = input("Curso: ")

estudiante = Estudiante(nombre, apellido, numero, curso)


# Pedir notas para cada materia
total_periodos = 4
for materia in estudiante.materias.keys():
    print(f"\nIngresando notas para {materia}")
    for i in range(1, total_periodos + 1):
        while True:
            try:
                nota = float(input(f"Ingrese la nota del periodo {i}: "))
                if 0 <= nota <= 100:
                    estudiante.agregar_nota(materia, nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 100. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada inválida. Ingresa un número válido.")

# Mostrar el registro completo
estudiante.mostrar_registro()
