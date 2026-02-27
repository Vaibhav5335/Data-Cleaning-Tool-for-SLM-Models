import re

# Open the file and read its content
with open("123.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Remove all occurrences of [number]
cleaned_content = re.sub(r'\[\d+\]', '', content)

# Optionally, remove extra spaces left after removal
cleaned_content = re.sub(r'\s+', ' ', cleaned_content).strip()

# Write the cleaned content back to a file
with open("cleaned_file.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_content)

print("Text cleaned successfully!")