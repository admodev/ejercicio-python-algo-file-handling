# Solución:

# Lista con los valores sin ordenar
energy = [-8828.815340, -826.799580, -8826.860560, -8543.593749, -850935.1498745, -8504.69876857]

# Abrir archivo de texto nuevo con derechos de escritura para guardar el menor valor
lowestNumbers = open("lowestNumbersFile.txt", "w+")

# Método para organizar la lista 'energy' de menor a mayor
energy.sort()

# Método para seleccionar el menor valor y pasarlo a String para poder escribirlo en el archivo de texto que creamos
minNum = str(min(energy))

# Escribir el valor en el archivo
lowestNumbers.write(minNum)

# Cerrar el archivo creado con el valor escrito
lowestNumbers.close()
