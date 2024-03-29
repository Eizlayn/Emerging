import requests

# Base URL for the Webex API
WEBEX_BASE_URL = 'https://webexapis.com/v1'

# Function to authenticate with Webex API using provided access token
def authenticate_webex(access_token):
    try:
        url = f'{WEBEX_BASE_URL}/people/me'
        headers = {'Authorization' : f'Bearer {access_token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for any request errors
        print("Connection to Webex successful!")  # Print success message
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")  # Print error message if request fails

def test_connection(access_token):
    try:
        #Define the URL for the Webex API endpoint to fetch user data
        url = 'https://webexapis.com/v1/people/me'

        #Prepare the headers with the authorization token
        headers = {
            'Authorization' : 'Bearer {}'.format(access_token)
        }

        #Send a GET request to the Webex API endpoint with the header
        response = requests.get(url, headers=headers)
        
        #Check if the response status code indicates success(200)
        if response.status_code != 200:
            #error message
            print("\n--------------------------------------------------")
            print("Failed to connect to the server. Please try again.")
            print("--------------------------------------------------")
        else:
            #success message
            print("\n************************")
            print(" Successfully Connected ")
            print("************************")
            
            while True:
                #Offer options to the user after successful connection
                print("\n--------------------------")
                print("| 1 | Back To Menu        |")
                print("| 2 | Exit                |")
                print("--------------------------")
                nav = int(input("Enter your choice: "))
            
                if nav == 1:
                    return
                elif nav == 2:
                    print("\nExiting The Program...")
                    exit(0)
                else:
                    print("\n* Invalid choice. Please enter 1 or 2. *")

    #Handle exceptions that might occur during the execution of the code 
    except Exception as e:
        #error message
        print("An error occurred:", e)

# Function to display user information retrieved from Webex API
def display_user_information(access_token):
    try:
        url = f'{WEBEX_BASE_URL}/people/me'
        headers = {'Authorization' : f'Bearer {access_token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for any request errors
        
        user_data = response.json()  # Extract JSON data from response
        # Print user information
        print("\nYour Name : " + user_data["displayName"])
        print("Your Nickname : " + user_data["nickName"])
        print("Your E-Mail : " + user_data["emails"][0]) 
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")  # Print error message if request fails

# Function to list rooms available to the user
def list_rooms(access_token):
    try:
        url = f'{WEBEX_BASE_URL}/rooms'
        headers = {'Authorization' : f'Bearer {access_token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for any request errors
        
        rooms = response.json()['items'][:6]  # Extract room data from response
        for room in rooms: 
            # Print room details
            print("\nYour Room ID : " + room["id"])
            print("The Room Title : " + room["title"])
            print("Date Created : " + room["created"])
            print("Last Activity : " + room["lastActivity"])
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")  # Print error message if request fails

# Function to create a new room
def create_room(access_token):
    try:
        url = f'{WEBEX_BASE_URL}/rooms'
        headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
        room_title = input("Enter Your New Room Title: ")
        data = {'Title': room_title}
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print("New Room Created Successfully!")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Function to send a message to a room
def send_message(access_token):
    try:
        url = f'{WEBEX_BASE_URL}/rooms'
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        rooms = response.json()['items']
        for i, room in enumerate(rooms, start=1):
            print(f"{i}. {room['title']}")

        room_number = int(input("Choose Room: "))
        message = input("Enter Your Message: ")

        selected_room_id = rooms[room_number - 1]['id']
        url = f'{WEBEX_BASE_URL}/messages'
        headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
        data = {'roomId': selected_room_id, 'text': message}
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print("Message sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Main function to interact with the user
def main():
    print("Welcome To My Webex Tool")
    access_token = input("Enter your Webex Access Token: ").strip()  # Prompt for access token
    authenticate_webex(access_token)  # Authenticate with Webex API using access token
    
    # Main loop for user interaction
    while True:
        print("\n+-------------------------------+")
        print("| 0. |      Test Connection     |")
        print("|-------------------------------|")
        print("| 1. | Display Your Information |")
        print("|-------------------------------|")
        print("| 2. |    List Of Your Rooms    |")
        print("|-------------------------------|")
        print("| 3. |      Create New Room     |")
        print("|-------------------------------|")
        print("| 4. | Send Message To Any Room |")
        print("|-------------------------------|")
        print("| 5. |           Exit           |")
        print("+-------------------------------+")

        choice = int(input("\nEnter Your choice: "))  # Prompt for user choice
        if choice == 0:
            test_connection(access_token) #Test connection to the server
        elif choice == 1:
            display_user_information(access_token)  # Display user information
        elif choice == 2:
            list_rooms(access_token)  # List available rooms
        elif choice == 3:
            create_room(access_token)  # Create a new room
        elif choice == 4:
            send_message(access_token)  # Send a message to a room
        elif choice == 5:
            print("Exiting The Program...")
            exit(0)  # Exit the program
            break
        else:
            print("Invalid option. Please try again.")  # Handle invalid user input

# Entry point of the script
if __name__ == "__main__":
    main()
