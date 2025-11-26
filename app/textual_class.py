from libraries import *

class TextEditor(App):
    CSS = """
        TextArea {
            height: 1fr;
        }
    """
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield TextArea(language="markdown", id="main-editor")
        yield Footer()

    def action_toggle_dark(self) -> None:   # An action to toggle dark mode.
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )