#zdefinowane wartości
i = 1
side = 1 # kierunek [1 = zwiększaj / 0 = zmniejszaj ]
maks = 20 # Ile znaków maksimum w linii [maksimum]

# start pętli
while True: 
          if (side == 1):
                    if  (i <=maks):
                              print("*"*i)
                              i = i+1                       
                              if (i ==maks):
                                        side = 0            
          else:
                    if (i >= 1):
                              print("*"*i)
                              i = i-1                       
                              if (i ==1):
                                        side = 1
          
