#API Data Processor

#Call a public API and:

#•⁠  ⁠Fetch data
#•⁠  ⁠Parse JSON
#•⁠  ⁠Display meaningful insights

# API Data Processor
# Fetch data from a public API
# Parse JSON
# Display meaningful insights

import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
    response.raise_for_status()

    # Parse JSON
    users = response.json()

    # Display meaningful insights
    print("=" * 50)
    print("API DATA PROCESSOR")
    print("=" * 50)

    print(f"Total Users: {len(users)}\n")

    for user in users:
        print(f"Name    : {user['name']}")
        print(f"Username: {user['username']}")
        print(f"Email   : {user['email']}")
        print(f"City    : {user['address']['city']}")
        print(f"Company : {user['company']['name']}")
        print("-" * 50)

except requests.exceptions.RequestException as e:
    print("Error:", e)
    print(type(data))
    print(data[0])