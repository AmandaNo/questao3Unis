import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class BMI_Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo de IMC - Índice de Massa Corporal")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.master, text="Nome do Paciente:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.master, text="Endereço Completo:").grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(self.master, text="Peso (kg):").grid(row=2, column=0, padx=10, pady=10)
        ttk.Label(self.master, text="Altura (cm):").grid(row=3, column=0, padx=10, pady=10)

        self.entry_patient_name = ttk.Entry(self.master)
        self.entry_full_address = ttk.Entry(self.master)
        self.entry_weight = ttk.Entry(self.master)
        self.entry_height = ttk.Entry(self.master)

        self.entry_patient_name.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.entry_full_address.grid(row=1, column=1, padx=10, pady=10)
        self.entry_weight.grid(row=2, column=1, padx=10, pady=10)
        self.entry_height.grid(row=3, column=1, padx=10, pady=10)

        ttk.Button(self.master, text="Calcular IMC", command=self.calculate_bmi).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(self.master, text="Reiniciar", command=self.reset_fields).grid(row=5, column=2, columnspan=2, pady=10)
        ttk.Button(self.master, text="Sair", command=self.close_program).grid(row=5, column=4, columnspan=2, pady=10)

        self.frame_result = ttk.Frame(self.master)
        self.frame_result.grid(row=2, column=2, rowspan=2, columnspan=2, pady=10, padx=10)

        self.label_result = ttk.Label(self.frame_result, text="")
        self.label_result.pack(expand=True, fill="both")

    def calculate_bmi(self):
        patient_name = self.entry_patient_name.get()
        full_address = self.entry_full_address.get()

        if not patient_name or not full_address:
            messagebox.showerror("Error", "Favor entrar com os campos Nome e Endereço Completo.")
            return

        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, insira valores numéricos válidos para Peso e Altura.")
            return

        bmi = ((weight * 100) / (height ** 2)) * 100

        if bmi < 17:
            situation = "Muito abaixo do peso"
        elif 17 <= bmi < 18.5:
            situation = "Abaixo do peso"
        elif 18.5 <= bmi < 25:
            situation = "Peso normal "
        elif 25 <= bmi < 30:
            situation = "Acima do peso"
        elif 30 <= bmi < 35:
            situation = "Obesidade I "
        elif 35 <= bmi < 40:
            situation = "Obesidade II (severa)"
        else:
            situation = "Obesidade III (mórbida)"

        result_text = f"{patient_name.upper()}\nIMC: {bmi:.2f}\nSituação: {situation}"
        self.label_result.config(text=result_text)

    def reset_fields(self):
        self.entry_patient_name.delete(0, tk.END)
        self.entry_full_address.delete(0, tk.END)
        self.entry_weight.delete(0, tk.END)
        self.entry_height.delete(0, tk.END)
        self.label_result.config(text="")

    def close_program(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()
