import os
import sys
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from pathlib import Path


# Placeholder classes for menus that required custom dialogs in Java
class FontChooser:
    pass


class FindDialog:
    pass


class FileOperation:
    def __init__(self, npd):
        self.npd = npd
        self.saved = True
        self.new_file_flag = True
        self.file_name = "Untitled"
        self.application_title = "NotePad"
        self.file_ref = None
        self.npd.root.title(f"{self.file_name} - {self.application_title}")
        self.file_types = [
            ("Text Files(*.txt)", "*.txt"),
            ("Java Source Files(*.java)", "*.java"),
            ("All Files", "*.*"),
        ]

    def set_save(self, saved):
        self.saved = saved

    def save_file(self, target_path):
        try:
            with open(target_path, "w", encoding="utf-8") as fout:
                text_content = self.npd.ta.get("1.0", tk.END)[:-1]
                fout.write(text_content)
            self.update_status(target_path, True)
            return True
        except Exception:
            self.update_status(target_path, False)
            return False

    def save_this_file(self, event=None):
        if not self.new_file_flag and self.file_ref:
            return self.save_file(self.file_ref)
        return self.save_as_file()

    def save_as_file(self, event=None):
        target_file = filedialog.asksaveasfilename(
            initialdir=".",
            title="Save As...",
            filetypes=self.file_types,
            defaultextension=".txt",
        )
        if not target_file:
            return False
        target_path = Path(target_file)
        if target_path.exists():
            if not messagebox.askyesno(
                "Save As",
                f"{target_path.name} already exists.\nDo you want to replace it?",
            ):
                return self.save_as_file()
        return self.save_file(target_path)

    def open_file_dialog(self, event=None):
        if not self.confirm_save():
            return
        target_file = filedialog.askopenfilename(
            initialdir=".", title="Open File...", filetypes=self.file_types
        )
        if not target_file:
            return
        target_path = Path(target_file)
        if not target_path.exists():
            messagebox.showinfo("Open", f"{target_path.name}\nfile not found.")
            return
        try:
            with open(target_path, "r", encoding="utf-8") as fin:
                self.npd.ta.delete("1.0", tk.END)
                self.npd.ta.insert("1.0", fin.read())
            self.update_status(target_path, True)
            self.npd.ta.mark_set("insert", "1.0")
        except Exception:
            self.update_status(target_path, False)
            self.file_name = "Untitled"
            self.saved = True
            self.npd.root.title(f"{self.file_name} - {self.application_title}")
        if not os.access(target_path, os.W_OK):
            self.new_file_flag = True

    def update_status(self, target_path, saved):
        target_path = Path(target_path)
        if saved:
            self.saved = True
            self.file_name = target_path.name
            if not os.access(target_path, os.W_OK):
                self.file_name += "(Read only)"
                self.new_file_flag = True
            self.file_ref = target_path
            self.npd.root.title(f"{self.file_name} - {self.application_title}")
            self.npd.status_bar.config(
                text=f"File : {target_path.resolve()} saved successfully."
            )
            self.new_file_flag = False
        else:
            self.npd.status_bar.config(
                text=f"Failed to save/open : {target_path.resolve()}"
            )

    def confirm_save(self):
        if not self.saved:
            choice = messagebox.askyesnocancel(
                self.application_title,
                f"The text in the {self.file_name} file has been changed.\nDo you want to save the changes?",
            )
            if choice is None:
                return False
            if choice is True:
                return self.save_as_file()
        return True

    def new_file(self, event=None):
        if not self.confirm_save():
            return
        self.npd.ta.delete("1.0", tk.END)
        self.file_name = "Untitled"
        self.file_ref = None
        self.saved = True
        self.new_file_flag = True
        self.npd.root.title(f"{self.file_name} - {self.application_title}")


