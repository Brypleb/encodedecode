# importing code from python modules
import urllib.parse
import sys
import base64

# main function
if __name__ == "__main__":

    # A quick check to see if the user inputed 3 command line arguments
    # If not, a usage example will be given to show how to use the script
    
    if len(sys.argv) != 3:
        print("Usage: python3 encodedecode.py <urlencode|urldecode|base64encode|base64decode|hexencode|hexdecode> <string>")
        sys.exit(1)

    # This function will take a string and url encode it
    def urlencode(string):
        try:
            print(urllib.parse.quote(string))
        except Exception as e:
            print(f"An error has occured in the function urlencode: {e}")

    # This function will take a string and url decode it
    def urldecode(string):
        try:
            print(urllib.parse.unquote(string))
        except Exception as e:
            print(f"An error has occured in the function urldecode: {e}")

    # This function will take a string and base64 encode it
    def base64encode(string):
        try:
            bytes_object = string.encode('utf-8')
            print(base64.b64encode(bytes_object).decode('utf-8'))
        except Exception as e:
             print(f"An error has occured in the function base64encode: {e}")

    # This function will take a string and base64 decode it
    def base64decode(string):
        try:
            print(base64.b64decode(string).decode('utf-8'))
        except Exception as e:
            print(f"An error has occured in the function base64decode: {e}")

    # This function will take a string and hex encode it
    def hexencode(string):
        try:
            print(string.encode('utf-8').hex())
        except Exception as e:
            print(f"An error has occured in the function hexencode: {e}")

    # This function will take a string and hex decode it
    def hexdecode(string):
        try:
            print(bytes.fromhex(string).decode('utf-8'))
        except Exception as e:
            print(f"An error has occured in the function hexdecode: {e}")

    # This takes the first command line argument and stores it in the option variable
    option = sys.argv[1].lower()

    # The option variable will then be compared to some possibilities to see which function to use
    if option == "urlencode":
        urlencode(sys.argv[2])
    elif option == "urldecode":
        urldecode(sys.argv[2])
    elif option == "base64encode":
        base64encode(sys.argv[2])
    elif option == "base64decode":
        base64decode(sys.argv[2])
    elif option == "hexencode":
        hexencode(sys.argv[2])
    elif option == "hexdecode":
        hexdecode(sys.argv[2])
    else:
    # If the options variable does not fit an option, the usage example message is shown
        print("Usage: python3 encode.py <urlencode|urldecode|base64encode|base64decode|hexencode|hexdecode> <string>")
