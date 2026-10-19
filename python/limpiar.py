import pandas as pd, glob, os

RAW = "../raw"
OUT = "../parquet"
os.makedirs(OUT, exist_ok=True)

VARS = ["PRCP", "TMAX", "TMIN", "TAVG"]
frames = []
for f in sorted(glob.glob(os.path.join(RAW, "*.csv"))):
    d = pd.read_csv(f, low_memory=False)
    d["DATE"] = pd.to_datetime(d["DATE"])
    for v in VARS:
        if v not in d:
            d[v] = pd.NA
            d[v + "_ATTRIBUTES"] = pd.NA
        d[v] = pd.to_numeric(d[v], errors="coerce")
        # bandera: medición,calidad,fuente -> si calidad no está vacía, descartar
        calidad = d[v + "_ATTRIBUTES"].astype("string").str.split(",", expand=True).reindex(columns=[0, 1, 2]).iloc[:, 1]
        d.loc[calidad.notna() & (calidad.str.strip() != ""), v] = pd.NA
    d["PAIS"] = d["STATION"].str[:2]
    frames.append(d[["STATION", "PAIS", "DATE", "LATITUDE", "LONGITUDE",
                     "ELEVATION", "NAME"] + VARS])

df = pd.concat(frames, ignore_index=True)
df = df.drop_duplicates(["STATION", "DATE"]).sort_values(["STATION", "DATE"])

print("Filas:", len(df))
print(df[VARS].describe())
print("Duplicados removidos:", sum(len(f) for f in frames) - len(df))
df.to_parquet(os.path.join(OUT, "clima_ca_mx.parquet"))