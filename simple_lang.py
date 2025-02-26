import string

def run(program): #What is good ordering of the code/functions here? below as that is logical, or above as its easy to read
    #I feel like these need to be accessed and changed globally, but is that good practice?
    #Feels like something is wrong with that, but also seems weird to pass them all through all functions
    global printlist
    printlist = []
    global location
    location = {} #save location name and index
    global vars
    vars = {char : 0 for char in string.ascii_uppercase} #initialise vars
    global i
    i = 0
    build_dic(program) #gotta find locations first

    eval_program(program, i)
    return printlist

def build_dic(program):
    k = 0
    for j in program:
        j = j.split(" ")
        location[j[0][:-1]] = k
        k += 1
    #print(location)

def eval_program(program, i):
    if len(program) == 0: return #printlist #gotta avoid errors if its empty
    while True:
        line = program[i]
        line = line.split(" ")
        match line[0]:
            case "PRINT":
                PRINT(line[1])
            case "MOV":
                MOV(line[1], line[2])
            case "ADD":
                ADD(line[1], line[2])
            case "SUB":
                SUB(line[1], line[2])
            case "MUL":
                MUL(line[1], line[2])
            case "JUMP":
                i = location[line[1]] -1 #doubt if should be function but needs pogram
            case "IF":
                if IF(line[1], line[2], line[3]):
                    i = location[line[5]] -1
            case "END":
                return #printlist
            case _: #catch all for the locations
                location[line[0][:-1]] = i # also here doesnt seem logical to use another function?
        i += 1
        if i >= len(program): return #printlist #avoid errors if there is no end statement
    
def PRINT(a):
    if a in vars:
        printlist.append(vars[a])
    else:
        printlist.append(int(a))
    

def MOV(a,b):
    if b in vars:
        vars[a] = vars[b]
    else:
        vars[a] = int(b)

def ADD(a,b):
    if b in vars:
        vars[a] += vars[b]
    else:
        vars[a] += int(b)

def SUB(a,b):
    if b in vars:
        vars[a] -= vars[b]
    else:
        vars[a] -= int(b)

def MUL(a,b):
    if b in vars:
        vars[a] *= vars[b]
    else:
        vars[a] *= int(b)

def IF(val1, op, val2): #feels like this might be doable directly with like int(val1)opint(val2) but couldnt do it
    if val1 in vars:
        val1 = vars[val1]
    if val2 in vars:
        val2 = vars[val2]
    
    match op:
        case "==":
            return int(val1) == int(val2)
        case ">=":
            return int(val1) >= int(val2)
        case "<=":
            return int(val1) <= int(val2)
        case "<":
            return int(val1) < int(val2)
        case ">":
            return int(val1) > int(val2)
        case "!=":
            return int(val1) != int(val2)

if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 999")
    program1.append("start:")
    program1.append("ADD A 1")
    program1.append("SUB B 1")
    program1.append("ADD C 1")
    program1.append("IF A == B JUMP end")
    program1.append("JUMP start")
    program1.append("end:")
    program1.append("PRINT C")
    
    result = run(program1)
    print(result)

    """
    while True:
        line = program[i]
        line = line.split(" ")
        if line[0] == "MOV":
            if line[2] in variables:
                variables[line[1]] = variables[line[2]]
            else:
                variables[line[1]] = int(line[2])
        elif line[0] == "PRINT":
            printlist.append(variables[line[1]])
        elif line[0] == "ADD":
            if line[2] in variables:
                variables[line[1]] += variables[line[2]]
            else:
                variables[line[1]] += int(line[2])
        elif line[0] == "SUB":
            if line[2] in variables:
                variables[line[1]] -= variables[line[2]]
            else:
                variables[line[1]] -= int(line[2])
        elif line[0] == "MUL":
            if line[2] in variables:
                variables[line[1]] *= variables[line[2]]
            else:
                variables[line[1]] *= int(line[2])
        #elif line[0] == "JUMP":
            #print(location[line[1]])
        #    i = location[line[1]]-1
        elif line[0] == "END":
            break
        else: #if it is nothing of these it is a location name
            location[line[0][:-1]] = i

        i += 1
    print(location)
    return printlist
    """
