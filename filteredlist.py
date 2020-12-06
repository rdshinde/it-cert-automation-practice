l = [1,2,'aasf','1','123',123]
def filter_list(l):
    return [i for i in l if not isinstance(i, str)]
print(filter_list(l))
