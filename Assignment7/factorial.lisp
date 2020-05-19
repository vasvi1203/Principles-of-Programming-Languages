;To write LISP function for finding factorial of a number without recursion.

(format t "Enter the number whose factorial you want to find:~%")
(setq n (read))
(setq fact 1)
(cond ((= n 0)
	(format t "Factorial of 0 is 1"))
	( t (loop for x from 1 to n
		do(setq fact (* x fact))
	)
	(format t "Factorial of ~d is ~d" n fact))
)
