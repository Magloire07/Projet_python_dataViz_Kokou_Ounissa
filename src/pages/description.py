from dash import html

def description_page():
    texts=[]
    with open("assets/description.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            texts.append(line)
    return html.Div(
         texts,
         className="descr")
