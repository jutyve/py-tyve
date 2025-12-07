name =  input("File name:")
extension = ".jut"



def main(line):
    if "let" in line:
        parts = line.split()
        variables[parts[1]]= parts[-1]
    elif "return" in line:
        imp = line[7::]
        changes = list(variables.keys())
        for i in changes:
            imp = imp.replace(i,variables[i])
        print(eval(imp))



if extension not in name:
    name += extension


variables = {}
with open(name, 'r') as file_object:
    content = file_object.read()
    content = content.split("\n")

    for i in content :
        if i:
            main(i)




