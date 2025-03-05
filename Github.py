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

# Registro de estudiantes
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