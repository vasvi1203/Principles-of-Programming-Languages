;To write LISP function for getting nth element from a list.

(format t "Enter the list with parenthesis:~%")
(setq l (read))
(format t "The list is ~s~%" l)
(format t "Enter n:~%")
(setq n (read))
(setq k (nth n l))
(format t "The nth element is ~s" k)
