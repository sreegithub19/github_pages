# Define the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Web Page</title>
</head>
<body>
    <h1>Welcome to My Web Page</h1>
    <p>This page is generated using Python!</p>
</body>
</html>
"""

# Specify the filename
filename = "my_web_page.html"

# Write the HTML content to the file
with open(filename, "w") as file:
    file.write(html_content)

print(f"HTML file '{filename}' has been created.")
