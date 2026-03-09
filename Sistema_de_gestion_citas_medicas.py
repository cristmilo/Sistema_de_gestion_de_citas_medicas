import tkinter as tk
from tkinter import messagebox
from tkinter import ttk




class Paciente:
    def __init__(self, id_paciente, nombre, apellido, telefono):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono


class Medico:
    def __init__(self, id_medico, nombre, especialidad):
        self.id_medico = id_medico
        self.nombre = nombre
        self.especialidad = especialidad


class Cita:
    def __init__(self, paciente, medico, fecha):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha


class SistemaHospital:

    def __init__(self):
        self.pacientes = []
        self.medicos = []
        self.citas = []

    def registrar_paciente(self, id_paciente, nombre, apellido, telefono):

        paciente = Paciente(id_paciente, nombre, apellido, telefono)
        self.pacientes.append(paciente)

    def registrar_medico(self, id_medico, nombre, especialidad):

        medico = Medico(id_medico, nombre, especialidad)
        self.medicos.append(medico)

    def agendar_cita(self, id_paciente, id_medico, fecha):

        paciente = None
        medico = None

        for p in self.pacientes:
            if p.id_paciente == id_paciente:
                paciente = p

        for m in self.medicos:
            if m.id_medico == id_medico:
                medico = m

        if paciente and medico:
            cita = Cita(paciente, medico, fecha)
            self.citas.append(cita)
            return True
        else:
            return False

    def obtener_citas(self):
        return self.citas



