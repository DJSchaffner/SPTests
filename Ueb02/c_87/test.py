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
		stderr = lambda x: len(x) > 0 and x.find('ERROR: Unknown argument!') >= 0,
		returnCode = lambda v: v != 0
	),
    Test(
		name = "Invalid Call (Unknown Argument)#2",
		description = "Invalid program call",
		command = "$DUT 1Hallo",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: Unknown argument!') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Call (Unknown Argument)#3",
		description = "Invalid program call",
		command = "$DUT 1 2 3 4-p",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: Unknown argument!') >= 0,
		returnCode = lambda v: v != 0
	),
    Test(
		name = "Invalid Call (Filter missing arg)#1",
		description = "Invalid program call",
		command = "$DUT +l -p",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: Filter is missing its argument!') >= 0,
		returnCode = lambda v: v != 0
	),
    Test(
		name = "Invalid Call (Unknown Filter)#1",
		description = "Invalid program call",
		command = "$DUT 1 +h -p",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: Unknown argument!') >= 0,
		returnCode = lambda v: v != 0
	),
    Test(
		name = "Invalid Call (Unknown Filter)#2",
		description = "Invalid program call",
		command = "$DUT 1 +lp -p",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: Unknown argument!') >= 0,
		returnCode = lambda v: v != 0
	),
    Test(
		name = "Invalid Call (Unknown Operation)#1",
		description = "Invalid program call",
		command = "$DUT 1 +l 1 -pb",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: Unknown argument!') >= 0,
		returnCode = lambda v: v != 0
	),
    Test(
		name = "Invalid Call (Unknown Operation)#2",
		description = "Invalid program call",
		command = "$DUT 1 +l 1 -f",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: Unknown argument!') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Call (Array Full)#1",
		description = "Invalid program call",
		command = "$DUT 1 2 3 4 5 6 7 8 9 10 11 -p",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: Array full!') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Call (Array Full)#2",
		description = "Invalid program call",
		command = "$DUT 1 2 3 4 5 6 7 8 9 10 11 12 13 14 -p",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: Array full!') >= 0,
		returnCode = lambda v: v != 0
	),
	#Invalid operations empty array
	Test(
		name = "Invalid Operation (Min -> empty)",
		description = "Valid Operation",
		command = "$DUT -m",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: No values given!') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Operation (Max -> empty)",
		description = "Valid Operation",
		command = "$DUT -M",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: No values given!') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Operation (Sum -> empty)",
		description = "Valid Operation",
		command = "$DUT -s",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: No values given!') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Operation (Product -> empty)",
		description = "Valid Operation",
		command = "$DUT -P",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: No values given!') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Operation (Span -> empty)",
		description = "Invalid Operation",
		command = "$DUT -S",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: No values given!') >= 0,
		returnCode = lambda v: v != 0
	),
	Test(
		name = "Invalid Operation (Monotonicity -> empty)",
		description = "Invalid Operation",
		command = "$DUT -c",
		stderr = lambda x: len(x) > 0 and x.find('ERROR: No values given!') >= 0,
		returnCode = lambda v: v != 0
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
		name = "Valid Operation (Print)#3",
		description = "Valid Operation",
		command = "$DUT -p",
		stdout = lambda x: len(x) > 0 and x.find('[ ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Print)#4",
		description = "Valid Operation",
		command = "$DUT 024 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 20 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Print)#5",
		description = "Valid Operation",
		command = "$DUT 0x14 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 20 ]') >= 0,
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
		name = "Valid Operation (Printasc)#3",
		description = "Valid Operation",
		command = "$DUT -a",
		stdout = lambda x: len(x) > 0 and x.find('[ ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Length)#1",
		description = "Valid Operation",
		command = "$DUT 1 -2 -3 3 2 -l",
		stdout = lambda x: len(x) > 0 and x.find('Length: 5') >= 0,
		returnCode = 0
	),
	Test(
		name = "Invalid Operation (Length)#2",
		description = "Valid Operation",
		command = "$DUT -l",
		stdout = lambda x: len(x) > 0 and x.find('Length: 0') >= 0,
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
		stdout = lambda x: len(x) > 0 and x.find('Sum: 1') >= 0,
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
		stdout = lambda x: len(x) > 0 and x.find('Product: 36') >= 0,
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
		command = "$DUT 1 -2 -3 3 2 -c",
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
	Test(
		name = "Valid Operation (Monoton)#4",
		description = "Valid Operation",
		command = "$DUT 3 2 1 -c",
		stdout = lambda x: len(x) > 0 and x.find('Strictly monotonically: yes') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Operation (Multiline)",
		description = "Valid Operation",
		command = "$DUT 3 2 1 -a -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 1 2 3 ]\n[ 3 2 1 ]') >= 0,
		returnCode = 0
	),
	#Valid Filters
	Test(
		name = "Valid Filter (LessEqual)#1",
		description = "Valid Filter",
		command = "$DUT 1 2 3 +u 4 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 1 2 3 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Filter (LessEqual)#2",
		description = "Valid Filter",
		command = "$DUT 1 2 3 +u 2 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 1 2 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Filter (LessEqual)#3",
		description = "Valid Filter",
		command = "$DUT 1 100 144 +u 0144 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 1 100 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Filter (LessEqual)#4",
		description = "Valid Filter",
		command = "$DUT 1 19 33 +u 0x14 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 1 19 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Filter (GreaterEqual)#1",
		description = "Valid Filter",
		command = "$DUT 1 2 3 +l 0 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 1 2 3 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Filter (GreaterEqual)#2",
		description = "Valid Filter",
		command = "$DUT 1 2 3 +l 2 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 2 3 ]') >= 0,
		returnCode = 0
	),
	#Multiple Filters 
	Test(
		name = "Valid Multiple Filters (ul)",
		description = "Valid Filter",
		command = "$DUT 1 2 3 +l 2 +u 2 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 2 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Multiple Filters (2x l)",
		description = "Valid Filter",
		command = "$DUT 1 2 3 +l 2 +l 2 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 2 3 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Multiple Filters (2x u)",
		description = "Valid Filter",
		command = "$DUT 1 2 3 +u 2 +u 2 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 1 2 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Multiple Filters (2x u)",
		description = "Valid Filter",
		command = "$DUT 3 5 7 8 +u 7 +l 4 -p +l 3 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 5 7 ]\n[ 3 5 7 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Multiple Filters (empty -> then not)#1",
		description = "Valid Filter",
		command = "$DUT 3 5 7 8 +u 2 +u 5 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 3 5 ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Multiple Filters (empty -> then not)21",
		description = "Valid Filter",
		command = "$DUT 3 5 7 8 +u 5 +l 3 +u 3 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ 3 ]') >= 0,
		returnCode = 0
	),
	#Valid filter empty array 
	Test(
		name = "Valid Call (Array Empty)",
		description = "Valid program call",
		command = "$DUT +l 4 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Multiple Filters (ul -> empty)",
		description = "Valid Filter",
		command = "$DUT 1 2 3 +l 2 +u 1 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Invalid Filter (LessEqual -> empty)",
		description = "Invalid Filter",
		command = "$DUT 1 2 3 +u 0 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ ]') >= 0,
		returnCode = 0
	),
	Test(
		name = "Valid Filter (GreaterEqual -> empty)",
		description = "Invalid Filter",
		command = "$DUT 1 2 3 +l 4 -p",
		stdout = lambda x: len(x) > 0 and x.find('[ ]') >= 0,
		returnCode = 0
	)
]
