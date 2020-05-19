;To write LISP function for finding factorial of a number with recursion.

(defun fact(n)
	(cond 
		((= n 0) 1)
		(t (* n (fact(decf n 1))))
	)
)
(format t "Enter the number whose factorial you want to find:~%")
(setq n (read))
(setq k (fact n))
(format t "Factorial of ~d is ~d" n k)
