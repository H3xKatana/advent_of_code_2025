
items = []
invalid = 0

with open("input.txt") as f : 
    data = f.read().strip().split(",")
    #print(data)
    for item in data :
        items.append(item.split("-"))
        items[-1][0] = int(items[-1][0])
        items[-1][1] = int(items[-1][1])
        
    for i in items :
        #print(f"Checking range {i[0]} to {i[1]}") 
        for v in range(i[0], i[1]+1):
            str_v = str(v)
            mid = len(str_v) // 2
            if len(str_v) % 2 == 0 :
                #print(f"Checking {v}")
                #print(f"Adding {v} to password")
                if str_v[:mid] == str_v[mid:]:
                    print(f"Valid: {v}")
                    invalid += v 

    print(invalid)
    #34826702005
    #print(items)   
        
        