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
	)
]
