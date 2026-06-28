import socket

# Function to scan ports
def scan_ports(target, start_port, end_port):
    print(f"\nScanning target: {target}")
    print(f"Scanning ports from {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        try:
            # Create socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # Try connecting
            result = s.connect_ex((target, port))

            if result == 0:
                print(f"Port {port} is OPEN")
            
            s.close()

        except KeyboardInterrupt:
            print("\nScan interrupted!")
            break

        except socket.gaierror:
            print("Hostname could not be resolved.")
            break

        except socket.error:
            print("Couldn't connect to server.")
            break


# Main program
if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    scan_ports(target, start_port, end_port)