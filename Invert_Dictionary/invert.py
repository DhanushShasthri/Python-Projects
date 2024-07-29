def invert_dictionary(d):
 #   key=[]
    value={}
    for u,v in d.items():
        value[v]=[u]
d={"name":"dhanush",
   "age":21,
   "gender":"male",
   "city":"hiriadka"}
invert_dictionary(d)
