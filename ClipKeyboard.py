import tkinter as tk
from tkinter import font, messagebox, simpledialog
import keyboard
import ctypes

class SimulatedKeyboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard Input Simulator")

        # Font settings
        self.current_font_family = "Consolas"
        self.current_font_size = 12
        self.text_font = font.Font(family=self.current_font_family, size=self.current_font_size)

        # Text widget for input
        self.text_box = tk.Text(root, wrap='word', font=self.text_font, undo=True)
        self.text_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Button frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=(0, 10))

        # Send button
        self.send_button = tk.Button(button_frame, text="Send as Keystrokes", command=self.send_text)
        self.send_button.pack(side=tk.LEFT, padx=5)

        # Font button
        tk.Button(button_frame, text="Set Font", command=self.set_font).pack(side=tk.LEFT, padx=5)

        # Clear button
        tk.Button(button_frame, text="Clear", command=self.clear_text).pack(side=tk.LEFT, padx=5)

        # Remove control characters button
        tk.Button(button_frame, text="Remove Control Chars", command=self.strip_control_chars).pack(side=tk.LEFT, padx=5)

        # Status label for countdown display
        self.status_label = tk.Label(root, text="", fg="blue")
        self.status_label.pack(pady=(0, 10))

        # Override Ctrl+V to paste as plain text
        self.text_box.bind("<Control-v>", self.paste_plain_text)

        # Internal variables for countdown
        self.countdown = 0
        self.text_to_send = ""

    def paste_plain_text(self, event=None):
        try:
            raw = self.root.clipboard_get()
            self.text_box.insert(tk.INSERT, raw)
        except tk.TclError:
            pass
        return "break"

    def strip_control_chars(self):
        """Remove CR, LF, and other control characters from the text."""
        full_text = self.text_box.get("1.0", tk.END)
        filtered = ''.join(ch for ch in full_text if ord(ch) >= 32)
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert("1.0", filtered)

    def send_text(self):
        text = self.text_box.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("No Text", "Please enter or paste text.")
            return

        if not self.is_admin():
            messagebox.showerror("Admin Required", "This function requires administrator privileges.")
            return

        # Start countdown and schedule keystroke simulation
        self.start_countdown(5, text)

    def start_countdown(self, seconds, text):
        self.countdown = seconds
        self.text_to_send = text
        self.send_button.config(state=tk.DISABLED)
        self.update_countdown()

    def update_countdown(self):
        if self.countdown > 0:
            self.status_label.config(text=f"Sending in {self.countdown} second{'s' if self.countdown != 1 else ''}...")
            self.countdown -= 1
            self.root.after(1000, self.update_countdown)
        else:
            # Clear status and send text
            self.status_label.config(text="")
            keyboard.write(self.text_to_send, delay=0.01)
            self.send_button.config(state=tk.NORMAL)

    def set_font(self):
        new_font = simpledialog.askstring("Font", "Enter font family (e.g., Arial, Consolas):")
        if new_font:
            new_size = simpledialog.askinteger("Font Size", "Enter font size (e.g., 12):", minvalue=6, maxvalue=72)
            if new_size:
                self.text_font.configure(family=new_font, size=new_size)

    def clear_text(self):
        self.text_box.delete("1.0", tk.END)

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulatedKeyboardApp(root)
    root.geometry("700x500")
    root.mainloop() 