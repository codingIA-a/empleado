#crear una clase empleado que tenga los siguientes atributos:
#nombre, id empleado, cargo, salario, departamento, tareas, bonos
#ademas deberá tener los siguientes métodos:
#asignar tarea, completar tareas, mostrar tareas, mostrar info empleado


class Empleado:
    def __init__(self, nombre, id_empleado, cargo, salario, departamento):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.cargo = cargo
        self.salario = salario
        self.departamento = departamento
        self.tareas = []
        self.bonos = 0
    #método asignar tarea
    def asignar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f'Tarea asignada a {self.nombre} : {tarea}\n')
    
    #método mostrar tareas
    def mostrar_tareas(self):
        print(f'Tareas asignadas a {self.nombre}:\n')
        for tarea in self.tareas:
            print(f'-{tarea}')

empleado1 = Empleado('Adán', 1 , 'Desarrollador', 1000, 'TI')
empleado1.asignar_tarea('Formulario Login')
empleado1.mostrar_tareas()
