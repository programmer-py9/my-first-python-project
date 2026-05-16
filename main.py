import tkinter as tk

def reset_buttons():
        home_btn.config(bg=BUTTON_COLOR)
        gym_btn.config(bg=BUTTON_COLOR)
        study_btn.config(bg=BUTTON_COLOR)
        motivation_btn.config(bg=BUTTON_COLOR)
        
def show_home():
    home_page.tkraise()
    reset_buttons()
    home_btn.config(bg=ACTIVE_BUTTON)
   
def show_gym():
    gym_page.tkraise()
    reset_buttons()
    gym_btn.config(bg=ACTIVE_BUTTON)
    
def show_study():
    study_page.tkraise()
    reset_buttons()
    study_btn.config(bg=ACTIVE_BUTTON)

def show_quotes():
    motivational_page.tkraise()
    reset_buttons()
    motivation_btn.config(bg=ACTIVE_BUTTON)
   
root = tk.Tk()
root.title("My First App 😎 ")
root.geometry("700x400")
root. config(bg = "white")
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
BG_COLOR = "#1E1E1E"
TEXT_COLOR = "#D4D4D4"
BUTTON_COLOR = "#1E1E1E"
BUTTON_ACTIVE = "#3A3A3A"
ACTIVE_BUTTON = "#3A3A3A"

FONT_LARGE = ("Arial", 26)
FONT_MEDIUM = ("Arial", 16)
FONT_BUTTON = ("Arial", 12)

header_frame = tk. Frame(
    root,
    bg = "#1E1E1E", 
    height = 100
    )
header_frame.grid(row = 0 ,column = 0 , sticky = "new")
header_label = tk.Label(
    header_frame,
    text = "Streak Recorder",
    bg = "#1E1E1E",
    fg = "#D4D4D4",
    font = ("Arial" , 26)
    )
header_label.pack(pady = 10)

main_frame = tk.Frame(root)
main_frame.grid(row = 1 , column = 0,sticky = "nsew")
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)

sidebar_frame = tk.Frame(
    main_frame ,
    bg = "#1E1E1E",
    width = 175)
    
sidebar_frame.grid(column = 0 ,sticky = "nsew" ) 
sidebar_label = tk.Label(
    sidebar_frame,
    text = "Navigate",
    bg = "#1E1E1E",
    fg = "#D4D4D4",
    font = ("Arial" , 14)
    )
sidebar_label.grid(row = 1 , column = 0 , pady = 20 , padx = 10 , sticky = "ew")  
sidebar_frame.columnconfigure(0, weight=1)

content_frame = tk.Frame(
    main_frame,
    bg = "#1E1E1E")
content_frame.grid(row = 0 , column = 1,sticky = "nsew")  
content_frame.rowconfigure(0, weight=1)
content_frame.columnconfigure(0, weight=1)

def create_page(text):

    page = tk.Frame(
        content_frame,
        bg=BG_COLOR
    )

    page.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    page.rowconfigure(0, weight=1)
    page.columnconfigure(0, weight=1)

    page_label = tk.Label(
        page,
        text=text,
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=FONT_MEDIUM
    )

    page_label.grid(
        row=0,
        column=0
    )

    return page   
    
home_page = create_page("Welcome")

gym_page = create_page("Exercising time")

study_page = create_page("Study hard")

motivational_page = create_page("Grow buddy")

def create_nav_button(text, command, row):

    button = tk.Button(
        sidebar_frame,
        text=text,
        bg=BUTTON_COLOR,
        fg=TEXT_COLOR,
        activebackground=BUTTON_ACTIVE,
        activeforeground="white",
        font=FONT_BUTTON,
        bd=0,
        relief="flat",
        highlightthickness=0,
        anchor="w",
        padx=15,
        pady=10,
        command=command
    )

    button.grid(
        row=row,
        column=0,
        padx=10,
        pady=20,
        sticky="ew"
    )
    def on_enter(event):

        event.widget.config(bg=BUTTON_ACTIVE)
    
    def on_leave(event):

        event.widget.config(bg=BUTTON_COLOR)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    return button
       
home_btn = create_nav_button("Home", show_home, 2)

gym_btn = create_nav_button("Gym", show_gym, 3)

study_btn = create_nav_button("Study", show_study, 4)

motivation_btn = create_nav_button("Motivation", show_quotes, 5)

 
       

footer_frame = tk.Frame(
    root ,
    bg = "#1E1E1E",
    height = 100
    )
footer_frame.grid(row = 2 , column = 0 , sticky = "nsew")

footer_label = tk.Label(
    footer_frame ,
    text = "Track habits" ,
    bg = "#1E1E1E",
    fg  = "#D4D4D4",
    font = ("Arial" , 32))
footer_label.grid(row = 0, column = 0 , sticky = "nsew") 
home_page.tkraise()
root.mainloop()
