palabra = input()

end = len(palabra)-1
ver = True
for x in range(len(palabra)//2):
    if palabra[x] != palabra[end]:
            print("no es palindromo")
            ver = False
            break
    end -= 1;

if ver == True:
    print("es palindromo")

