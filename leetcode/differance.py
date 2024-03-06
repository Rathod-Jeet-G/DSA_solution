s = "a"
t = "aa"
st = {}

for i in s:
    if i in st:
        st[i]+=1
    else:
        st[i] = 1
for i in t:
    if i in st:
        st[i] +=1
    else:
        st[i] = 1

if st.values() == 1 or st.values() == 3:
    print(st)




