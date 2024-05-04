def eliminar_duplicados(lista):
  lista_sin_duplicados = []
  for elemento in lista:
    if elemento not in lista_sin_duplicados:
      lista_sin_duplicados.append(elemento)
  return lista_sin_duplicados

lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_procesada = eliminar_duplicados(lista_original)
print(f"Lista original: {lista_original}")
print(f"Lista procesada: {lista_procesada}")