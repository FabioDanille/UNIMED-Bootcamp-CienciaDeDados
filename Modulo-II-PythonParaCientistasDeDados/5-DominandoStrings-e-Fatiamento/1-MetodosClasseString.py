curso = "pYtHon"

print(curso.upper()) # PYTHON
print(curso.lower()) # python
print(curso.title()) # Python


curso = "     Python "

print(curso.strip()) # "Python"
print(curso.lstrip()) # "Python "
print(curso.rstrip()) # "   Python"


curso = "Python"

print(curso.center(10, "#")) # "##Python##"
print(".".join(curso)) # "P.y.t.h.o.n"