class App:


    def __init__(self, root):

        self.root = root
        self.sistema = SistemaHospital()

        self.root.title("SISTEMA HOSPITAL")
        self.root.geometry("800x400")

        self.crear_pestañas()


    def crear_pestañas(self):

        notebook = ttk.Notebook(self.root)

        self.tab1 = ttk.Frame(notebook)
        self.tab2 = ttk.Frame(notebook)
        self.tab3 = ttk.Frame(notebook)
        self.tab4 = ttk.Frame(notebook)

        notebook.add(self.tab1, text="Registrar Paciente")
        notebook.add(self.tab2, text="Registrar Medico")
        notebook.add(self.tab3, text="Agendar Cita")
        notebook.add(self.tab4, text="Mostrar Citas")

        notebook.pack(expand=True, fill="both")

        self.pestaña_paciente()
        self.pestaña_medico() 
        self.pestaña_cita()
        self.pestaña_mostrar_citas()   



    def pestaña_paciente(self):

        titulo = tk.Label(self.tab1,
                        text="DATOS PACIENTE",
                        font=("Arial", 16, "bold"),
                        fg="blue")

        titulo.pack(pady=20)

        form_frame = tk.Frame(self.tab1)
        form_frame.pack(pady=20, anchor="w", padx=50)

        tk.Label(form_frame, text="ID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.ID_Paciente = tk.Entry(form_frame, width=25)
        self.ID_Paciente.grid(row=1, column=1)

        tk.Label(form_frame, text="Nombre:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.Nombre = tk.Entry(form_frame, width=25)
        self.Nombre.grid(row=2, column=1)

        tk.Label(form_frame, text="Apellido:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.Apellido = tk.Entry(form_frame, width=25)
        self.Apellido.grid(row=3, column=1)

        tk.Label(form_frame, text="Telefono:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=10, pady=10)
        self.Telefono = tk.Entry(form_frame, width=25)
        self.Telefono.grid(row=4, column=1)

        button_frame = tk.Frame(self.tab1)
        button_frame.pack(pady=20)

        btn_save = tk.Button(button_frame,text="Guardar", font=("Arial", 12), bg="#4CAF50", width=10, command=self.guardar_paciente)
        btn_save.pack()

  

    def guardar_paciente(self):

        self.sistema.registrar_paciente(
            self.ID_Paciente.get(),
            self.Nombre.get(),
            self.Apellido.get(),
            self.Telefono.get()
        )

        messagebox.showinfo("Exito", "Paciente registrado")





    def pestaña_medico(self):

        titulo = tk.Label(self.tab2,
                        text="DATOS MEDICO",
                        font=("Arial", 16, "bold"),
                        fg="blue")

        titulo.pack(pady=20)

        form_frame = tk.Frame(self.tab2)
        form_frame.pack(pady=20, anchor="w", padx=50)

        tk.Label(form_frame, text="ID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.ID_Medico = tk.Entry(form_frame, width=25)
        self.ID_Medico.grid(row=1, column=1)

        tk.Label(form_frame, text="Nombre:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.Nombre = tk.Entry(form_frame, width=25)
        self.Nombre.grid(row=2, column=1)

        tk.Label(form_frame, text="Especialidad:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.Especialidad = tk.Entry(form_frame, width=25)
        self.Especialidad.grid(row=3, column=1)
    
        button_frame = tk.Frame(self.tab2)
        button_frame.pack(pady=20)

        btn_save = tk.Button(button_frame,text="Guardar", font=("Arial", 12), bg="#4CAF50", width=10, command=self.guardar_medico)
        btn_save.pack()

  

    def guardar_medico(self):

        self.sistema.registrar_medico(
            self.ID_Medico.get(),
            self.Nombre.get(),
            self.Especialidad.get(),
            
        )

        messagebox.showinfo("Exito", "Medico registrado")




    def pestaña_cita(self):

        titulo = tk.Label(self.tab3,
                        text="AGENDA CITA",
                        font=("Arial", 16, "bold"),
                        fg="blue")

        titulo.pack(pady=20)

        form_frame = tk.Frame(self.tab3)
        form_frame.pack(pady=20, anchor="w", padx=50)

        tk.Label(form_frame, text="ID Paciente:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.ID_paciente = tk.Entry(form_frame, width=25)
        self.ID_paciente.grid(row=1, column=1)

        tk.Label(form_frame, text="ID Medico:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.ID_medico= tk.Entry(form_frame, width=25)
        self.ID_medico.grid(row=2, column=1)

        tk.Label(form_frame, text="Fecha:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.Fecha = tk.Entry(form_frame, width=25)
        self.Fecha.grid(row=3, column=1)
    
        button_frame = tk.Frame(self.tab3)
        button_frame.pack(pady=20)

        btn_save = tk.Button(button_frame,text="Agendar", font=("Arial", 12), bg="#4CAF50", width=10, command=self.agendar_cita)
        btn_save.pack()

  
    def agendar_cita(self):

        exito = self.sistema.agendar_cita(
           self.ID_paciente.get(),
           self.ID_medico.get(),
           self.Fecha.get()
        )

        if exito:
                messagebox.showinfo("Exito", "Cita agendada correctamente")
        else:
                messagebox.showerror("Error", "Paciente o medico no encontrado")



    def pestaña_mostrar_citas(self):

        titulo = tk.Label(self.tab4, text="LISTA DE CITAS", font=("Arial", 16, "bold"), fg="blue")
        titulo.pack(pady=20)

        boton = tk.Button(self.tab4,text="Mostrar Citas",font=("Arial", 12), command=self.mostrar_citas)
        boton.pack(pady=10)

        self.texto_citas = tk.Text(self.tab4, width=80, height=15)
        self.texto_citas.pack(pady=10)


    def mostrar_citas(self):

        citas = self.sistema.obtener_citas()

        self.texto_citas.delete("1.0", tk.END)

        if len(citas) == 0:
            self.texto_citas.insert(tk.END, "No hay citas registradas\n")
            return

        for cita in citas:

            texto = (
                f"Paciente: {cita.paciente.nombre} {cita.paciente.apellido} | "
                f"Medico: {cita.medico.nombre} | "
                f"Fecha: {cita.fecha}\n"
            )

            self.texto_citas.insert(tk.END, texto)




root = tk.Tk()
app = App(root)
root.mainloop() 