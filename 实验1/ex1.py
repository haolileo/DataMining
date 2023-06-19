from sklearn.preprocessing import OneHotEncoder
#age<=30:0;31~40:1;age>40:2
#low:0;medium:1;high:2
#now:0;yes:1
#fail:0;excellent:1
x=[[0,2,0,0],[0,2,0,1],[1,2,0,0],[2,1,0,0],[2,0,1,0],[2,0,1,1],[1,0,1,1],
   [0,1,0,0],[0,0,1,0],[2,1,1,0],[0,1,1,1],[1,1,0,1],[1,2,1,0],[2,1,0,1]]
enc=OneHotEncoder(sparse=False)
enc.fit(x)
result=enc.transform(x)
print(result)