import ctypes, subprocess

BUF_SIZE = 256
buffer = ctypes.create_unicode_buffer(BUF_SIZE)
ctypes.windll.kernel32.GetConsoleTitleW(buffer, BUF_SIZE)

window = buffer.value
print(buffer.value)
input("Introduce Enter para continuar")
a = "direccion"

process = subprocess.Popen('Write-Host "CP " -ForegroundColor blue -NoNewline; write-host '+a+'> ', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#process = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = process.communicate()

if stdout: print(stdout.decode('cp437'))
if stderr: print(stderr.decode('cp437'))