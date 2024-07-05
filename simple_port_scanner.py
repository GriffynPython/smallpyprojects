import socket

def is_port_in_use(port: int) -> bool:# This is the syntax to create a bool function with the argument an integer named port.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

# Example usage
port_to_check = int(input("Enter a valid port number")) #Checking if the smb port is open or not
port_descriptions={80:"HTTP(Web)",21:"FTP",445:"SMB",443:"HTTPS (Secure Web)",23:"SSH (Secure Shell)"}
if is_port_in_use(port_to_check):
    print(f"Port {port_to_check} ({port_descriptions.get(port_to_check, 'Unknown')}) is open.")
else:
    print(f"Port {port_to_check} is not open.")