import string
#structural pattern matching / match case

def run(program): #What is good ordering of the code/functions here? below as that is logical, or above as its easy to read
    
    printlist = []
    location = {} #save location name and index
    vars = {char : 0 for char in string.ascii_uppercase} #initialise vars
    i = 0
    eval_program(program, i)
    return printlist

if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 10")
    program1.append("PRINT A")
    program1.append("MOV B A")
    program1.append("PRINT A")
    program1.append("potat:")
    program1.append("PRINT B")
    program1.append("MUL A B")
    #program1.append("JUMP potat")
    program1.append("PRINT A")
    program1.append("END")
    
    result = run(program1)
    print(result)



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
