import markdown

with open("README.md", "r", encoding="utf-8") as input_file:
    text = input_file.read()
html = markdown.markdown(text)

with open("README.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
    output_file.write(html)
