import pandas as pd 

Tabla = {
        "Productos": ["Manzanas", "Naranjas", "Platanos", "Uvas", "Peras"],
        "Precio": [100,80,60,120,90],
        "Stock": [30,50,20,60,40]
}

df = pd.DataFrame(Tabla)
print (df)

df.set_index("Productos", inplace=True)
print (df)

nuevo_orden = ["Uvas", "Manzanas", "Melones", "Naranjas", "Peras ", "Platanos"]
df_reindexado = df.reindex(nuevo_orden)
print (df_reindexado)

df_renombrado = df.rename(index={"Manzanas":"Aples", "Naranjas": "Oranges"})
print (df_renombrado)

df_reset = df.reset_index ()
print (df_reset)