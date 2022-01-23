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

(define (sqrt x)
  (sqrt-iter 1.0 x))

(define (multiply-tens n)
		  (if (> n 0)
			  (* 10 (multiply-tens (- n 1)))
              1))

;This is output from performing the square root calculation on a tiny number:
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

Ok, so the exercise said that the good-enough? test is not very
effective at finding square roots of very small numbers.
This is because inside the compound combination, the procedure uses a
number of `0.001` when it calculates a difference between a squared
guess and radicand and the number is limiting that, given enough
guessed iterations, will prevent the procedure from calculating further
due to satisfied condition of comparing between the difference and the number.
For example, for finding square of `0.001`, the function can
produce a plausible square root whereas finding square root for
`0.00001` will show inaccuracy in terms of an incorrect number
of decimal places within the calculated root. This same calculation can
be observed for even tinier numbers than the mentioned one.
As for the big


; This is output for the large numbers

;1 ]=> (sqrt 9999999999999999)

;Value: 100000000.

;1 ]=> (sqrt 99999999999)

;Value: 316227.76601525676

;1 ]=> (sqrt 99999999999999999)


