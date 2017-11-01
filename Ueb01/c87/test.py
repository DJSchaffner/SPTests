#!/usr/bin/env python
# Device Under Test
DUT = "./ueb01"
# Test definitions

suite = [	
	#Invalid program calls
	Test(
		name = "Invalid Call (Negative Number)#1",
		description = "Invalid program call",
		command = "$DUT \-1 \+ 2",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Call (Negative Number)#2",
		description = "Invalid program call",
		command = "$DUT 2 \+ \-1",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Call (Too few Args) #1",
		description = "Invalid program call",
		command = "$DUT 1",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Call (Too few Args) #2",
		description = "Invalid program call",
		command = "$DUT 1 \+  ",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Call (Too many Args)#1",
		description = "Invalid program call",
		command = "$DUT 1 \+  1 \+  1",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Call (Too many Args)#2",
		description = "Invalid program call",
		command = "$DUT 1 \+  1 hallo",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Call (Wrong Args)#1",
		description = "Invalid program call",
		command = "$DUT hallo",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Call (Wrong Args)#2",
		description = "Invalid program call",
		command = "$DUT 1 \& 2",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Call (Wrong Args)#3",
		description = "Invalid program call",
		command = "$DUT A \+ 2",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Call (Floats)",
		description = "Invalid program call",
		command = "$DUT 4.0 \+ 2.3",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
	#Addition Tests
	Test(
		name = "Valid Addition",
		description = "Addition with valid params",
		command = "$DUT 1 \+ 1",
		stdout = lambda x: len(x) > 0 and x.find('2') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Addition (Zero)",
		description = "Addition with valid params",
		command = "$DUT 1 \+  0",
		stdout = lambda x: len(x) > 0 and x.find('1') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Addition (Result Zero)",
		description = "Addition with valid params",
		command = "$DUT 0 \+  0",
		stdout = lambda x: len(x) > 0 and x.find('0') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Addition (Octal)#1",
		description = "Addition with valid params",
		command = "$DUT 02 \+  02",
		stdout = lambda x: len(x) > 0 and x.find('4') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Addition (Octal)#2",
		description = "Addition with valid params",
		command = "$DUT 012 \+  012",
		stdout = lambda x: len(x) > 0 and x.find('20') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Addition (Hex)#1",
		description = "Addition with valid params",
		command = "$DUT 0x2 \+  0x2",
		stdout = lambda x: len(x) > 0 and x.find('4') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Addition (Hex)#2",
		description = "Addition with valid params",
		command = "$DUT 0xF \+  0xF",
		stdout = lambda x: len(x) > 0 and x.find('30') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Addition (Partial Hex)",
		description = "Addition with valid params",
		command = "$DUT 0x34 \+  3",
		stdout = lambda x: len(x) > 0 and x.find('55') >= 0,
		returnCode = 0
	),
	#Subtraction Tests
	Test(
		name = "Valid Subtraction",
		description = "Subtraction with valid params",
		command = "$DUT 2 \- 1",
		stdout = lambda x: len(x) > 0 and x.find('1') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Subtraction (Zero)",
		description = "Subtraction with valid params",
		command = "$DUT 1 \- 0",
		stdout = lambda x: len(x) > 0 and x.find('1') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Subtraction (Result Zero)",
		description = "Subtraction with valid params",
		command = "$DUT 0 \- 0",
		stdout = lambda x: len(x) > 0 and x.find('0') >= 0,
		returnCode = 0
	),
	#Multiplication Tests
	Test(
		name = "Valid Multiplication",
		description = "Multiplication with valid params",
		command = "$DUT 2 \* 2",
		stdout = lambda x: len(x) > 0 and x.find('4') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Multiplication (Zero)",
		description = "Multiplication with valid params",
		command = "$DUT 3 \* 0",
		stdout = lambda x: len(x) > 0 and x.find('0') >= 0,
		returnCode = 0
	),
	#Division Tests
	Test(
		name = "Valid Division",
		description = "Division with valid params",
		command = "$DUT 3 \/ 1",
		stdout = lambda x: len(x) > 0 and x.find('3') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Division (Zero)",
		description = "Division with valid params",
		command = "$DUT 0 \/ 3",
		stdout = lambda x: len(x) > 0 and x.find('0') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Division (Rounded)#1", #NOT SURE WHAT SHOULD HAPPEN (round up/down?)
		description = "Division with valid params",
		command = "$DUT 3 \/ 2",
		stdout = lambda x: len(x) > 0 and x.find('1') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Division (Rounded)#2",
		description = "Division with valid params",
		command = "$DUT 7 \/ 2",
		stdout = lambda x: len(x) > 0 and x.find('3') >= 0,
		returnCode = 0
	),
	Test(
		name = "Invalid Division (Zero)",
		description = "Division with invalid params",
		command = "$DUT 3 \/ 0",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
	#Modulo Tests
	Test(
		name = "Valid Modulo",
		description = "Modulo with valid params",
		command = "$DUT 3 \% 2",
		stdout = lambda x: len(x) > 0 and x.find('1') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Modulo (Zero)",
		description = "Modulo with valid params",
		command = "$DUT 0 \% 2",
		stdout = lambda x: len(x) > 0 and x.find('0') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Modulo (Result Zero)",
		description = "Modulo with valid params",
		command = "$DUT 3 \% 1",
		stdout = lambda x: len(x) > 0 and x.find('0') >= 0,
		returnCode = 0
	),
	Test(
		name = "Invalid Modulo (Zero)",
		description = "Modulo with invalid params",
		command = "$DUT 2 \% 0",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	)
]
