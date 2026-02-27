import tkinter as tk

def draw_xbox_controller(canvas):
    # Main body: dark rounded rectangle (approximated with a rectangle and corner circles)
    body_color = "#2c2c2c"  # dark gray
    x1, y1, x2, y2 = 50, 50, 550, 350
    radius = 30
    # Draw four corner circles for rounding effect
    canvas.create_oval(x1, y1, x1+2*radius, y1+2*radius, fill=body_color, outline=body_color)
    canvas.create_oval(x2-2*radius, y1, x2, y1+2*radius, fill=body_color, outline=body_color)
    canvas.create_oval(x1, y2-2*radius, x1+2*radius, y2, fill=body_color, outline=body_color)
    canvas.create_oval(x2-2*radius, y2-2*radius, x2, y2, fill=body_color, outline=body_color)
    # Draw the main rectangle connecting the rounded corners
    canvas.create_rectangle(x1+radius, y1, x2-radius, y2, fill=body_color, outline=body_color)
    canvas.create_rectangle(x1, y1+radius, x2, y2-radius, fill=body_color, outline=body_color)

    # Left analog stick (top‑left)
    canvas.create_oval(120, 120, 180, 180, fill="#4a4a4a", outline="black", width=2)
    canvas.create_oval(135, 135, 165, 165, fill="#1a1a1a", outline="gray")  # inner dimple

    # Right analog stick (top‑right)
    canvas.create_oval(420, 120, 480, 180, fill="#4a4a4a", outline="black", width=2)
    canvas.create_oval(435, 135, 465, 165, fill="#1a1a1a", outline="gray")

    # D‑pad (bottom‑left) – plus sign shape
    dpad_color = "#3a3a3a"
    # horizontal arm
    canvas.create_rectangle(120, 240, 180, 260, fill=dpad_color, outline="black", width=2)
    # vertical arm
    canvas.create_rectangle(140, 220, 160, 280, fill=dpad_color, outline="black", width=2)

    # Action buttons (bottom‑right) – diamond layout
    button_center_x, button_center_y = 450, 250
    button_radius = 16
    # A (bottom) – green
    canvas.create_oval(button_center_x-button_radius, button_center_y+button_radius-5,
                       button_center_x+button_radius, button_center_y+button_radius+27,
                       fill="#0f0", outline="black", width=2)
    # B (right) – red
    canvas.create_oval(button_center_x+button_radius-5, button_center_y-button_radius,
                       button_center_x+button_radius+27, button_center_y+button_radius,
                       fill="#f00", outline="black", width=2)
    # X (left) – blue
    canvas.create_oval(button_center_x-button_radius-27, button_center_y-button_radius,
                       button_center_x-button_radius+5, button_center_y+button_radius,
                       fill="#00f", outline="black", width=2)
    # Y (top) – yellow
    canvas.create_oval(button_center_x-button_radius, button_center_y-button_radius-27,
                       button_center_x+button_radius, button_center_y-button_radius+5,
                       fill="#ff0", outline="black", width=2)

    # Start and Select buttons (center bottom)
    canvas.create_oval(270, 300, 300, 330, fill="#aaa", outline="black", width=2)  # select
    canvas.create_oval(330, 300, 360, 330, fill="#aaa", outline="black", width=2)  # start

    # Xbox logo (center)
    canvas.create_text(300, 180, text="X", fill="white", font=("Arial", 24, "bold"))

def main():
    root = tk.Tk()
    root.title("Xbox Controller")
    root.geometry("600x400")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.pack()

    draw_xbox_controller(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()