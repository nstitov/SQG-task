import sys

try:
    replaces_file_name, text_file_name = sys.argv[1:3]
except ValueError:
    print("Names of both files must be passed as command line arguments.")
    raise


with open(replaces_file_name, "r", encoding="utf-8") as replaces_file:
    replaces = {}
    for line in replaces_file:
        old, new = line.strip().split("=")
        replaces[old] = new

with open(text_file_name, "r", encoding="utf-8") as text_file:
    replaced_lines = []
    for line in text_file:
        line = line.strip()
        total_replacements = 0

        for old, new in replaces.items():
            total_replacements += line.count(old) * len(old)
            line = line.replace(old, new)

        replaced_lines.append((line, total_replacements))


for line, counter in sorted(replaced_lines, key=lambda pair: pair[1], reverse=True):
    print(line)
