class Computer:
    def __init__(self, A, B, C):
        self.registers = {'A': A, 'B': B, 'C': C}
        self.instruction_pointer = 0
        self.output = []

    def get_operand_value(self, operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return self.registers['A']
        elif operand == 5:
            return self.registers['B']
        elif operand == 6:
            return self.registers['C']
        else:
            raise ValueError("Invalid combo operand")

    def adv(self, operand):
        value = self.get_operand_value(operand)
        self.registers['A'] //= 2 ** value

    def bxl(self, operand):
        self.registers['B'] ^= operand

    def bst(self, operand):
        value = self.get_operand_value(operand)
        self.registers['B'] = value % 8

    def jnz(self, operand):
        if self.registers['A'] != 0:
            self.instruction_pointer = operand
        else:
            self.instruction_pointer += 2

    def bxc(self, operand):
        self.registers['B'] ^= self.registers['C']

    def out(self, operand):
        value = self.get_operand_value(operand)
        self.output.append(value % 8)

    def bdv(self, operand):
        value = self.get_operand_value(operand)
        self.registers['B'] = self.registers['A'] // (2 ** value)

    def cdv(self, operand):
        value = self.get_operand_value(operand)
        self.registers['C'] = self.registers['A'] // (2 ** value)

    def execute_instruction(self, opcode, operand):
        if opcode == 0:
            self.adv(operand)
        elif opcode == 1:
            self.bxl(operand)
        elif opcode == 2:
            self.bst(operand)
        elif opcode == 3:
            self.jnz(operand)
        elif opcode == 4:
            self.bxc(operand)
        elif opcode == 5:
            self.out(operand)
        elif opcode == 6:
            self.bdv(operand)
        elif opcode == 7:
            self.cdv(operand)
        else:
            raise ValueError("Unknown opcode")

    def run(self, program):
        self.output = []
        
        while self.instruction_pointer < len(program):
            opcode, operand = program[self.instruction_pointer], program[self.instruction_pointer + 1]
            self.execute_instruction(opcode, operand)

            if opcode != 3:
                self.instruction_pointer += 2

input_text = open('input.txt').read()

lines = input_text.strip().split('\n')
registers = {}

for line in lines[:3]:
    parts = line.split(': ')
    registers[parts[0].split()[1]] = int(parts[1])

program = list(map(int, lines[4].split(': ')[1].split(',')))
output = []


# Find last digits of the output with small A
# A = 0

# print("Program", program)

# for l in range(1, 8):
#     while program != output:
#         cpu = Computer(A, registers['B'], registers['C'])
#         cpu.run(program)
#         output = cpu.output
#         A += 1
#         print(len(program), program, len(output), output, A)

#     if program[-l:] == output:
#         print("Truncated program", program[-l:], output)
#         print("Found", A)
#         break

# A = int(6443664 * (8 ** 8)) # First saw a pattern in the last digits from previous code


# while program != output:
#     cpu = Computer(A, registers['B'], registers['C'])
#     cpu.run(program)
#     output = cpu.output
#     A += 10000
#     print(len(program), program, len(output), output, A)

#     if program[-6:] == output[-6:]:
#         print("Truncated program", program[-6:], output[-6:])
#         print("Found", A)
#         break

# # The previous code found a good start for the search, now fine tune it:
# A = 108107548079424

# while program != output:
#     cpu = Computer(A, registers['B'], registers['C'])
#     cpu.run(program)
#     output = cpu.output
#     A += 100
#     print(len(program), program, len(output), output, A)

#     if program[-10:] == output[-10:]:
#         print("Truncated program", program[-10:], output[-10:])
#         print("Found", A)
#         break

# Final search
A = 108107565891724

while program != output:
    A += 1
    cpu = Computer(A, registers['B'], registers['C'])
    cpu.run(program)
    output = cpu.output

print(A)