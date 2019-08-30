try:

	import paramiko, time
	from getpass import getpass
	print("REQUISITOS COMPLETADOS\n")
	time.sleep(2)

except:

	print("TE FALTAN REQUISITOS")
	print("INSTALANDO REQUISITOS...")

	import os
	os.system("pip install paramiko")

	import paramiko, time
	from getpass import getpass
	time.sleep(2)
autor = "MANZA"
print("\n"*50)
print(f"MEDIDOR DE TEMPERATURA DE LA RASPBERRY PI BY {autor}\n")

ip = input("Introduce la ip de tu Raspberry PI: ")
usuario = input("Introduce el usuario: ")
clave = getpass("Introduce la clave de acceso: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip, username=usuario, password=clave)
print("\n")
print("Credenciales correctas.")
tiempo = int(input("Introduce el tiempo de refresco: "))
print("\n")
while True:
	try:
		stdin, stdout, stderr = client.exec_command('cat /sys/class/thermal/thermal_zone0/temp')
		for line in stdout:
			t = line[:2]
			c = line[2:]
			if t >= '50':
				print(f" [PELIGRO] Temperatura: {t}º, centesimas: {c}",end = '')
			if t <= '49' and t >= '44':
				print(f" [WARNING] Temperatura: {t}º, centesimas: {c}",end = '')
			if t <= '43':
				print(f" [NORMAL] Temperatura: {t}º, centesimas: {c}",end = '')
			time.sleep(tiempo)
	except KeyboardInterrupt:
		print("\n"*50)
		print("Se ha detenido el programa")
		client.close()
		input("Enter para continuar...")
		break
