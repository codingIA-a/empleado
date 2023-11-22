class Empleado:
    def __init__(self, nombre, id_empleado, cargo, salario, departamento):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.cargo = cargo
        self.salario = salario
        self.departamento = departamento
        self.tareas = []
        self.bonos = 0

    def asignar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f'Tarea asignada a {self.nombre}: {tarea}\n')

    def mostrar_tareas(self):
        print(f'Tareas asignadas a {self.nombre}:\n')
        for tarea in self.tareas:
            print(f'-{tarea}')

    def completar_tareas(self, tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            print(f'{self.nombre.capitalize()} completó la tarea: {tarea}\n')
            self.bonos += self.calcular_bonos_por_tarea()
            
        else:
            print(f'{self.nombre} no tiene asignada la tarea: {tarea}')

    def mostrar_info(self):
        print('*******Info******')
        print(f'Nombre: {self.nombre.capitalize()}')
        print(f'Bonos: {self.bonos}')
        print(f'Salario: {self.salario}')
        print(f'Salario + bonos: {self.salario+self.bonos}')

    @staticmethod
    def calcular_bonos_por_tarea():
        return 10  # Puedes ajustar la cantidad de bonos según tus necesidades

# Ejemplo de uso
empleado1 = Empleado('Adán', 1, 'Desarrollador', 1000, 'TI')
empleado1.asignar_tarea('Formulario Login')
empleado1.asignar_tarea('Formulario Registro')
empleado1.mostrar_tareas()
empleado1.completar_tareas('Formulario Login')
empleado1.completar_tareas('Formulario Registro')
empleado1.mostrar_info()
