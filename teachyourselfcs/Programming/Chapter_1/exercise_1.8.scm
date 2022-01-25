(define (cubert-iter guess x)
  (if (good-enough? guess x)
      guess
      (cubert-iter (improve guess x)
                 x)))

(define (improve guess x)
        (average (/ x (square guess))
                 (* 2 guess)))

(define (average x y)
        (/ (+ x y)
           3))

;Improved good-enough? test
(define (good-enough? guess x)
        (< (abs (- guess (improve guess x)))
           0.00000000001))

(define (square x)
		(* x x))

(define (cubert x)
  (cubert-iter 1.0 x))
