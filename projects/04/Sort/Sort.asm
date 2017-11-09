//R14 - Address
//R15 - Length

	@R15
	D = M

	@i
	M = D - 1

	
	
	@l2
	M = 0
(LOOP)
	//END of loop
	@i
	D = M
	@END
	D ; JEQ
	
	//Inner loop end of
	@R15
	D = M
	@l2
	D = D-M
	@j
	M = D - 1
	
	//Outer pointer
	@R14
	D = M
	@pos
	M = D
	
(INERLOOP)
	@pos
	A = M
	D = M
	A = A + 1
	D = M-D
	@NOSWAP
	D;JLE
	@pos
	A = M
	D = M
	@temp
	M = D
	
	@pos
	A = M
	A = A+1
	D = M;
	@pos
	A = M
	M = D;
	
	@temp
	D = M
	@pos
	A = M
	A = A+1
	M = D
	
(NOSWAP)
	@pos
	M = M + 1
	@j
	M = M - 1
	D = M
	@DI
	D;JEQ
	@INERLOOP
	0;JMP
	
(DI)
	@i
	M = M - 1
	@l2
	M = M + 1
	@LOOP
	0;JMP
	
	
(END)
@END
0;JMP