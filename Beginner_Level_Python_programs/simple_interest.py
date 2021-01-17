def simple_interest(principle,time,rate): 
    print('The principal is', principle) 
    print('The time period is', time) 
    print('The rate of interest is',rate) 
      
    si = (principal * time * rate)/100
      
    print('The Simple Interest is', si) 
    return si 
      

simple_interest(8, 6, 8) 