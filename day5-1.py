from itertools import product


def parse_op_code(opcode):
    opcode_str = str(opcode)
    if len(opcode_str) == 1:
        return '000'+ opcode_str[0]
    if (len(opcode_str)) == 3:
        return '0' + opcode_str
    if len(opcode_str) == 4:
        return opcode_str
    raise Exception('problem with opcode ' + opcode_str)

def get_value_from_op_code(opcode, input, instruction_pointer, param_number):
    if param_number == 1:
        if opcode[-3] == '0':

            return input[input[instruction_pointer+1]]
        elif opcode[-3] == '1':
            return input[instruction_pointer+1]
        else:
            raise Exception('problem with opcode ' + opcode)
    elif param_number == 2:
        if opcode[-4] == '0':
            return input[input[instruction_pointer+2]]
        elif opcode[-4] == '1':
            return input[instruction_pointer+2]
        else:
            raise Exception('problem with opcode ' + opcode)

def program(input,  input_user):

    should_halt = False
    instruction_pointer = 0 

    while True:
        opcode = input[instruction_pointer]

        if opcode == 99:
            should_halt = True
            break
        
        parsed_op_code = parse_op_code(opcode)
        opcode = int(parsed_op_code[-1])
        if opcode == 1:
            
            input[input[instruction_pointer+3]] = get_value_from_op_code(parsed_op_code, input, instruction_pointer, 1) + get_value_from_op_code(parsed_op_code, input, instruction_pointer, 2)
            instruction_pointer = instruction_pointer + 4
        elif opcode == 2:
            input[input[instruction_pointer+3]] = get_value_from_op_code(parsed_op_code, input, instruction_pointer, 1) * get_value_from_op_code(parsed_op_code, input, instruction_pointer, 2)
            instruction_pointer = instruction_pointer + 4
        elif opcode == 3:
            input[input[instruction_pointer+1]] = input_user
            instruction_pointer = instruction_pointer + 2
        elif opcode == 4:
            print(input[input[instruction_pointer+1]])
            instruction_pointer =instruction_pointer + 2
    return input




input = [3,225,1,225,6,6,1100,1,238,225,104,0,2,136,183,224,101,-5304,224,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1101,72,47,225,1101,59,55,225,1101,46,75,225,1101,49,15,224,101,-64,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,102,9,210,224,1001,224,-270,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,101,14,35,224,101,-86,224,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1102,40,74,224,1001,224,-2960,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1101,10,78,225,1001,39,90,224,1001,224,-149,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1002,217,50,224,1001,224,-1650,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1102,68,8,225,1,43,214,224,1001,224,-126,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1102,88,30,225,1102,18,80,225,1102,33,28,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,677,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1107,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,108,226,226,224,102,2,223,223,1005,224,359,1001,223,1,223,1108,677,226,224,102,2,223,223,1006,224,374,101,1,223,223,108,677,226,224,102,2,223,223,1006,224,389,1001,223,1,223,107,226,226,224,102,2,223,223,1005,224,404,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,419,101,1,223,223,1107,677,677,224,102,2,223,223,1006,224,434,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,449,101,1,223,223,7,677,677,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,494,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,509,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,524,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,539,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,554,101,1,223,223,107,226,677,224,1002,223,2,223,1005,224,569,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,584,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,599,101,1,223,223,1008,677,677,224,102,2,223,223,1005,224,614,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]

input = program(input,1)