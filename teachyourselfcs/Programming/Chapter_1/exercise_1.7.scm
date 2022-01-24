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

;Improved good-enough? test
(define (good-enough? guess x)
        (< (abs (- guess (improve guess x)))
           0.00000001))

(define (square x)
		(* x x))

(define (sqrt x)
  (sqrt-iter 1.0 x))

(define (multiply-tens n)
		  (if (> n 0)
			  (* 10 (multiply-tens (- n 1)))
              1))

(define (multiply-tenth n)
        (if (> n 0)
            (* 0.1 (multiply-tenth (- n 1)))
            1))


;Ok, so the exercise said that the good-enough? test is not very
;effective at finding square roots of very small numbers.
;This is because inside the compound combination, the procedure uses a
;number of `0.001` when it calculates a difference between a squared
;guess and radicand and the number is limiting that, given enough
;guessed iterations, will prevent the procedure from calculating further
;due to satisfied condition of comparing between the difference and the number.

; Look at the examples below:
;-----------------------------------
;1 ]=> (sqrt (multiply-tenth 6))

;Value: 3.1260655525445276e-2

;1 ]=> (sqrt (multiply-tenth 7))

;Value: .03125106561775382

;1 ]=> (sqrt (multiply-tenth 8))

;Value: .03125010656242753
;-----------------------------------
;It can be observed that the change in decimal value (100 thousandth place)
;doesn't change because it procedure's condition will be satisfied
;(i.e. 0.03125010656242753^2 - 0.000000001 < 0.001).
;However, the calculator will show that:
;square root of 0.00000001 will be 0.0001 and square root of 0.000000001
;will be 0.000031623. The decimal value is not wrong but it's the decimal
;places that the good-enough? test couldn't 


;As for very large numbers, the good-enough? test will not suffice because
;when calculating differences between squared guess and the radicand, the
;condition that tests for closeness of both numbers doesn't get satisfied
;because the differences are very big.
;If you look below, 
;-----------------------------------------
;1 ]=> (sqrt (multiply-tens 11))

;Value: 316227.7660168379

;1 ]=> (sqrt (multiply-tens 12))

;Value: 1000000.

;1 ]=> (sqrt (multiply-tens 13))
;-----------------------------------------
;It can be observed that there's a limit of calcuating the square roots
;becuase when a number contains 13 zeros, the procedure struggles to
;calculate it by being stuck in an endless loop. This is caused not
;satisfying the aformentioned condition.
;For example, actual square root value is 3162277.660168379.
;If we give it to the good-enough? test, you get the following:
;----------------------------------------------------------------
;1 ]=> (good-enough? 3162277.660168379 (multiply-tens 13))

;Value: #f

;1 ]=> (good-enough? 1000000 (multiply-tens 12))

;Value: #t
;----------------------------------------------------------------

; Output for testing large numbers

;1 ]=> (sqrt (multiply-tens 8))

;Value: 10000.

;1 ]=> (sqrt (multiply-tens 9))

;Value: 31622.776601684047

;1 ]=> (sqrt (multiply-tens 10))

;Value: 100000.

;1 ]=> (sqrt (multiply-tens 11))

;Value: 316227.7660168379

;1 ]=> (sqrt (multiply-tens 12))

;Value: 1000000.

;1 ]=> (sqrt (multiply-tens 13))



; Output for testing small numbers

;1 ]=> (sqrt (multiply-tenth 1))

;Value: .316245562280389

;1 ]=> (sqrt (multiply-tenth 2))

;Value: .10032578510960607

;1 ]=> (sqrt (multiply-tenth 3))

;Value: .04124542607499115

;1 ]=> (sqrt (multiply-tenth 4))

;Value: .03230844833048122

;1 ]=> (sqrt (multiply-tenth 5))

;Value: .03135649010771716

;1 ]=> (sqrt (multiply-tenth 6))

;Value: 3.1260655525445276e-2

;1 ]=> (sqrt (multiply-tenth 7))

;Value: .03125106561775382

;1 ]=> (sqrt (multiply-tenth 8))

;Value: .03125010656242753

;1 ]=> (sqrt (multiply-tenth 9))

;Value: .03125001065624928

;1 ]=> (sqrt (multiply-tenth 10))

;Value: .03125000106562499


