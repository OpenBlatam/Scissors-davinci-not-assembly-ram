import subprocess

# Execute a command (a simple "echo" command in this case)
result = subprocess.run(['echo', 'Hello, Network!'], stdout=subprocess.PIPE)

# To get the output of the command
output = result.stdout.decode('utf-8')

print(output)  # Prints: Hello, Network!
