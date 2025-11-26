from libraries import *

class TextEditor(App):
    CSS = """
        TextArea {
            height: 1fr;
        }
    """
    BINDINGS = [
        ("ctrl+d", "toggle_dark", "Toggle dark mode"),
        ("ctrl+s", "save", "Save")
        ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield TextArea(language="markdown", id="main_editor")
        yield Footer()

    def action_toggle_dark(self) -> None:   # An action to toggle dark mode.
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
    
    def action_save(self) -> None:
        editor = self.query_one("#main_editor", TextArea)
        content = editor.text

        try:
            file = filedialog.asksaveasfile(initialdir="/home/simone/Documenti/",
            defaultextension=".md",
            filetypes=[
                ("Markdown File", ".md")
            ])
            if file != None:
                file.write(content)
                file.close()
                with open("bozza.md", "w") as f:
                    f.write(content)
        
                self.notify("Salvato come bozza")
        except Exception as e:
            with open("error_log.txt", "a") as f:
                f.write(f"[ERROR]: {e}")

            self.notify("ERROR, file not save. More info in error_log.txt")
