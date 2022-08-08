def alumno(name):
    print(f"Bienvenido {name} a la Escuela America Clinton")
name=input("Digita tu Nombre: ")

def calif():
    i=5
    num=0
    prom_fin=0
    while i>=1:
        prom=int(input(f"Digita tus calificaciones {i}: "))
        num=num+prom
        prom_fin=num/5
        i-=1
    print(f"SU claificacion promedio es de: {prom_fin}")

if __name__=='__main__':
    alumno(name)
    calif()