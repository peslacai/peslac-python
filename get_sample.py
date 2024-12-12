from peslac import Peslac

# Initialize the Peslac client
api_key = "api-key"  # Replace with your actual API key
client = Peslac(api_key)

# Document ID to retrieve
document_id = "document-id"

try:
    # Retrieve the document
    response = client.retrieve_document(document_id)
    print("Document Response:", response)
except Exception as e:
    # Print the exception message
    print("Error retrieving document:")
    print(str(e))
