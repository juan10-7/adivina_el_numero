# input
import random
usu=int(input("dijite su numero"))

# processing

maq=random.randint(1,100)

i=1

while usu!= maq:


  if usu<maq:
        print("fallaste,el numero que toca adivinar es mayor" ) 
        usu=int(input("dijite su numero"))
        i=i+1

  else: 
        print("fallaste el numeo es menor,intentalo de nuevo")
        usu=int(input("dijite su numero"))
        i=i+1

if usu==maq:
    print("adivinaste,te tomo" +str(i)+ "intentos")



    


































