import os

def get_nmap(options, ip):
    command = "nmap " + options + " " + ip
    process = os.popen(command)

    results = str(process.read())

    return results

print(get_nmap('-F', '8.8.8.8'))
