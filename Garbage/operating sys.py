import os
if(not os.mkdir("Garbage/Data")):
    os.mkdir("Garbage/Data")

for i in range(0,10):
    print(os.mkdir(f"Day{i+1}"))