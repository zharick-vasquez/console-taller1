from datetime import datetime

class Note:
    HIGH : str = "HIGH"
    MEDIUM : str = "MEDIUM"
    LOW : str = "LOW"

    def __init__(self, code:str, title:str, text: str, importance: str):
        self.tag = None
        self.code : str = code
        self.title : str = title
        self.text : str = text
        self.importance : str = importance
        self.tags : list[str] = []
        creation_date : datetime = datetime.now()

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tag.append(tag)
            print(f"Etiqueta '{tag}' añadida.")
        else:
            print(f"La etiqueta '{tag}' ya está en los tags.")

    def __str__(self)  -> str:
        return f"Date: {datetime.now} {self.title}: {self.text}"

class Notebook:
    def __init__(self, notes: list[Note]):
        notes: list[Note]






