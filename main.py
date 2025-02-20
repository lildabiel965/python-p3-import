import requests # type: ignore

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())  # Fetch a sample JSON response
