from html.parser import HTMLParser
import os

class PresidencyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.is_in_galery = False #galery est la valeur de l'attribut class sur la page web
        self.is_in_a = False      # ici a est une balise de lien 
        self.current_text = []
        self.output_file = "data/raw/presiData.csv"
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        with open(self.output_file, "a", encoding="utf-8") as file:
            file.write("nom_president,mandat" + "\n")

    def handle_starttag(self, tag, attrs):
        if tag == "ul" and any(attr == ("class", "galery") for attr in attrs):
            self.is_in_galery = True
        if self.is_in_galery and tag == "a":
            self.is_in_a = True

    def handle_endtag(self, tag):
        if tag == "a" and self.is_in_a:
            self.is_in_a = False
            full_text = ",".join(self.current_text).strip()
            if full_text:
                with open(self.output_file, "a", encoding="utf-8") as file:
                    file.write(full_text + "\n")
                #print(full_text)
            self.current_text = []
        if tag == "ul" and self.is_in_galery:
            self.is_in_galery = False

    def handle_data(self, data):
        if self.is_in_a and data.strip():
            self.current_text.append(data.strip())


