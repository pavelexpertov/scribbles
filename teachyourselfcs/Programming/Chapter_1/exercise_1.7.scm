(define (sqrt-iter guess x)
  (if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x)
                 x)))

(define (improve guess x)
  (average guess (/ x guess)))

(define (average x y)
  (/ (+ x y) 2))

(define (good-enough? guess x)
  (< (abs (- (square guess) x)) 0.001))

(define (square x)
		(* x x))

(define (sqrt x)
  (sqrt-iter 1.0 x))

(define (multiply-tens n)
		  (if (> n 0)
			  (* 10 (multiply-tens (- n 1)))
              1))

;This is output from performing the square root calculation:
;1 ]=> (sqrt 0.001)

;Value: .04124542607499115

;1 ]=> (sqrt 0.00001)

;Value: .03135649010771716

;1 ]=> (sqrt 0.000000001)

;Value: .03125001065624928

;1 ]=> (sqrt 0.0000000000000001)

;Value: .03125000000000106

;1 ]=> (sqrt 0.00000000000000000000001)

;Value: .03125

;1 ]=> (sqrt 0.0000000000000000000000000001)

;Value: .03125

;1 ]=> (sqrt-iter 0.1 0.001)

;Value: .03659090909090909

;1 ]=> (sqrt-iter 0.1 0.00001)

;Value: .0251249000999001

;1 ]=> (sqrt-iter 0.1 0.000000001)

;Value: .025000012499999

;1 ]=> (sqrt-iter 0.1 0.0000000000000001)

;Value: .02500000000000125

;1 ]=> (sqrt 0.1 0.00000000000000000000001)

;1 ]=> (sqrt-iter 0.1 0.00000000000000000000001)

;Value: .025

;]=> (sqrt-iter 0.1 0.0000000000000000000000000001)

;Value: .025

