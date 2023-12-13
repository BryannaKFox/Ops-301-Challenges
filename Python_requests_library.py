

import requests

def translate_status_code(status_code):
    status_codes = {
        200: 'OK',
        201: 'Created',
        204: 'No Content',
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        500: 'Internal Server Error'
        
    }
    return status_codes.get(status_code, 'Unknown Status Code')

def main():
    # Get destination URL from the user
    destination_url = input("Enter the destination URL: ")

    # Get HTTP Method from the user
    http_method = input("Choose HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

    # Print the request information
    print(f"\nRequest about to be sent:\nURL: {destination_url}\nMethod: {http_method}")

    # Confirm before proceeding
    confirmation = input("Do you want to proceed? (yes/no): ").lower()

    if confirmation != 'yes':
        print("Operation canceled.")
        return

    # Perform the request using the requests library
    response = requests.request(http_method, destination_url)

    # Print translated status code
    translated_status = translate_status_code(response.status_code)
    print(f"\nResponse Status: {response.status_code} - {translated_status}")

    # Print response header information
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

if __name__ == "__main__":
    main()
