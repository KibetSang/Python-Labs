text = "  Hello, Python!  "

# Accessing and Slicing
first_char = text[2]  # 'H'
substring = text[9:15] # 'Python'

# Case Changing
uppercase_text = text.upper() # '  HELLO, PYTHON!  '

# Stripping Whitespace
cleaned_text = text.strip() # 'Hello, Python!'

# Replacing
new_text = cleaned_text.replace("Python", "World") # 'Hello, World!'

# Splitting
words = new_text.split(", ") # ['Hello', 'World!']

# Joining
rejoined_text = "-".join(words) # 'Hello-World!'

# F-string formatting
name = "Alice"
formatted_string = f"Welcome, {name}!" # 'Welcome, Alice!'