import pandas as pd

# DataFrame pequeño de ejemplo: lecturas de 4 estaciones
df = pd.DataFrame({
    "ESTACION": ["GT001", "GT002", "MX001", "SV001"],
    "PAIS":     ["GT", "GT", "MX", "SV"],
    "TMAX":     [31.2, 28.5, 35.0, 33.1],
    "TMIN":     [18.4, 15.0, 22.3, 21.7],
    "PRCP":     [0.0, 12.5, 3.2, 0.0],
})

print("DataFrame completo:")
print(df)
#   ESTACION PAIS  TMAX  TMIN  PRCP
# 0    GT001   GT  31.2  18.4   0.0
# 1    GT002   GT  28.5  15.0  12.5
# 2    MX001   MX  35.0  22.3   3.2
# 3    SV001   SV  33.1  21.7   0.0
#
# Posiciones de columnas: 0=ESTACION, 1=PAIS, 2=TMAX, 3=TMIN, 4=PRCP
# iloc siempre usa POSICIONES (números), nunca nombres: iloc[filas, columnas]


print("\n1) Un solo valor -> iloc[fila, columna]")
print(df.iloc[1, 2])          # fila 1, columna 2 (TMAX de GT002) -> 28.5


print("\n2) Una fila completa -> iloc[fila]  (sin coma = filas)")
print(df.iloc[0])             # devuelve una Series con los datos de GT001


print("\n3) Una columna completa -> iloc[:, columna]")
print(df.iloc[:, 2])          # todas las filas, columna TMAX


print("\n4) Varias filas seguidas (slice) -> iloc[inicio:fin]  (fin NO se incluye)")
print(df.iloc[1:3])           # filas 1 y 2


print("\n5) Varias columnas seguidas -> iloc[:, inicio:fin]")
print(df.iloc[:, 2:5])        # TMAX, TMIN, PRCP


print("\n6) Filas y columnas específicas con listas")
print(df.iloc[[0, 2], [0, 2, 3]])   # filas 0 y 2; columnas ESTACION, TMAX, TMIN


print("\n7) Posiciones negativas: cuentan desde el final")
print(df.iloc[-1])            # última fila (SV001)
print(df.iloc[:, -1])         # última columna (PRCP)


print("\n8) Un rango de filas de una sola columna")
print(df.iloc[:2, 0])         # primeras 2 estaciones


print("\n9) Filtrar con una máscara booleana (debe ser lista/array, no Series)")
mascara = (df["PRCP"] > 0).to_numpy()
print(df.iloc[mascara, [0, 4]])     # estaciones con lluvia y su PRCP


print("\n10) Modificar un valor con iloc")
df2 = df.copy()
df2.iloc[0, 4] = 1.8         # cambia PRCP de GT001
print(df2)


print("\n11) Diferencia Series vs DataFrame al seleccionar una columna")
print(type(df.iloc[:, 2]))    # Series      -> columna sola
print(type(df.iloc[:, [2]]))  # DataFrame   -> lista con una columna


print("\n12) Error típico: posición fuera de rango")
try:
    df.iloc[:, 10]
except IndexError as e:
    print("IndexError:", e)
