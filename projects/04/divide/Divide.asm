// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Divide.asm

// Put your code here.
	@R13
	D = M
	@n
	M = D
	@R14
	D = M
	@R15
	M = 0
	@m
	M = D
	@counter
	M = 1
(LOOP1)
	@n
	D = M
	@m
	D = D - M
	@ENDLOOP2
	D;JEQ
	@ENDLOOP1
	D; JLT
	@m
	M = M<<
	@counter
	M = M<<
	@LOOP1
	0;JMP	
(ENDLOOP1)
	@counter
	M = M>>
	@m
	M = M>>
	@n
	D = M
	@m
	D = D - M
	@n
	M = D
	@R14
	D = M
	@m
	M = D
	
	@counter
	D=M
	@END
	D;JEQ 
	@R15
	M = D + M
	
	@counter
	M = 1
	@LOOP1
	0;JMP
(ENDLOOP2)	
	@counter
	D = M
	@R15
	M = M + D
	
(END)
	@END
	0;JMP
	





	
	
	
	
	