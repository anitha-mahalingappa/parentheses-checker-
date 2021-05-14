open_para = ["(","[","{"]
close_para = [")","]","}"]
data = []
User_input = input(" please enter your input: ")
for elem in User_input:
    if elem in open_para:
        data.append(elem)
    elif elem in close_para:
        last_data = data.pop()
        if elem == ")" and last_data != "(":
            print ("invalid Para ")
            break
        elif elem == "]" and last_data != "[":
            print ("invalid Para ")
            break
        elif elem == "}" and last_data != "{":
            print ("invalid Para ")
            break
        # else:
        #     data.pop()
else:
    print("valid Para")



    
