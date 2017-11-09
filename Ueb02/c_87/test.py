#!/usr/bin/env python
# Device Under Test
DUT = "./ueb02"
# Test definitions

suite = [	
	#Invalid program calls
	Test(
		name = "Invalid Call (Unknown Argument)#1",
		description = "Invalid program call",
		command = "$DUT hallo",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
    Test(
		name = "Invalid Call (Unknown Argument)#2",
		description = "Invalid program call",
		command = "$DUT 1Hallo",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
    Test(
		name = "Invalid Call (Filter missing arg)#1",
		description = "Invalid program call",
		command = "$DUT +l -p",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
    Test(
		name = "Invalid Call (Unknown Filter)#1",
		description = "Invalid program call",
		command = "$DUT 1 +h -p",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
    Test(
		name = "Invalid Call (Unknown Filter)#2",
		description = "Invalid program call",
		command = "$DUT 1 +lp -p",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
    Test(
		name = "Invalid Call (Unknown Operation)#1",
		description = "Invalid program call",
		command = "$DUT 1 +l -pb",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
    Test(
		name = "Invalid Call (Unknown Operation)#2",
		description = "Invalid program call",
		command = "$DUT 1 +l -f",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Filter (LessEqual -> empty)",
		description = "Invalid Filter",
		command = "$DUT 1 2 3 +l 0 -p",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = 0
	),
	Test(
		name = "Invalid Filter (GreaterEqual -> empty)",
		description = "Invalid Filter",
		command = "$DUT 1 2 3 +u 4 -p",
		stderr = lambda x: len(x) > 0 and x.find('ERROR') >= 0,
		returnCode = 0
	),
	#Valid Operations
	Test(
		name = "Valid Operation (Print)#1",
		description = "Valid Operation",
		command = "$DUT 1 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 1 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Print)#2",
		description = "Valid Operation",
		command = "$DUT 1 3 2 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 1 3 2 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Printasc)#1",
		description = "Valid Operation",
		command = "$DUT 1 3 2 -a",
		stdout = lambda x: len(x) > 0 and x.find('[ 1 2 3 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Printasc)#2",
		description = "Valid Operation",
		command = "$DUT 1 -2 -3 3 2 -a",
		stdout = lambda x: len(x) > 0 and x.find('[ -3 -2 1 2 3 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (length)",
		description = "Valid Operation",
		command = "$DUT 1 -2 -3 3 2 -l",
		stdout = lambda x: len(x) > 0 and x.find('Length: 5') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Min)#1",
		description = "Valid Operation",
		command = "$DUT 1 -2 -3 3 2 -m",
		stdout = lambda x: len(x) > 0 and x.find('Minimum: -3') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Min)#2",
		description = "Valid Operation",
		command = "$DUT 1 2 3 -m",
		stdout = lambda x: len(x) > 0 and x.find('Minimum: 1') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Max)#1",
		description = "Valid Operation",
		command = "$DUT 1 -2 -3 3 2 -M",
		stdout = lambda x: len(x) > 0 and x.find('Maximum: 3') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Max)#2",
		description = "Valid Operation",
		command = "$DUT 1 2 3 4 5 -M",
		stdout = lambda x: len(x) > 0 and x.find('Maximum: 5') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Sum)#1",
		description = "Valid Operation",
		command = "$DUT 1 -2 -3 3 2 -s",
		stdout = lambda x: len(x) > 0 and x.find('Sum: 0') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Sum)#2",
		description = "Valid Operation",
		command = "$DUT 1 2 3 4 5 -s",
		stdout = lambda x: len(x) > 0 and x.find('Sum: 15') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Product)#1",
		description = "Valid Operation",
		command = "$DUT 1 2 3 4 -P",
		stdout = lambda x: len(x) > 0 and x.find('Product: 24') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Product)#2",
		description = "Valid Operation",
		command = "$DUT 1 -2 -3 3 2 -P",
		stdout = lambda x: len(x) > 0 and x.find('Product: -36') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Span)",
		description = "Valid Operation",
		command = "$DUT 1 -2 -3 3 2 -S",
		stdout = lambda x: len(x) > 0 and x.find('Span: 6') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Monoton)#1",
		description = "Valid Operation",
		command = "$DUT 1 -2 -3 3 2 -l",
		stdout = lambda x: len(x) > 0 and x.find('Strictly monotonically: no') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Monoton)#2",
		description = "Valid Operation",
		command = "$DUT 1 2 3 -c",
		stdout = lambda x: len(x) > 0 and x.find('Strictly monotonically: yes') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Monoton)#3",
		description = "Valid Operation",
		command = "$DUT 1 2 2 3 -c",
		stdout = lambda x: len(x) > 0 and x.find('Strictly monotonically: no') >= 0,
		returnCode = 0
	),
	#Valid Filters
	Test(
		name = "Valid Filter (LessEqual)#1",
		description = "Valid Filter",
		command = "$DUT 1 2 3 +l 4 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 1 2 3 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Filter (LessEqual)#2",
		description = "Valid Filter",
		command = "$DUT 1 2 3 +l 2 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 1 2 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Filter (GreaterEqual)#1",
		description = "Valid Filter",
		command = "$DUT 1 2 3 +u 0 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 1 2 3 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Filter (GreaterEqual)#2",
		description = "Valid Filter",
		command = "$DUT 1 2 3 +u 2 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 2 3 ]') >= 0,
		returnCode = 0
	)
]
