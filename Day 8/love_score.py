def calculate_love_score(name1,name2):
    array = []
    for char in name1.lower() :
        array.append(char)
    for char in name2.lower() :
        array.append(char)
    
    total1 = 0
    for char in  ['t','r','u','e'] : 
        total1 += array.count(char)
        
    total2 = 0 
    for char in  ['l','o','v','e']  :
        total2 += array.count(char)
        
    print(f'Love Score = {str(total1)+str(total2)}')
    
    
calculate_love_score("Kanye West", "Kim Kardashian")
        