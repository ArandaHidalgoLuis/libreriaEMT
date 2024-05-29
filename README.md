if __name__ == "__main__":
    numeroParada = input("Escribe el número de parada que deseas consultar: ")
    liBuses = inicializar(numeroParada)
    bus_identifiers = devolverNBuses(liBuses)
    bus_times = devolverTBuses(liBuses)

   print("Identificadores de buses:", bus_identifiers)
   print("Tiempos de buses:", bus_times)