# Read a Text File Line by Line
with open('../data/notes.txt', 'r', encoding='utf-8') as file:
    for line_number, line in enumerate(file, start=1):
        print(f"Line {line_number}: {line.strip()}")
        #strip() removes the new line at the end
    