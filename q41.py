#the authors name is Isa Grace guthrie
def count_hashtag(x):
    index=0
    count=0
    while index<len(x):
        if x[index:index+len("#")]=="#":
            index+=1
            count+=1
        else:
            index+=1
    print(count)
    return -1


string="I am incredible #happy #today hope you have a great #day"
count_hashtag(string)
