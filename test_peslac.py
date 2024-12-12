from peslac import Peslac

# Initialize the Peslac client
api_key = "api-key"  # Replace with your actual API key
client = Peslac(api_key)

# Path to the local file
file_path = "sample.png"  # Replace with the actual file path

try:
    # Use the tool with the local file
    response = client.parser(file_path)
    print("Tool Response:", response)
except Exception as e:
    # Print the exception message
    print("Error using the tool with a local file:")
    print(str(e))
