s=int(input());#no. of test
a=[];
b=[];
#name of city data input
for i in range(1,s+1):
    n=int(input("enter no of city"));
    for i in range(1,n+1):
        name=input("name of city");
        p=int(input("no of neighbours of city"+name));
        for i in range(1,p+1):
            nr=int(input("index of city"));
            cost=int(input("cost of travlling"));
            a.append(nr);#index of city
            b.append(cost);#coost of travll
r=int(input("no of path to find"));

