# Conjunto total de ciudadanos
ciudadanos = {f"Ciudadano {i}" for i in range(1, 501)}

# Vacunados con Pfizer (75)
pfizer = {f"Ciudadano {i}" for i in range(1, 76)}

# Vacunados con AstraZeneca (75)
astra = {f"Ciudadano {i}" for i in range(51, 126)}

# Operaciones de conjuntos
ambas_dosis = pfizer & astra
solo_pfizer = pfizer - astra
solo_astra = astra - pfizer
vacunados = pfizer | astra
no_vacunados = ciudadanos - vacunados

print("REPORTE DE VACUNACIÓN COVID-19")
print("------------------------------")
print("Total ciudadanos:", len(ciudadanos))
print("No vacunados:", len(no_vacunados))
print("Ambas dosis:", len(ambas_dosis))
print("Solo Pfizer:", len(solo_pfizer))
print("Solo AstraZeneca:", len(solo_astra))