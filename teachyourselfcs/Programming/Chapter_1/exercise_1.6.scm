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

(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
          (else else-clause)))

(define (sqrt-iter guess x)
  (new-if (good-enough? guess x)
            guess
			(sqrt-iter (improve guess x)
		               x)))
;Ok, the answer for the exercise is (sqrt-iter (improve guess x) x) will get evaluated
;*endlessly* by calling sqrt-iter procedure (endlessly).
; I don't get why I don't get maximum recursion error when it spits 23 is not an applicable object.
; Update: just reinstalled my OS on my desktop and now I get the specific error.
; Still don't get it how I didn't get the recursion error in the first place
