import psutil
import customtkinter as ctk
import time
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FloatingSystemMonitor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Floating System Monitor")
        self.geometry("300x400")
        self.resizable(False, False)
        self.attributes('-topmost', True)
        self.configure(bg="black")
        self.attributes("-alpha", 0.9)

        self.create_widgets()
        self.start_thread()

    def create_widgets(self):
        self.label_title = ctk.CTkLabel(self, text="System Monitor", font=("Arial", 20, "bold"), text_color="cyan")
        self.label_title.pack(pady=10)

        self.cpu_label = ctk.CTkLabel(self, text="CPU Usage", text_color="white")
        self.cpu_label.pack()
        self.cpu_progress = ctk.CTkProgressBar(self, width=250)
        self.cpu_progress.pack(pady=5)

        self.ram_label = ctk.CTkLabel(self, text="RAM Usage", text_color="white")
        self.ram_label.pack()
        self.ram_progress = ctk.CTkProgressBar(self, width=250, progress_color='green')
        self.ram_progress.pack(pady=5)

        self.memory_label = ctk.CTkLabel(self, text="Memory Used", text_color="white")
        self.memory_label.pack()
        self.memory_progress = ctk.CTkProgressBar(self, width=250, progress_color="blue")
        self.memory_progress.pack(pady=5)

        self.battery_label = ctk.CTkLabel(self, text="Battery", text_color="white")
        self.battery_label.pack()
        self.battery_progress = ctk.CTkProgressBar(self, width=250, progress_color="red")
        self.battery_progress.pack(pady=5)

    def update_stats(self):
        while True:
            cpu_usage = psutil.cpu_percent() / 100
            ram_usage = psutil.virtual_memory().percent / 100
            memory_usage = psutil.virtual_memory().used / psutil.virtual_memory().total  # FIXED HERE ✅
            battery = psutil.sensors_battery().percent / 100 if psutil.sensors_battery() else 0

            self.cpu_progress.set(cpu_usage)
            self.ram_progress.set(ram_usage)
            self.memory_progress.set(memory_usage)
            self.battery_progress.set(battery)

            time.sleep(1)

    def start_thread(self):
        threading.Thread(target=self.update_stats, daemon=True).start()

if __name__ == "__main__":
    app = FloatingSystemMonitor()
    app.mainloop()
