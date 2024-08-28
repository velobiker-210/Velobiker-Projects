from tkinter import *
from tkinter import ttk
import psutil as pt
from datetime import date
from ctypes import windll
from string import ascii_uppercase as au
import time, sys


class CPU_Bar:
    def __init__(self):
        self.num_of_physical_cores = pt.cpu_count(logical=FALSE)
        self.num_of_logical_cores = pt.cpu_count()
        
        
    def cpu_percents(self):
        return pt.cpu_percent(percpu=TRUE)
    
    
    def get_ram_usage(self):
        return pt.virtual_memory()
    
    
class Disks:
    def __init__(self):
        self.drives = self.get_local_drives()
        self.deal_with_disks()
        
        
    def get_local_drives(self):
        drives = []
        b = windll.kernel32.GetLogicalDrives()
        for i in au:
            if b & 1:
                drives.append(i)
            b >>= 1
        return drives
    
    
    def deal_with_disks(self):
        for i in self.drives:
            try:
                s = pt.disk_usage(f"{i}:\\")
            except PermissionError:
                self.drives.remove(i)                


class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self["bg"] = "#000000"
        self.title("CPU, Disk, RAM Usage Monitor Bar")
        self.resizable(FALSE, FALSE)
        self.overrideredirect(TRUE)
        self.attributes("-topmost", TRUE)
        self.exit_but_text = "Exit"
        self.date_time_fr_text = "DATE & TIME"
        self.qf_frame_text = "QUICK FUNCTIONS"
        self.language_lab_text = "Language"
        self.time_format_lab_text = "Time Format"
        self.modes_lab_text = "Mode"
        self.list_modes = ["Light", "Dark"]
        self.cpu_frame_text = "CPU CORES' USAGES"
        self.disk_frame_text = "DISKS' USAGES"
        self.ram_frame_text = "RAM USAGE"
        self.disk_name_title_text = "Disk Name"
        self.total_disk_title_text = "Total, GB"
        self.percent_disk_title_text = "Percent"
        self.used_disk_title_text = "Used, GB"
        self.free_disk_title_text = "Free, GB"
        self.ram_total_text = "Total, MB"
        self.ram_percent_text = "Percent"
        self.ram_used_text = "Used, MB"
        self.ram_free_text = "Free, MB"
        self.time_format = 1
        self.cpu = CPU_Bar()
        self.disks = Disks()
        self.mode = 1
        self.lang = 0
        self.launch()
        
        
    def launch(self):
        self.loading()
        self.update()
        time.sleep(2.3)
        self.clear_win()
        self.update()
        time.sleep(2.3)
        self.set_ui()
        self.update()
        
        
    def loading(self):
        self.exit_but = Button(self, text=self.exit_but_text,
                               font=("SF Pro Display", "24"),
                               foreground="#ffffff", background="#ff0000",
                               command=None)
        self.exit_but.pack(fill=X)
        self.date_time_fr = LabelFrame(self, text=self.date_time_fr_text,
                                       font=("SF Pro Display", "18"),
                                       foreground="#6a6a6a", background="#000000")
        self.date_time_fr.pack(fill=X)
        
        self.date_lab = Label(self.date_time_fr, text="88-08-8888",
                              font=("Digital-7 Mono", "36"),
                              foreground="#ff0000", background="#000000",
                              width="12")
        self.date_lab.pack(side=LEFT)
        
        self.time_lab = Label(self.date_time_fr, text="88:88:88",
                              font=("Digital-7 Mono", "36"),
                              foreground="#ff0000", background="#000000",
                              width="10")
        self.time_lab.pack(side=LEFT) 
        
        self.am_pm = Frame(self.date_time_fr, background="#000000")
        self.am_pm.pack(side=LEFT)
        
        self.am, self.pm = Label(self.am_pm, text="AM", 
                                 font=("SF Pro Display", "14"),
                                 foreground="#ff0000", background="#000000",
                                 width="3"), \
            Label(self.am_pm, text="PM", font=("SF Pro Display", "14"),
                  foreground="#ff0000", background="#000000",
                  width="3")
        self.am.pack(side=TOP);  self.pm.pack(side=BOTTOM)
        
        self.qf_frame = LabelFrame(self, text=self.qf_frame_text,
                                   font=("SF Pro Display", "18"),
                                   foreground="#6a6a6a", background="#000000")
        self.qf_frame.pack(fill=X)
        
        self.func1 = Frame(self.qf_frame, background="#000000")
        self.func1.pack(side=TOP, fill=X, expand=TRUE)
        self.language_lab = Label(self.func1, text=self.language_lab_text,
                                  font=("SF Pro Display", "24"),
                                  foreground="#ffffff", background="#000000",
                                  justify=LEFT, anchor=W)
        self.language_lab.pack(side=LEFT)
        
        self.languages_win = ttk.Combobox(self.func1, 
                                          values=["English", "Deutsch",
                                                  "Français", "Español",
                                                  "Italiano", "Ελληνικά",
                                                  "Български", "Беларуская",
                                                  "Қазақша", "Македонски", 
                                                  "Српски", "Татарча",
                                                  "中文", "Հայերեն"],
                                          state="disabled", 
                                          font=("SF Pro Display", "24"),
                                          width="10")
        self.languages_win.current(0)
        self.languages_win.pack(side=RIGHT)
        
        self.func2 = Frame(self.qf_frame, background="#000000")
        self.func2.pack(side=TOP, fill=X, expand=TRUE)
        
        self.time_format_lab = Label(self.func2, text=self.time_format_lab_text,
                                     font=("SF Pro Display", "24"),
                                     foreground="#ffffff", background="#000000",
                                     justify=LEFT, anchor=W)
        self.time_format_lab.pack(side=LEFT)   
        
        self.time_formats = ttk.Combobox(self.func2, values=["12 h.", "24 h."],
                                         state="disabled", 
                                         font=("SF Pro Display", "24"),
                                         width="4")
        self.time_formats.current(1)
        self.time_formats.pack(side=RIGHT)
        
        self.func3 = Frame(self.qf_frame, background="#000000")
        self.func3.pack(side=TOP, fill=X, expand=TRUE)
        
        self.modes_lab = Label(self.func3, text=self.modes_lab_text,
                               font=("SF Pro Display", "24"),
                               foreground="#ffffff", background="#000000",
                               justify=LEFT, anchor=W)
        self.modes_lab.pack(side=LEFT)
        
        self.modes = ttk.Combobox(self.func3, values=self.list_modes,
                                  state="disabled", 
                                  font=("SF Pro Display", "24"),
                                  width="12")
        self.modes.current(1)
        self.modes.pack(side=RIGHT)
        
        self.cpu_frame = LabelFrame(self, text=self.cpu_frame_text,
                                    font=["SF Pro Display", "18"],
                                    foreground="#6a6a6a",
                                    background="#000000")
        self.cpu_frame.pack(fill=BOTH)
        
        self.list_frames = [Frame(self.cpu_frame, background="#000000")
                            for i in range(self.cpu.num_of_physical_cores)]
        
        self.list_num_cores = [Label(self.list_frames[i], text=i+1,
                                     font=["Digital-7 Mono", "36"],
                                     foreground="#ff0000", background="#000000",
                                     justify=LEFT, anchor=CENTER)
                               for i in range(self.cpu.num_of_physical_cores)]
        
        self.list_percent_cores = [Label(self.list_frames[i], text='188.88%',
                                   font=["Digital-7 Mono", "36"],
                                   foreground="#ff0000", background="#000000",
                                   justify=RIGHT, anchor=E, width="8")
                                   for i in range(self.cpu.num_of_physical_cores)]
        
        for i in self.list_frames:
            i.pack(side=TOP, fill=X, expand=TRUE)
        
        for i in self.list_num_cores:
            i.pack(side=LEFT)
            
        for i in self.list_percent_cores:
            i.pack(side=RIGHT) 
            
        self.disk_frame = LabelFrame(self, text=self.disk_frame_text,
                                     font=["SF Pro Display", "18"],
                                     foreground="#6a6a6a",
                                     background="#000000")
        self.disk_frame.pack(fill=BOTH)
            
        self.subs = Frame(self.disk_frame, background='#000000')
        self.subs.pack(side=TOP, fill=X, expand=TRUE)
        
        self.disk_name_title = Label(self.subs, text=self.disk_name_title_text,
                                     font=("SF Pro Display", "22"),
                                     foreground="#ff0000", background="#000000",
                                     width="12")
        self.disk_name_title.pack(side=LEFT)
            
        self.total_disk_title = Label(self.subs, text=self.total_disk_title_text,
                                      font=("SF Pro Display", "22"),
                                      foreground="#ff0000", background="#000000",
                                      width="12")
        self.total_disk_title.pack(side=LEFT)
            
        self.percent_disk_title = Label(self.subs, text=self.percent_disk_title_text,
                                        font=("SF Pro Display", "22"),
                                        foreground="#ff0000", background="#000000",
                                        width="11")
        self.percent_disk_title.pack(side=LEFT)
            
        self.used_disk_title = Label(self.subs, text=self.used_disk_title_text,
                                     font=("SF Pro Display", "22"),
                                     foreground="#ff0000", background="#000000",
                                     width="12")
        self.used_disk_title.pack(side=LEFT)
            
        self.free_disk_title = Label(self.subs, text=self.free_disk_title_text,
                                     font=("SF Pro Display", "22"),
                                     foreground="#ff0000", background="#000000",
                                     width="12")
        self.free_disk_title.pack(side=LEFT)  
        
        self.frames_list_disks = [Frame(self.disk_frame, bg="#000000")
                                  for i in range(len(self.disks.drives))]
        for i in self.frames_list_disks:
            i.pack(side=TOP, fill=X, expand=TRUE)
            
        self.disk_names = [Label(self.frames_list_disks[i], 
                                 text=self.disks.drives[i],
                                 font=("Digital-7 Mono", "36"),
                                 foreground="#ff0000", background="#000000",
                                 width="8")
                           for i in range(len(self.disks.drives))]
        
        self.disk_totals = [Label(self.frames_list_disks[i], 
                                  text="88888.88",
                                  font=("Digital-7 Mono", "36"),
                                  foreground="#ff0000", background="#000000",
                                  width="9", justify=RIGHT, anchor=E)
                            for i in range(len(self.disks.drives))]
        
        self.disk_percents = [Label(self.frames_list_disks[i], 
                                    text="188.88",
                                    font=("Digital-7 Mono", "36"),
                                    foreground="#ff0000", background="#000000",
                                    width="7", justify=RIGHT, anchor=E)
                              for i in range(len(self.disks.drives))]  
        
        self.disk_uses = [Label(self.frames_list_disks[i], 
                                text="88888.88",
                                font=("Digital-7 Mono", "36"),
                                foreground="#ff0000", background="#000000",
                                width="10", justify=RIGHT, anchor=E)
                          for i in range(len(self.disks.drives))] 
        
        self.disk_free = [Label(self.frames_list_disks[i], 
                                text="88888.88",
                                font=("Digital-7 Mono", "36"),
                                foreground="#ff0000", background="#000000",
                                width="9", justify=RIGHT, anchor=E)
                          for i in range(len(self.disks.drives))]         
               
        for i in self.disk_names:
            i.pack(side=LEFT)
            
        for i in self.disk_totals:
            i.pack(side=LEFT) 
            
        for i in self.disk_percents:
            i.pack(side=LEFT)  
            
        for i in self.disk_uses:
            i.pack(side=LEFT)   
            
        for i in self.disk_free:
            i.pack(side=LEFT)

        self.ram_frame = LabelFrame(self, text=self.ram_frame_text,
                                    font=["SF Pro Display", "18"],
                                    foreground="#6a6a6a", background="#000000")
        self.ram_frame.pack(fill=BOTH)

        self.ram_usual_frames = [Frame(self.ram_frame, background="#000000")
                                 for i in range(4)]
        for i in self.ram_usual_frames:
            i.pack(side=TOP, fill=X, expand=TRUE)

        self.ram_total = Label(self.ram_usual_frames[0], text=self.ram_total_text,
                               font=["SF Pro Display", "22"], foreground="#ffffff",
                               background="#000000")
        self.ram_total.pack(side=LEFT)

        self.ram_total_value = Label(self.ram_usual_frames[0], text="888888.88",
                                     font=["Digital-7 Mono", "36"], foreground="#ff0000",
                                     background="#000000", justify=RIGHT, anchor=E)
        self.ram_total_value.pack(side=RIGHT)

        self.ram_percent = Label(self.ram_usual_frames[1], text=self.ram_percent_text,
                                 font=["SF Pro Display", "22"], foreground="#ffffff",
                                 background="#000000")
        self.ram_percent.pack(side=LEFT)

        self.ram_percent_value = Label(self.ram_usual_frames[1], text="188.88",
                                       font=["Digital-7 Mono", "36"], foreground="#ff0000",
                                       background="#000000", justify=RIGHT, anchor=E)
        self.ram_percent_value.pack(side=RIGHT)

        self.ram_used = Label(self.ram_usual_frames[2], text=self.ram_used_text,
                              font=["SF Pro Display", "22"], foreground="#ffffff",
                              background="#000000")
        self.ram_used.pack(side=LEFT)

        self.ram_used_value = Label(self.ram_usual_frames[2], text="888888.88",
                                    font=["Digital-7 Mono", "36"], foreground="#ff0000",
                                    background="#000000", justify=RIGHT, anchor=E)
        self.ram_used_value.pack(side=RIGHT)

        self.ram_free = Label(self.ram_usual_frames[3], text=self.ram_free_text,
                               font=["SF Pro Display", "22"], foreground="#ffffff",
                               background="#000000")
        self.ram_free.pack(side=LEFT)

        self.ram_free_value = Label(self.ram_usual_frames[3], text="888888.88",
                                     font=["Digital-7 Mono", "36"], foreground="#ff0000",
                                     background="#000000", justify=RIGHT, anchor=E)
        self.ram_free_value.pack(side=RIGHT)
        
        
    def set_ui(self):
        self.exit_but = Button(self, text=self.exit_but_text,
                               font=["SF Pro Display", "24"],
                               foreground="#ffffff", background="#ff0000",
                               command=self.app_exit,
                               activeforeground="#ffffff", 
                               activebackground="#ff0000")
        self.exit_but.pack(fill=X)
        self.date_time_fr = LabelFrame(self, text=self.date_time_fr_text,
                                       font=["SF Pro Display", "18"],
                                       foreground="#6a6a6a", background="#000000")
        self.date_time_fr.pack(fill=X)
        
        self.date_lab = Label(self.date_time_fr, text="88-08-8888",
                              font=["Digital-7 Mono", "36"],
                              foreground="#ff0000", background="#000000",
                              width="12")
        self.date_lab.pack(side=LEFT)
        
        self.time_lab = Label(self.date_time_fr, text="88:88:88",
                              font=["Digital-7 Mono", "36"],
                              foreground="#ff0000", background="#000000",
                              width="10")
        self.time_lab.pack(side=LEFT) 
        
        self.am_pm = Frame(self.date_time_fr, background="#000000")
        self.am_pm.pack(side=LEFT)
        
        self.am, self.pm = Label(self.am_pm, text="AM", 
                                 font=["SF Pro Display", "14"],
                                 foreground="#ff0000", background="#000000",
                                 width="3"), \
            Label(self.am_pm, text="PM", font=["SF Pro Display", "14"],
                  foreground="#ff0000", background="#000000",
                  width="3")
        self.am.pack(side=TOP);  self.pm.pack(side=BOTTOM)
        
        self.qf_frame = LabelFrame(self, text=self.qf_frame_text,
                                   font=["SF Pro Display", "18"],
                                   foreground="#6a6a6a", background="#000000")
        self.qf_frame.pack(fill=X)
        
        self.func1 = Frame(self.qf_frame, background="#000000")
        self.func1.pack(side=TOP, fill=X, expand=TRUE)
        self.language_lab = Label(self.func1, text=self.language_lab_text,
                                  font=["SF Pro Display", "24"],
                                  foreground="#ffffff", background="#000000",
                                  justify=LEFT, anchor=W)
        self.language_lab.pack(side=LEFT)
        
        self.languages_win = ttk.Combobox(self.func1, 
                                          values=["English", "Deutsch",
                                                  "Français", "Español",
                                                  "Italiano", "Ελληνικά",
                                                  "Български", "Беларуская",
                                                  "Қазақша", "Македонски", 
                                                  "Српски", "Татарча",
                                                  "中文", "Հայերեն"],
                                          state="readonly", 
                                          font=["SF Pro Display", "24"],
                                          width="10")
        self.languages_win.current(0)
        self.languages_win.bind("<<ComboboxSelected>>", self.change_language)
        self.languages_win.pack(side=RIGHT)
        
        self.func2 = Frame(self.qf_frame, background="#000000")
        self.func2.pack(side=TOP, fill=X, expand=TRUE)
        
        self.time_format_lab = Label(self.func2, text=self.time_format_lab_text,
                                     font=["SF Pro Display", "24"],
                                     foreground="#ffffff", background="#000000",
                                     justify=LEFT, anchor=W)
        self.time_format_lab.pack(side=LEFT)   
        
        self.time_formats = ttk.Combobox(self.func2, values=["12 h.", "24 h."],
                                         state="readonly", 
                                         font=["SF Pro Display", "24"],
                                         width="4")
        self.time_formats.current(1)
        self.time_formats.bind("<<ComboboxSelected>>", self.change_format)
        self.time_formats.pack(side=RIGHT)
        
        self.func3 = Frame(self.qf_frame, background="#000000")
        self.func3.pack(side=TOP, fill=X, expand=TRUE)
        
        self.modes_lab = Label(self.func3, text=self.modes_lab_text,
                               font=["SF Pro Display", "24"],
                               foreground="#ffffff", background="#000000",
                               justify=LEFT, anchor=W)
        self.modes_lab.pack(side=LEFT)
        
        self.modes = ttk.Combobox(self.func3, values=self.list_modes,
                                  state="readonly", 
                                  font=["SF Pro Display", "24"],
                                  width="12")
        self.modes.current(1)
        self.modes.bind("<<ComboboxSelected>>", self.change_mode)
        self.modes.pack(side=RIGHT)
        
        self.cpu_bar() 
        self.disk_bar()
        self.ram_bar()
        self.configure_date_and_time()
        
        
    def cpu_bar(self):
        self.cpu_frame = LabelFrame(self, text=self.cpu_frame_text,
                                    font=["SF Pro Display", "18"],
                                    foreground="#6a6a6a",
                                    background="#000000")
        self.cpu_frame.pack(fill=BOTH)
        
        self.list_frames = [Frame(self.cpu_frame, background="#000000")
                            for i in range(self.cpu.num_of_physical_cores)]
        
        self.list_num_cores = [Label(self.list_frames[i], text=i+1,
                                     font=["Digital-7 Mono", "36"],
                                     foreground="#ff0000", background="#000000",
                                     justify=LEFT, anchor=CENTER)
                               for i in range(self.cpu.num_of_physical_cores)]
        
        self.list_percent_cores = [Label(self.list_frames[i], text='188.88%',
                                   font=["Digital-7 Mono", "36"],
                                   foreground="#ff0000", background="#000000",
                                   justify=RIGHT, anchor=E, width="8")
                                   for i in range(self.cpu.num_of_physical_cores)]
        
        for i in self.list_frames:
            i.pack(side=TOP, fill=X, expand=TRUE)
        
        for i in self.list_num_cores:
            i.pack(side=LEFT)
            
        for i in self.list_percent_cores:
            i.pack(side=RIGHT)           
        self.configure_cpu_bar()
        
        
    def disk_bar(self):
        self.disk_frame = LabelFrame(self, text=self.disk_frame_text,
                                     font=["SF Pro Display", "18"],
                                     foreground="#6a6a6a",
                                     background="#000000")
        self.disk_frame.pack(fill=BOTH)
        
        self.subs = Frame(self.disk_frame, background='#000000')
        self.subs.pack(side=TOP, fill=X, expand=TRUE)
        self.disk_name_title = Label(self.subs, text=self.disk_name_title_text,
                                     font=("SF Pro Display", "22"),
                                     foreground="#ff0000", background="#000000",
                                     width="12")
        self.disk_name_title.pack(side=LEFT)
        
        self.total_disk_title = Label(self.subs, text=self.total_disk_title_text,
                                      font=("SF Pro Display", "22"),
                                      foreground="#ff0000", background="#000000",
                                      width="12")
        self.total_disk_title.pack(side=LEFT)
        
        self.percent_disk_title = Label(self.subs, text=self.percent_disk_title_text,
                                        font=("SF Pro Display", "22"),
                                        foreground="#ff0000", background="#000000",
                                        width="11")
        self.percent_disk_title.pack(side=LEFT)
        
        self.used_disk_title = Label(self.subs, text=self.used_disk_title_text,
                                     font=("SF Pro Display", "22"),
                                     foreground="#ff0000", background="#000000",
                                     width="12")
        self.used_disk_title.pack(side=LEFT)
        
        self.free_disk_title = Label(self.subs, text=self.free_disk_title_text,
                                     font=("SF Pro Display", "22"),
                                     foreground="#ff0000", background="#000000",
                                     width="12")
        self.free_disk_title.pack(side=LEFT)        
        
        self.frames_list_disks = [Frame(self.disk_frame, bg="#000000")
                                  for i in range(len(self.disks.drives))]
        for i in self.frames_list_disks:
            i.pack(side=TOP, fill=X, expand=TRUE)
            
        self.disk_names = [Label(self.frames_list_disks[i], 
                                 text=self.disks.drives[i],
                                 font=("Digital-7 Mono", "36"),
                                 foreground="#ff0000", background="#000000",
                                 width="8")
                           for i in range(len(self.disks.drives))]
        
        self.disk_totals = [Label(self.frames_list_disks[i], 
                                  text="88888.88",
                                  font=("Digital-7 Mono", "36"),
                                  foreground="#ff0000", background="#000000",
                                  width="9", justify=RIGHT, anchor=E)
                            for i in range(len(self.disks.drives))]
        
        self.disk_percents = [Label(self.frames_list_disks[i], 
                                    text="188.88",
                                    font=("Digital-7 Mono", "36"),
                                    foreground="#ff0000", background="#000000",
                                    width="7", justify=RIGHT, anchor=E)
                              for i in range(len(self.disks.drives))]
        self.disk_uses = [Label(self.frames_list_disks[i], 
                                text="88888.88",
                                font=("Digital-7 Mono", "36"),
                                foreground="#ff0000", background="#000000",
                                width="10", justify=RIGHT, anchor=E)
                          for i in range(len(self.disks.drives))]
        
        self.disk_free = [Label(self.frames_list_disks[i], 
                                text="88888.88",
                                font=("Digital-7 Mono", "36"),
                                foreground="#ff0000", background="#000000",
                                width="9", justify=RIGHT, anchor=E)
                          for i in range(len(self.disks.drives))]        
        
        for i in self.disk_names:
            i.pack(side=LEFT)
            
        for i in self.disk_totals:
            i.pack(side=LEFT)
            
        for i in self.disk_percents:
            i.pack(side=LEFT)
            
        for i in self.disk_uses:
            i.pack(side=LEFT)
            
        for i in self.disk_free:
            i.pack(side=LEFT)            
        self.configure_disk_bar()


    def ram_bar(self):
        self.ram_frame = LabelFrame(self, text=self.ram_frame_text,
                                    font=["SF Pro Display", "18"],
                                    foreground="#6a6a6a", background="#000000")
        self.ram_frame.pack(fill=BOTH)

        self.ram_usual_frames = [Frame(self.ram_frame, background="#000000")
                                 for i in range(4)]
        for i in self.ram_usual_frames:
            i.pack(side=TOP, fill=X, expand=TRUE)

        self.ram_total = Label(self.ram_usual_frames[0], text=self.ram_total_text,
                               font=["SF Pro Display", "22"], foreground="#ffffff",
                               background="#000000")
        self.ram_total.pack(side=LEFT)

        self.ram_total_value = Label(self.ram_usual_frames[0], text="888888.88",
                                     font=["Digital-7 Mono", "36"], foreground="#ff0000",
                                     background="#000000", justify=RIGHT, anchor=E)
        self.ram_total_value.pack(side=RIGHT)

        self.ram_percent = Label(self.ram_usual_frames[1], text=self.ram_percent_text,
                                 font=["SF Pro Display", "22"], foreground="#ffffff",
                                 background="#000000")
        self.ram_percent.pack(side=LEFT)

        self.ram_percent_value = Label(self.ram_usual_frames[1], text="188.88",
                                       font=["Digital-7 Mono", "36"], foreground="#ff0000",
                                       background="#000000", justify=RIGHT, anchor=E)
        self.ram_percent_value.pack(side=RIGHT)

        self.ram_used = Label(self.ram_usual_frames[2], text=self.ram_used_text,
                              font=["SF Pro Display", "22"], foreground="#ffffff",
                              background="#000000")
        self.ram_used.pack(side=LEFT)

        self.ram_used_value = Label(self.ram_usual_frames[2], text="888888.88",
                                    font=["Digital-7 Mono", "36"], foreground="#ff0000",
                                    background="#000000", justify=RIGHT, anchor=E)
        self.ram_used_value.pack(side=RIGHT)

        self.ram_free = Label(self.ram_usual_frames[3], text=self.ram_free_text,
                               font=["SF Pro Display", "22"], foreground="#ffffff",
                               background="#000000")
        self.ram_free.pack(side=LEFT)

        self.ram_free_value = Label(self.ram_usual_frames[3], text="888888.88",
                                     font=["Digital-7 Mono", "36"], foreground="#ff0000",
                                     background="#000000", justify=RIGHT, anchor=E)
        self.ram_free_value.pack(side=RIGHT)

        self.configure_ram_bar()
        
        
    def change_format(self, event):
        self.time_format = self.time_formats.current()
        self.time_formats.current(self.time_format)


    def change_mode(self, event):
        if self.modes.current() == 0:  # light
            self["background"] = "#ffffff"
            self.date_time_fr["background"] = '#ffffff'
            self.date_lab["background"] = '#ffffff'
            self.time_lab["background"] = '#ffffff'
            self.am_pm["background"] = self.am["background"] = \
                                       self.pm["background"] = "#ffffff"
            self.qf_frame["background"] = self.func1["background"] = \
                                          self.language_lab["background"] = \
                                          self.func2["background"] = "#ffffff"

            self.language_lab["foreground"] = '#000000'
            
            self.time_format_lab["background"] = self.func3["background"] = "#ffffff"
            self.time_format_lab["foreground"] = "#000000"
            self.modes_lab["background"] = '#ffffff'
            self.modes_lab["foreground"] = '#000000'
            self.cpu_frame["background"] = '#ffffff'

            for i in self.list_frames:
                i["background"] = "#ffffff"
            
            for i in self.list_num_cores:
                i["background"] = "#ffffff"
            
            for i in self.list_percent_cores:
                i["background"] = "#ffffff"
                
            self.disk_frame["background"] = "#ffffff"
                
            self.subs["background"] = "#ffffff"
            
            self.disk_name_title["background"] = "#ffffff"
                
            self.total_disk_title["background"] = "#ffffff"
                
            self.percent_disk_title["background"] = "#ffffff"
                
            self.used_disk_title["background"] = "#ffffff"
                
            self.free_disk_title["background"] = "#ffffff"  
            
            for i in self.frames_list_disks:
                i["bg"] = "#ffffff"

            for i in self.disk_names:
                i["background"] = "#ffffff"

            for i in self.disk_totals:
                i["background"] = "#ffffff"

            for i in self.disk_percents:
                i["background"] = "#ffffff"

            for i in self.disk_uses:
                i["background"] = "#ffffff"

            for i in self.disk_free:
                i["background"] = "#ffffff"
                
            
            self.ram_frame["background"] = "#ffffff"
            
            for i in self.ram_usual_frames:
                i["background"] = "#ffffff"

            self.ram_total["background"] = "#ffffff"
            self.ram_total["foreground"] = "#000000"

            self.ram_total_value["background"] = "#ffffff"

            self.ram_percent["background"] = "#ffffff"
            self.ram_percent["foreground"] = "#000000"

            self.ram_percent_value["background"] = "#ffffff"

            self.ram_used["background"] = "#ffffff"
            self.ram_used["foreground"] = "#000000"

            self.ram_used_value["background"] = "#ffffff"

            self.ram_free["background"] = "#ffffff"
            self.ram_free["foreground"] = "#000000"

            self.ram_free_value["background"] = "#ffffff"

        else:
            self["background"] = "#000000"
            self.date_time_fr["background"] = '#000000'
            self.date_lab["background"] = '#000000'
            self.time_lab["background"] = '#000000'
            self.am_pm["background"] = self.am["background"] = \
                                       self.pm["background"] = "#000000"
            self.qf_frame["background"] = self.func1["background"] = \
                                          self.language_lab["background"] = \
                                          self.func2["background"] = "#000000"

            self.language_lab["foreground"] = '#ffffff'
            
            self.time_format_lab["background"] = self.func3["background"] = "#000000"
            self.time_format_lab["foreground"] = "#ffffff"
            self.modes_lab["background"] = '#000000'
            self.modes_lab["foreground"] = '#ffffff'
            self.cpu_frame["background"] = '#000000'

            for i in self.list_frames:
                i["background"] = "#000000"
            
            for i in self.list_num_cores:
                i["background"] = "#000000"
            
            for i in self.list_percent_cores:
                i["background"] = "#000000"
                
            self.disk_frame["background"] = "#000000"
                
            self.subs["background"] = "#000000"
            
            self.disk_name_title["background"] = "#000000"
                
            self.total_disk_title["background"] = "#000000"
                
            self.percent_disk_title["background"] = "#000000"
                
            self.used_disk_title["background"] = "#000000"
                
            self.free_disk_title["background"] = "#000000"
            
            for i in self.frames_list_disks:
                i["bg"] = "#000000"

            for i in self.disk_names:
                i["background"] = "#000000"

            for i in self.disk_totals:
                i["background"] = "#000000"

            for i in self.disk_percents:
                i["background"] = "#000000"

            for i in self.disk_uses:
                i["background"] = "#000000"

            for i in self.disk_free:
                i["background"] = "#000000"
                
            
            self.ram_frame["background"] = "#000000"
            
            for i in self.ram_usual_frames:
                i["background"] = "#000000"

            self.ram_total["background"] = "#000000"
            self.ram_total["foreground"] = "#ffffff"

            self.ram_total_value["background"] = "#000000"

            self.ram_percent["background"] = "#000000"
            self.ram_percent["foreground"] = "#ffffff"

            self.ram_percent_value["background"] = "#000000"

            self.ram_used["background"] = "#000000"
            self.ram_used["foreground"] = "#ffffff"

            self.ram_used_value["background"] = "#000000"

            self.ram_free["background"] = "#000000"
            self.ram_free["foreground"] = "#ffffff"

            self.ram_free_value["background"] = "#000000"
                  
        
    def configure_date_and_time(self):
        current_date = str(date.today())
        current_date = "-".join(reversed(current_date.split('-')))  
        self.date_lab["text"] = current_date
        time_ = time.strftime("%H:%M:%S", time.localtime()).split(":")
        buf = time_.copy()
        if self.time_formats.current() == 0:
            time_[0] = f"{int(time_[0]) % 12:02d}" if time_[0] != "12" else "12"
            self.time_lab["text"] = ":".join(time_)
            
            if int(buf[0]) in range(0, 12) and self.modes.current() == 0:
                self.am["foreground"] = "#ff0000"; self.pm["foreground"] = "#ffffff"
                
            elif int(buf[0]) in range(0, 12) and self.modes.current() == 1:
                self.am["foreground"] = "#ff0000"; self.pm["foreground"] = "#000000"

            elif int(buf[0]) in range(12, 24) and self.modes.current() == 0:
                self.am["foreground"] = "#ffffff"; self.pm["foreground"] = "#ff0000"

            elif int(buf[0]) in range(12, 24) and self.modes.current() == 1:
                self.am["foreground"] = "#000000"; self.pm["foreground"] = "#ff0000"
            
          
        else:
            self.time_lab["text"] = ":".join(time_)
            if self.modes.current() == 0:
                self.am["foreground"] = "#ffffff"; self.pm["foreground"] = "#ffffff"
            elif self.modes.current() == 1:
                self.am["foreground"] = "#000000"; self.pm["foreground"] = "#000000"
        
        self.after(1, self.configure_date_and_time)
        
        
    def configure_cpu_bar(self):
        percents = self.cpu.cpu_percents()
        for i in range(len(self.list_percent_cores)):
            self.list_percent_cores[i]["text"] = f"{percents[i]:.2f}%".zfill(7)
            
        self.after(750, self.configure_cpu_bar)
        
        
    def configure_disk_bar(self):
        r = self.disks.drives
        for i in range(len(r)):
            k = pt.disk_usage(f"{self.disks.drives[i]}:\\")
            self.disk_totals[i]["text"] = f"{k[0]/1048576/1024:.2f}"
            self.disk_percents[i]["text"] = f"{k[3]:.2f}"
            self.disk_uses[i]["text"] = f"{k[1]/1048576/1024:.2f}"
            self.disk_free[i]["text"] = f"{k[2]/1048576/1024:.2f}"
                
        self.after(250, self.configure_disk_bar)


    def configure_ram_bar(self):
        s = self.cpu.get_ram_usage()
        self.ram_total_value["text"] = f"{s[0]/1048576:.2f}"
        self.ram_percent_value["text"] = f"{s[2]:.2f}"
        self.ram_used_value["text"] = f"{s[3]/1048576:.2f}"
        self.ram_free_value["text"] = f"{s[4]/1048576:.2f}"

        self.after(750, self.configure_ram_bar)
                 
        
    def change_language(self, event):
        if self.languages_win.current() == 0:  # english
            self.exit_but_text = "Exit"
            self.date_time_fr_text = "DATE & TIME"
            self.qf_frame_text = "QUICK FUNCTIONS"
            self.language_lab_text = "Language"
            self.time_format_lab_text = "Time Format"
            self.modes_lab_text = "Mode"
            self.list_modes = ["Light", "Dark"]
            self.cpu_frame_text = "CPU CORES' USAGES"
            self.disk_frame_text = "DISKS' USAGES"
            self.disk_name_title_text = "Disk Name"
            self.total_disk_title_text = "Total, GB"
            self.percent_disk_title_text = "Percent"
            self.used_disk_title_text = "Used, GB"
            self.free_disk_title_text = "Free, GB"
            self.ram_frame_text = "RAM USAGE"
            self.ram_total_text = "Total, MB"
            self.ram_percent_text = "Percent"
            self.ram_used_text = "Used, MB"
            self.ram_free_text = "Free, MB"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab['text'] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.ram_frame["text"] = self.ram_frame_text
            self.ram_total["text"] = self.ram_total_text
            self.ram_percent["text"] = self.ram_percent_text
            self.ram_used["text"] = self.ram_used_text
            self.ram_free["text"] = self.ram_free_text
            self.modes.current(self.mode)
            self.update()
            
        elif self.languages_win.current() == 1:  # german
            self.exit_but_text = "Ausfahrt"
            self.date_time_fr_text = "DATUM & UHRZEIT"
            self.qf_frame_text = "SCHNELLE FUNKTIONEN"
            self.language_lab_text = "Sprache"
            self.time_format_lab_text = "Zeitformat"
            self.modes_lab_text = "Modus"
            self.list_modes = ["Hell", "Dunkel"]
            self.cpu_frame_text = "VERWENDUNG VON CPU-KERNEN"
            self.disk_frame_text = "VERWENDUNG VON FESTPLATTEN"
            self.disk_name_title_text = "Datenträgern."
            self.total_disk_title_text = "Gesamt, GB"
            self.percent_disk_title_text = "Prozent"
            self.used_disk_title_text = "Gebr., GB"
            self.free_disk_title_text = "Frei, GB"
            self.ram_frame_text = "RAM-NUTZUNG"
            self.ram_total_text = "Gesamt, MB"
            self.ram_percent_text = "Prozent"
            self.ram_used_text = "Gebraucht, MB"
            self.ram_free_text = "Kostenlos, MB"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab['text'] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.ram_frame["text"] = self.ram_frame_text
            self.ram_total["text"] = self.ram_total_text
            self.ram_percent["text"] = self.ram_percent_text
            self.ram_used["text"] = self.ram_used_text
            self.ram_free["text"] = self.ram_free_text
            self.modes.current(self.mode)
            self.update()
            
        elif self.languages_win.current() == 2:  # french
            self.exit_but_text = "Sortie"
            self.date_time_fr_text = "DATE ET HEURE"
            self.qf_frame_text = "FONCTIONS RAPIDES"
            self.language_lab_text = "Langue"
            self.time_format_lab_text = "Format de l'heure"
            self.modes_lab_text = "Mode"
            self.list_modes = ["Clair", "Sombre"]
            self.cpu_frame_text = "UTILISATIONS DES CŒURS DE PROCESSEUR"
            self.disk_frame_text = "USAGES DES DISQUES"
            self.disk_name_title_text = "Nom du Disque"
            self.total_disk_title_text = "Total, GB"
            self.percent_disk_title_text = "Pourcent."
            self.used_disk_title_text = "D'occasion, GB"
            self.free_disk_title_text = "Libr., GB"
            self.ram_frame_text = "UTILISATION DE LA RAM"
            self.ram_total_text = "Total, MB"
            self.ram_percent_text = "Pourcentage"
            self.ram_used_text = "Utilisé, MB"
            self.ram_free_text = "Gratuit, MB"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab['text'] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.ram_frame["text"] = self.ram_frame_text
            self.ram_total["text"] = self.ram_total_text
            self.ram_percent["text"] = self.ram_percent_text
            self.ram_used["text"] = self.ram_used_text
            self.ram_free["text"] = self.ram_free_text
            self.modes.current(self.mode)
            self.update()
            
        elif self.languages_win.current() == 3:  # spanish
            self.exit_but_text = "Salida"
            self.date_time_fr_text = "FECHA Y HORA"
            self.qf_frame_text = "FUNCIONES RÁPIDAS"
            self.language_lab_text = "Idioma"
            self.time_format_lab_text = "Formato de Hora"
            self.modes_lab_text = "Modo"
            self.list_modes = ["Claro", "Oscuro"]
            self.cpu_frame_text = "USOS DE LOS NÚCLEOS DE CPU"
            self.disk_frame_text = "USOS DE LOS DISCOS"
            self.disk_name_title_text = "Nom. del Disco"
            self.total_disk_title_text = "Total, GB"
            self.percent_disk_title_text = "Porcentaje"
            self.used_disk_title_text = "Usado, GB"
            self.free_disk_title_text = "Libre, GB"
            self.ram_frame_text = "USO DE RAM"
            self.ram_total_text = "Total, MB"
            self.ram_percent_text = "Porcentaje"
            self.ram_used_text = "Usado, MB"
            self.ram_free_text = "Gratis, MB"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab['text'] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.ram_frame["text"] = self.ram_frame_text
            self.ram_total["text"] = self.ram_total_text
            self.ram_percent["text"] = self.ram_percent_text
            self.ram_used["text"] = self.ram_used_text
            self.ram_free["text"] = self.ram_free_text
            self.modes.current(self.mode)
            self.update()
            
        elif self.languages_win.current() == 4:  # italian
            self.exit_but_text = "Uscita"
            self.date_time_fr_text = "DATA E ORA"
            self.qf_frame_text = "FUNZIONI RAPIDE"
            self.language_lab_text = "Lingua"
            self.time_format_lab_text = "Formato orario"
            self.modes_lab_text = "Modalità"
            self.list_modes = ["Luce", "Buio"]
            self.cpu_frame_text = "USI DEI CORE CPU"
            self.disk_frame_text = "USI DEI DISCHI"
            self.disk_name_title_text = "Nome disco"
            self.total_disk_title_text = "Totale, GB"
            self.percent_disk_title_text = "Percento"
            self.used_disk_title_text = "Usato, GB"
            self.free_disk_title_text = "Libero, GB"
            self.ram_frame_text = "UTILIZZO RAM"
            self.ram_total_text = "Totale, MB"
            self.ram_percent_text = "Percento"
            self.ram_used_text = "Usato, MB"
            self.ram_free_text = "Libero, MB"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab['text'] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes  
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.ram_frame["text"] = self.ram_frame_text
            self.ram_total["text"] = self.ram_total_text
            self.ram_percent["text"] = self.ram_percent_text
            self.ram_used["text"] = self.ram_used_text
            self.ram_free["text"] = self.ram_free_text
            self.modes.current(self.mode)
            self.update()
            
        elif self.languages_win.current() == 5:  # greek
            self.exit_but_text = "Έξοδος"
            self.date_time_fr_text = "ΗΜΕΡΟΜΗΝΙΑ & ΩΡΑ"
            self.qf_frame_text = "ΓΡΗΓΟΡΕΣ ΛΕΙΤΟΥΡΓΙΕΣ"
            self.language_lab_text = "Γλώσσα"
            self.time_format_lab_text = "Μορφή Ώρας"
            self.modes_lab_text = "Λειτουργία"
            self.list_modes = ["Φωτεινή", "Σκοτεινή"]
            self.cpu_frame_text = "ΧΡΗΣΕΙΣ ΠΥΡΗΝΩΝ ΚΜΕ"
            self.disk_frame_text = "ΧΡΗΣΕΙΣ ΔΙΣΚΩΝ"
            self.disk_name_title_text = "Όνομα Δίσκου"
            self.total_disk_title_text = "Σύνολο, ΜΒ"
            self.percent_disk_title_text = "Τοις"
            self.used_disk_title_text = "Χρησ., GB"
            self.free_disk_title_text = "Ελεύθ., GB"
            self.ram_frame_text = "ΧΡΗΣΗ RAM"
            self.ram_total_text = "Σύνολο, ΜΒ"
            self.ram_percent_text = "Τοις"
            self.ram_used_text = "Χρησιμοποιείται, MB"
            self.ram_free_text = "Ελεύθερο, MB"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab['text'] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.ram_frame["text"] = self.ram_frame_text
            self.ram_total["text"] = self.ram_total_text
            self.ram_percent["text"] = self.ram_percent_text
            self.ram_used["text"] = self.ram_used_text
            self.ram_free["text"] = self.ram_free_text
            self.modes.current(self.mode)
            self.update()
            
        elif self.languages_win.current() == 6:  # bulgarian
            self.exit_but_text = "Изход"
            self.date_time_fr_text = "ДАТА И ЧАС"
            self.qf_frame_text = "БЪРЗИ ФУНКЦИИ"
            self.language_lab_text = "Език"
            self.time_format_lab_text = "Формат на времето"
            self.modes_lab_text = "Режим"
            self.list_modes = ["Светъл", "Тъмен"]
            self.cpu_frame_text = "УПОТРЕБА НА ПРОЦЕСОРНИТЕ ЯДРА"
            self.disk_frame_text = "УПОТРЕБА НА ДИСКОВЕ"
            self.disk_name_title_text = "Име На Диска"
            self.total_disk_title_text = "Общо, ГБ"
            self.percent_disk_title_text = "Процент"
            self.used_disk_title_text = "Изп., ГБ"
            self.free_disk_title_text = "Своб., ГБ"
            self.ram_frame_text = "ИЗПОЛЗВАНЕ НА RAM"
            self.ram_total_text = "Общо, ГБ"
            self.ram_percent_text = "Процент"
            self.ram_used_text = "Използвано, МБ"
            self.ram_free_text = "Свободно, МБ"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab['text'] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes 
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.ram_frame["text"] = self.ram_frame_text
            self.ram_total["text"] = self.ram_total_text
            self.ram_percent["text"] = self.ram_percent_text
            self.ram_used["text"] = self.ram_used_text
            self.ram_free["text"] = self.ram_free_text
            self.modes.current(self.mode)
            self.update()
            
        elif self.languages_win.current() == 7:  # belarusian
            self.exit_but_text = "Выхад"
            self.date_time_fr_text = "ДАТА І ЧАС"
            self.qf_frame_text = "ХУТКІЯ ФУНКЦЫІ"
            self.language_lab_text = "Мова"
            self.time_format_lab_text = "Фармат часу"
            self.modes_lab_text = "Рэжым"
            self.list_modes = ["Светлы", "Цёмны"]
            self.cpu_frame_text = "ВЫКАРЫСТАННЕ ПРАЦЭСАРНЫХ ЯДРАЎ"
            self.disk_frame_text = "ВЫКАРЫСТАННЕ ДЫСКАЎ"
            self.disk_name_title_text = "Назва дыска"
            self.total_disk_title_text = "Усяго, ГБ"
            self.percent_disk_title_text = "Адсотак"
            self.used_disk_title_text = "Выкар., ГБ"
            self.free_disk_title_text = "Сваб., ГБ"
            self.ram_frame_text = "ВЫКАРЫСТАННЕ АПЕРАТЫЎНАЙ ПАМЯЦІ"
            self.ram_total_text = "Усяго, ГБ"
            self.ram_percent_text = "Адсотак"
            self.ram_used_text = "Выкарыстаны, МБ"
            self.ram_free_text = "Свабодны, МБ"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab['text'] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.ram_frame["text"] = self.ram_frame_text
            self.ram_total["text"] = self.ram_total_text
            self.ram_percent["text"] = self.ram_percent_text
            self.ram_used["text"] = self.ram_used_text
            self.ram_free["text"] = self.ram_free_text
            self.modes.current(self.mode)
            self.update()
            
        elif self.languages_win.current() == 8:  # kazakh
            self.exit_but_text = "Шығу"
            self.date_time_fr_text = "КҮНІ МЕН УАҚЫТЫ"
            self.qf_frame_text = "ЖЫЛДАМ ФУНКЦИЯЛАР"
            self.language_lab_text = "Тіл"
            self.time_format_lab_text = "Уақыт Форматы"
            self.modes_lab_text = "Режимі"
            self.list_modes = ["Жарық", "Қараңғы"]
            self.cpu_frame_text = "CPU ЯДРОЛАРЫНЫҢ ҚОЛДАНЫЛУЫ"
            self.disk_frame_text = "ДИСКІЛЕРДІ ПАЙДАЛАНУ"
            self.disk_name_title_text = "Диск Атауы"
            self.total_disk_title_text = "Барлығы, ГБ"
            self.percent_disk_title_text = "Пайыз"
            self.used_disk_title_text = "Пайд., ГБ"
            self.free_disk_title_text = "Тегін, ГБ"
            self.ram_frame_text = "ЖЖҚ-НЫ ПАЙДАЛАНУ"
            self.ram_total_text = "Барлығы, ГБ"
            self.ram_percent_text = "Пайыз"
            self.ram_used_text = "Пайдаланылған, МБ"
            self.ram_free_text = "Тегін, МБ"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab['text'] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.ram_frame["text"] = self.ram_frame_text
            self.ram_total["text"] = self.ram_total_text
            self.ram_percent["text"] = self.ram_percent_text
            self.ram_used["text"] = self.ram_used_text
            self.ram_free["text"] = self.ram_free_text
            self.modes.current(self.mode)
            self.update()
            
        elif self.languages_win.current() == 9:  # macedonian
            self.exit_but_text = "Излез"
            self.date_time_fr_text = "ДАТУМ И ВРЕМЕ"
            self.qf_frame_text = "БРЗИ ФУНКЦИИ"
            self.language_lab_text = "Јазик"
            self.time_format_lab_text = "Временски Формат"
            self.modes_lab_text = "Режим"
            self.list_modes = ["Светл", "Темен"]
            self.cpu_frame_text = "УПОТРЕБА НА ЈАДРАТА НА ПРОЦЕСОРОТ"
            self.disk_frame_text = "УПОТРЕБА НА ДИСКОВИ"
            self.disk_name_title_text = "Име На Дискот"
            self.total_disk_title_text = "Вкупно, ГБ"
            self.percent_disk_title_text = "Проценти"
            self.used_disk_title_text = "Кор., ГБ"
            self.free_disk_title_text = "Слоб., ГБ"
            self.ram_frame_text = "УПОТРЕБА НА RAM"
            self.ram_total_text = "Вкупно, МБ"
            self.ram_percent_text = "Проценти"
            self.ram_used_text = "Користени, МБ"
            self.ram_free_text = "Слободен, МБ"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab['text'] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes 
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.ram_frame["text"] = self.ram_frame_text
            self.ram_total["text"] = self.ram_total_text
            self.ram_percent["text"] = self.ram_percent_text
            self.ram_used["text"] = self.ram_used_text
            self.ram_free["text"] = self.ram_free_text
            self.modes.current(self.mode)
            self.update()
            
        elif self.languages_win.current() == 10:  # serbian
            self.exit_but_text = "Излаз"
            self.date_time_fr_text = "ДАТУМ И ВРЕМЕ"
            self.qf_frame_text = "БРЗЕ ФУНКЦИЈЕ"
            self.language_lab_text = "Језик"
            self.time_format_lab_text = "Формат времена"
            self.modes_lab_text = "Режим"
            self.list_modes = ["Светли", "Тамни"]
            self.cpu_frame_text = "КОРИШЋЕЊЕ ПРОЦЕСОРСКИХ ЈЕЗГАРА"
            self.disk_frame_text = "КОРИШЋЕЊЕ ДИСКОВА"
            self.disk_name_title_text = "Назив диска"
            self.total_disk_title_text = "Укупно, ГБ"
            self.percent_disk_title_text = "Проценат"
            self.used_disk_title_text = "Кор., ГБ"
            self.free_disk_title_text = "Слоб., ГБ"
            self.ram_frame_text = "КОРИШЋЕЊЕ РАМ-А"
            self.ram_total_text = "Укупно, МБ"
            self.ram_percent_text = "Проценат"
            self.ram_used_text = "Коришћен, МБ"
            self.ram_free_text = "Слободен, МБ"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab['text'] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes  
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.ram_frame["text"] = self.ram_frame_text
            self.ram_total["text"] = self.ram_total_text
            self.ram_percent["text"] = self.ram_percent_text
            self.ram_used["text"] = self.ram_used_text
            self.ram_free["text"] = self.ram_free_text
            self.modes.current(self.mode)
            self.update()
            
        elif self.languages_win.current() == 11:  # tatar
            self.exit_but_text = "Чыгыш"
            self.date_time_fr_text = "ДАТА ҺӘМ ВАКЫТ"
            self.qf_frame_text = "ТИЗ ФУНКЦИЯЛӘР"
            self.language_lab_text = "Тел"
            self.time_format_lab_text = "Вакыт форматы"
            self.modes_lab_text = "Тәртип"
            self.list_modes = ["Якты", "Караңгы"]
            self.cpu_frame_text = "ПРОЦЕССОР ТӨШЛӘРЕННӘН КУЛЛАНЫШЛАР"
            self.disk_frame_text = "ДИСКЛАРНЫ КУЛЛАНУ"
            self.disk_name_title_text = "Диск исеме"
            self.total_disk_title_text = "Барлыгы, ГБ"
            self.percent_disk_title_text = "Процент"
            self.used_disk_title_text = "Кулл., ГБ"
            self.free_disk_title_text = "Ирекле, ГБ"
            self.ram_frame_text = "ОПЕРАТИВ ХӘТЕРДӘН КУЛЛАНЫШ"
            self.ram_total_text = "Барлыгы, ГБ"
            self.ram_percent_text = "Процент"
            self.ram_used_text = "Кулланылган, МБ"
            self.ram_free_text = "Ирекле, МБ"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab['text'] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes  
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.ram_frame["text"] = self.ram_frame_text
            self.ram_total["text"] = self.ram_total_text
            self.ram_percent["text"] = self.ram_percent_text
            self.ram_used["text"] = self.ram_used_text
            self.ram_free["text"] = self.ram_free_text
            self.modes.current(self.mode)
            self.update()
            
        elif self.languages_win.current() == 12:  # chinese
            self.exit_but_text = "出口"
            self.date_time_fr_text = "日期及时间"
            self.qf_frame_text = "快速功能"
            self.language_lab_text = "语言"
            self.time_format_lab_text = "时间格式"
            self.modes_lab_text = "模式"
            self.list_modes = ["亮", "暗"]
            self.cpu_frame_text = "CPU核心的用途"
            self.disk_frame_text = "磁盘的用途"
            self.disk_name_title_text = "磁盘名称"
            self.total_disk_title_text = "总计,GB"
            self.percent_disk_title_text = "百分比"
            self.used_disk_title_text = "使用,GB"
            self.free_disk_title_text = "自由,GB"
            self.ram_frame_text = "RAM使用情况"
            self.ram_total_text = "总计,MB"
            self.ram_percent_text = "百分比"
            self.ram_used_text = "使用,MB"
            self.ram_free_text = "免费，MB"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab['text'] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.ram_frame["text"] = self.ram_frame_text
            self.ram_total["text"] = self.ram_total_text
            self.ram_percent["text"] = self.ram_percent_text
            self.ram_used["text"] = self.ram_used_text
            self.ram_free["text"] = self.ram_free_text
            self.modes.current(self.mode)
            self.update()
            
        elif self.languages_win.current() == 13:  # armenian
            self.exit_but_text = "Ելք"
            self.date_time_fr_text = "ԱՄՍԱԹԻՎ և ԺԱՄ"
            self.qf_frame_text = "ԱՐԱԳ ՀԱՏԿՈՒԹՅՈՒՆՆԵՐ"
            self.language_lab_text = "Լեզու"
            self.time_format_lab_text = "Ժամանակի ձևաչափ"
            self.modes_lab_text = "Ռեժիմ"
            self.list_modes = ["Ռեժիմ", "մութ".title()]
            self.cpu_frame_text = "ՕԳՏԱԳՈՐԾԵԼՈՎ ՊՐՈՑԵՍՈՐԻ ՄԻՋՈՒԿՆԵՐ"
            self.disk_frame_text = "ՕԳՏԱԳՈՐԾԵԼՈՎ ԿՐԻՉՆԵՐ"
            self.disk_name_title_text = "Սկավ. անվ."
            self.total_disk_title_text = "Ընդհ., ԳԲ"
            self.percent_disk_title_text = "Տոկոս"
            self.used_disk_title_text = "Օգտագ., ԳԲ"
            self.free_disk_title_text = "Ազատ., ԳԲ"
            self.ram_frame_text = "RAM-Ի ՕԳՏԱԳՈՐԾՈՒՄԸ"
            self.ram_total_text = "Ընդամենը, ՄԲ"
            self.ram_percent_text = "Տոկոս"
            self.ram_used_text = "Օգտագործված, ՄԲ"
            self.ram_free_text = "Ազատ, ՄԲ"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab['text'] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes  
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.ram_frame["text"] = self.ram_frame_text
            self.ram_total["text"] = self.ram_total_text
            self.ram_percent["text"] = self.ram_percent_text
            self.ram_used["text"] = self.ram_used_text
            self.ram_free["text"] = self.ram_free_text
            self.modes.current(self.mode)
            self.update()

        if self.languages_win.current() == 13:
            self.exit_but["font"] = ("Noto Sans Armenian", "24")
            self.date_time_fr["font"] = ("Noto Sans Armenian", "18")
            self.qf_frame["font"] = ("Noto Sans Armenian", "18")
            self.languages_win['font'] = ("Noto Sans Armenian", "24")
            self.language_lab['font'] = ("Noto Sans Armenian", "24")
            self.time_format_lab["font"] = ("Noto Sans Armenian", "24")
            self.modes_lab["font"] = ("Noto Sans Armenian", "24")
            self.modes["font"] = ("Noto Sans Armenian", "24")  
            self.cpu_frame["font"] = ("Noto Sans Armenian", "18")
            self.disk_frame["font"] = ("Noto Sans Armenian", "18")
            self.disk_name_title["font"] = ("Noto Sans Armenian", "22")
            self.total_disk_title["font"] = ("Noto Sans Armenian", "22")
            self.percent_disk_title["font"] = ("Noto Sans Armenian", "22")
            self.used_disk_title["font"] = ("Noto Sans Armenian", "22")
            self.free_disk_title["font"] = ("Noto Sans Armenian", "22")
            self.ram_frame["font"] = ("Noto Sans Armenian", "18")
            self.ram_total["font"] = ("Noto Sans Armenian", "22")
            self.ram_percent["font"] = ("Noto Sans Armenian", "22")
            self.ram_used["font"] = ("Noto Sans Armenian", "22")
            self.ram_free["font"] = ("Noto Sans Armenian", "22")
        else:
            self.exit_but["font"] = ("SF Pro Display", "24")
            self.date_time_fr["font"] = ("SF Pro Display", "18")
            self.qf_frame["font"] = ("SF Pro Display", "18")
            self.languages_win['font'] = ("SF Pro Display", "24")
            self.language_lab['font'] = ("SF Pro Display", "24")
            self.time_format_lab["font"] = ("SF Pro Display", "24")
            self.modes_lab["font"] = ("SF Pro Display", "24")
            self.modes["font"] = ("SF Pro Display", "24")  
            self.cpu_frame["font"] = ("SF Pro Display", "18")
            self.disk_frame["font"] = ("SF Pro Display", "18")
            self.disk_name_title["font"] = ("SF Pro Display", "22")
            self.total_disk_title["font"] = ("SF Pro Display", "22")
            self.percent_disk_title["font"] = ("SF Pro Display", "22")
            self.used_disk_title["font"] = ("SF Pro Display", "22")
            self.free_disk_title["font"] = ("SF Pro Display", "22")
            self.ram_frame["font"] = ("SF Pro Display", "18")
            self.ram_total["font"] = ("SF Pro Display", "22")
            self.ram_percent["font"] = ("SF Pro Display", "22")
            self.ram_used["font"] = ("SF Pro Display", "22")
            self.ram_free["font"] = ("SF Pro Display", "22")
        
        
    def clear_win(self):
        for i in self.winfo_children():
            i.destroy()
            
            
    def app_exit(self):
        self.destroy()
        sys.exit()
    
    
root = Application()
root.mainloop()
