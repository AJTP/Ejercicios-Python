# Escribir un algoritmo que, dado el infinitivo de un verbo regular de la primera
# conjugación, obtenga la conjugación en singular y plural de presente de indicativo.
# Por ejemplo, para el verbo cantar el resultado es yo canto, tú cantas, el canta,
# nosotros cantamos, vosotros cantáis, ellos cantan.

verbo = (input("Introduce el verbo: "))
verbo=verbo.rstrip("ar")
print("Yo ", verbo+"o")
print("Tu ", verbo+"as")
print("Él ", verbo+"a")
print("Nosotros ", verbo+"amos")
print("Vosotros ", verbo+"ais")
print("Ellos ", verbo+"an")