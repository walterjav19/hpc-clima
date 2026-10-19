# Limpieza de datos NOAA GHCN-Daily (México y Centroamérica)
 
Proyecto: análisis meteorológico para el I Taller de HPC en CPU y GPU con Python (ECYS USAC y CeNAT, 10 de noviembre de 2026).


# Analisis climatologico de los ultimos 30 AÑOS

1366640 filas obtenidas del conjunto de datos de [NOAA](https://www.ncei.noaa.gov/)

## Resultado del conteo
 
| Variable | Valores útiles | % de las 1,366,640 filas |
|---|---|---|
| PRCP | 1,080,471 | 79 % |
| TAVG | 1,139,893 | 83 % |
| TMAX | 928,792 | 68 % |
| TMIN | 927,750 | 68 % |
 
- **Rango real de fechas:** 1938-08-01 a 2026-10-11.
- **Filas totales:** 1,366,640 registros diarios (estación-día).
- Guatemala no entra: NOAA solo tiene una estación (`GT000060100`) con cobertura muy corta.


## Hallazgos
 
1. **Rango:** la serie más antigua arranca en 1938
2. **Cada variable por separado** pasa el millón (PRCP y TAVG) o se acerca (TMAX y TMIN, ~930 mil).
3. **TAVG** está muy irregular: algunas estaciones solo tienen TAVG y no TMAX/TMIN. Para tendencias de temperatura conviene usar TMAX y TMIN, y TAVG solo donde no haya otra opción, o calcular `(TMAX + TMIN) / 2`.
4. **Estaciones desiguales:** por ejemplo `ES003800510` tiene muchas filas pero pocos TMAX y PRCP
5. **Unidades:** `TAVG = "  268"` en una estación de Chiapas sugiere **décimas de grado** (26.8 °C)
6. **Banderas `_ATTRIBUTES`:** formato `medición,calidad,fuente`. Si el campo de calidad (el segundo) no está vacío, el dato falló un control de NOAA y se descarta.
7. **SNWD** (nieve) no aplica a la región y se descarta.


## PRIMER ANALISIS

| País | Código | Estaciones | Filas | PRCP | TMAX | TMIN | TAVG | Desde | Hasta |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| México | MX | 73 | 1,147,202 | 973,126 | 808,776 | 799,624 | 945,503 | 1938-08-01 | 2026-10-11 |
| Honduras | HO | 5 | 75,877 | 50,024 | 39,385 | 44,409 | 73,445 | 1945-05-01 | 2025-12-11 |
| Costa Rica | CS | 3 | 56,939 | 26,216 | 37,786 | 38,851 | 51,181 | 1949-02-01 | 2025-08-24 |
| El Salvador | ES | 2 | 41,056 | 9,988 | 24,048 | 25,106 | 33,343 | 1956-01-03 | 2025-08-24 |
| Nicaragua | NU | 1 | 19,259 | 2,492 | 2,423 | 2,783 | 19,259 | 1942-10-01 | 2025-08-24 |
| Belice | BH | 1 | 16,196 | 11,538 | 8,469 | 9,072 | 16,196 | 1960-11-07 | 2025-08-24 |
| Panamá | PM | 2 | 10,111 | 7,087 | 7,905 | 7,905 | 966 | 1949-01-01 | 2026-10-10 |
| **Total** | | **87** | **1,366,640** | | | | | 1938-08-01 | 2026-10-11 |




- **México aporta el 84 % de las filas** (1,147,202 de 1,366,640) y 73 de las 87 estaciones. Los demás países suman solo el 16 %, así que un promedio "regional" estaría dominado por México. Conviene reportar tendencias por país o por estación.
- **Nicaragua tiene una sola estación con muy poca temperatura útil:** 19,259 filas, pero apenas ~2,400 valores de TMAX y TMIN (casi todo es TAVG), y solo 2,492 de PRCP. Para tendencias de TMAX/TMIN no sirve; solo serviría con TAVG.
- **Panamá tiene TAVG casi vacío** (966 valores en 10,111 filas), lo contrario de Nicaragua: sus datos útiles son TMAX, TMIN y PRCP.
- **El Salvador tiene muy poca PRCP** (9,988 en 41,056 filas), así que su análisis de lluvia sería débil.
- **Centroamérica en conjunto aporta pocas estaciones** (14), con series irregulares. 

