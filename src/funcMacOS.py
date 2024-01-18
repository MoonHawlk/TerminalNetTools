import subprocess

def getIpConfig():
    result = subprocess.run(['ifconfig'], capture_output=True, text=True)
    print("==========================================================")
    print("Informações da rede:", result.stdout)
    print("==========================================================")

def getPublicIP():
    result = subprocess.run(['curl', 'ifconfig.me'], capture_output=True, text=True)
    print("==========================================================")
    print("Endereço IP Público:", result.stdout.strip())
    print("==========================================================")

def getOpenPorts():
    result = subprocess.run(['lsof', '-i'], capture_output=True, text=True)
    print("==========================================================")
    print("Portas abertas:", result.stdout)
    print("==========================================================")

def getPing():
    print("==========================================================")
    host_to_ping = str(input("Digite o site que deseja verificar o ping: "))
    print("==========================================================")

    result = subprocess.run(['ping', '-c', '4', host_to_ping], capture_output=True, text=True)
    print("==========================================================")
    print(f"Informações da conexão com {host_to_ping}:")
    print(result.stdout)
    print("==========================================================")

def getInfoDns():
    result = subprocess.run(['scutil', '--dns'], capture_output=True, text=True)
    print("==========================================================")
    print("Informações sobre Conexões DNS:")
    print(result.stdout)
    print("==========================================================")


def getRoutingTable():
    result = subprocess.run(['netstat', '-rn'], capture_output=True, text=True)
    print("==========================================================")
    print("Tabela de Roteamento:")
    print(result.stdout)
    print("==========================================================")
