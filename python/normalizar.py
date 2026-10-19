import pandas as pd, glob

paises={
    "MX":"México",
    "BH":"Belice",
    "GT":"Guatemala",
    "ES":"El Salvador",
    "HO":"Honduras",
    "NU":"Nicaragua",
    "CS":"Costa Rica",
    "PM":"Panamá"
}

filas = []
for f in sorted(glob.glob("../raw/*.csv")):
    d = pd.read_csv(f, low_memory=False)
    filas.append({
        "estacion": d["STATION"].iloc[0],
        "filas": len(d),
        "desde": d["DATE"].min(),
        "hasta": d["DATE"].max(),
        "prcp": d["PRCP"].notna().sum() if "PRCP" in d else 0,
        "tmax": d["TMAX"].notna().sum() if "TMAX" in d else 0,
        "tmin": d["TMIN"].notna().sum() if "TMIN" in d else 0,
        "tavg": d["TAVG"].notna().sum() if "TAVG" in d else 0,
    })

r = pd.DataFrame(filas)


# print(r[["filas", "prcp", "tmax", "tmin", "tavg"]].sum())
# print("Fecha más antigua:", r["desde"].min(), "| más reciente:", r["hasta"].max())
# print(r.sort_values("filas", ascending=False).head(10))

#crear una nueva columna truncando el nombre de la estación para obtener el país
r["pais_abreviatura"]=r["estacion"].str[:2]
r["pais"]=r["pais_abreviatura"].map(paises)



resumen=r.groupby(["pais_abreviatura", "pais"]).agg(
    estaciones=("estacion", "count"),
    filas=("filas", "sum"),
    prcp=("prcp", "sum"),
    tmax=("tmax", "sum"),
    tmin=("tmin", "sum"),
    tavg=("tavg", "sum"),
    desde=("desde", "min"),
    hasta=("hasta", "max")
).sort_values("filas", ascending=False)

print(resumen)