class Notepad:
    def __init__(self):
        self.root = tk.Tk()
        self.application_name = "Notepad"
        self.root.geometry("700x500")

        main_frame = ttk.Frame(self.root, padding="5 5 5 0")
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.status_bar = ttk.Label(
            self.root, text="||       Ln 1, Col 1  ", anchor=tk.E, padding=(0, 2, 10, 2)
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        scrollbar = ttk.Scrollbar(main_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.ta = tk.Text(
            main_frame, wrap=tk.NONE, yscrollcommand=scrollbar.set, undo=True
        )
        self.ta.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.ta.yview)

        self.file_handler = FileOperation(self)
        self.create_menu_bar()
        self.bind_shortcuts()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.ta.bind("<KeyRelease>", self.on_key_release)
        self.root.mainloop()

    def create_menu_bar(self):
        # Master Menu bar object
        menubar = tk.Menu(self.root)

        # 1. FILE MENU
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(
            label="New", accelerator="Ctrl+N", command=self.file_handler.new_file
        )
        file_menu.add_command(
            label="Open...",
            accelerator="Ctrl+O",
            command=self.file_handler.open_file_dialog,
        )
        file_menu.add_command(
            label="Save", accelerator="Ctrl+S", command=self.file_handler.save_this_file
        )
        file_menu.add_command(
            label="Save As...", command=self.file_handler.save_as_file
        )
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)
        menubar.add_cascade(label="File", menu=file_menu)

        # 2. EDIT MENU (Maps Java standard menu variables like cutItem, copyItem...)
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(
            label="Undo",
            accelerator="Ctrl+Z",
            command=lambda: self.ta.event_generate("<<Undo>>"),
        )
        edit_menu.add_command(
            label="Redo",
            accelerator="Ctrl+Y",
            command=lambda: self.ta.event_generate("<<Redo>>"),
        )
        edit_menu.add_separator()
        edit_menu.add_command(
            label="Cut",
            accelerator="Ctrl+X",
            command=lambda: self.ta.event_generate("<<Cut>>"),
        )
        edit_menu.add_command(
            label="Copy",
            accelerator="Ctrl+C",
            command=lambda: self.ta.event_generate("<<Copy>>"),
        )
        edit_menu.add_command(
            label="Paste",
            accelerator="Ctrl+V",
            command=lambda: self.ta.event_generate("<<Paste>>"),
        )
        edit_menu.add_command(
            label="Delete",
            accelerator="Del",
            command=lambda: (
                self.ta.delete("sel.first", "sel.last")
                if self.ta.tag_ranges("sel")
                else self.ta.delete("insert")
            ),
        )
        edit_menu.add_separator()
        edit_menu.add_command(
            label="Find...",
            accelerator="Ctrl+F",
            command=lambda: print("Find requested"),
        )
        edit_menu.add_command(
            label="Find Next",
            accelerator="F3",
            command=lambda: print("Find Next requested"),
        )
        edit_menu.add_command(
            label="Replace...",
            accelerator="Ctrl+H",
            command=lambda: print("Replace requested"),
        )
        edit_menu.add_separator()
        edit_menu.add_command(
            label="Select All",
            accelerator="Ctrl+A",
            command=lambda: self.ta.tag_add("sel", "1.0", "end"),
        )
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # 3. FORMAT MENU (Word Wrap feature toggle)
        format_menu = tk.Menu(menubar, tearoff=0)
        self.word_wrap_var = tk.BooleanVar(value=False)
        format_menu.add_checkbutton(
            label="Word Wrap",
            variable=self.word_wrap_var,
            command=self.toggle_word_wrap,
        )
        format_menu.add_command(
            label="Font...",
            command=lambda: print("Font selection window dialog request"),
        )
        menubar.add_cascade(label="Format", menu=format_menu)

        # Mount Menu to Root Configuration Frame
        self.root.config(menu=menubar)

    def bind_shortcuts(self):
        # Binds systemic OS keystrokes explicitly to your Controller Methods
        self.root.bind("<Control-n>", self.file_handler.new_file)
        self.root.bind("<Control-o>", self.file_handler.open_file_dialog)
        self.root.bind("<Control-s>", self.file_handler.save_this_file)
        self.root.bind(
            "<Control-a>", lambda e: [self.ta.tag_add("sel", "1.0", "end"), "break"][1]
        )

    def toggle_word_wrap(self):
        if self.word_wrap_var.get():
            self.ta.config(wrap=tk.WORD)
        else:
            self.ta.config(wrap=tk.NONE)

    def on_key_release(self, event):
        if event.char and event.keysym not in (
            "Control_L",
            "Control_R",
            "Shift_L",
            "Shift_R",
            "Alt_L",
            "Alt_R",
            "Caps_Lock",
        ):
            self.file_handler.set_save(False)
        self.caret_update(event)

    def caret_update(self, event):
        try:
            row_col = self.ta.index(tk.INSERT)
            line, col = row_col.split(".")
            self.status_bar.config(text=f"||       Ln {line}, Col {int(col) + 1}  ")
        except Exception:
            pass

    def on_closing(self, event=None):
        if self.file_handler.confirm_save():
            self.root.destroy()
            sys.exit(0)


if __name__ == "__main__":
    Notepad()
