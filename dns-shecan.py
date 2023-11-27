import subprocess
import msvcrt


def set_dns_server(primary_dns, secondary_dns, interface_name='Wi-Fi'):
    try:
        command = f'netsh interface ip set dns name="{interface_name}" static {primary_dns} primary'
        subprocess.run(command, check=True, shell=True)

        command = f'netsh interface ip add dns name="{interface_name}" {secondary_dns} index=2'
        subprocess.run(command, check=True, shell=True)

        print(
            f"DNS servers set to {primary_dns} and {secondary_dns} for {interface_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except OSError as e:
        print(f"OS Error: {e}")


def clear_dns_servers(interface_name='Wi-Fi'):
    try:
        command = f'netsh interface ip delete dns name="{interface_name}" all'
        subprocess.run(command, check=True, shell=True)
        print(
            f"The DNS servers for {interface_name} have been successfully cleared.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except OSError as e:
        print(f"OS Error: {e}")


print("Choose :")
print("1. Set DNS Servers")
print("2. Clear DNS Servers")

choice = input("Enter your choice: ")

if choice == "1":
    primary_dns = '178.22.122.100'
    secondary_dns = '185.51.200.2'
    set_dns_server(primary_dns, secondary_dns)
elif choice == "2":
    clear_dns_servers()
else:
    print("Error.")

print("Press any key to exit...")
while not msvcrt.kbhit():
    pass
