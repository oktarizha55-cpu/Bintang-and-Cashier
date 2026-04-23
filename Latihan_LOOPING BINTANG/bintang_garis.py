#bagian atas 
for i in range (2):
    for x in range (5):
        if x == 2:
            print ("*", end=" ")
        else:
            print ("-", end=" ")
    print ()

#garis penuh bintang 
for i in range (5):
    print ("*", end=" ")
print ()


#bagian tengah 
for i in range (2):
    for x in range (5):
        if x == 2:
            print ("*", end=" ")
        else:
            print ("-", end=" ")

    print ()  

# kotak bawah 
for i in range (5):
    print ("*",end= " ")
print()

for i in range (3): 
    for x in range (5):
        if x == 0 or x == 4: 
          print ("*", end=" ")
        else: 
            print("-",end=" ")
    print()

    for i in range(5):
        print("*", end=" ")
    print()         
