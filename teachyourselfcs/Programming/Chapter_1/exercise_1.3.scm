(define (square x) (* x x))
(define (sum-of-squares x y) (+ (square x) (square y)))
(define (max x y) (if (> x y) x y))
(define (>= x y) (not (< x y)))
(define (<= x y) (not (> x y)))

(define (main-procedure x y z) (cond ((and (>= x z) (>= y z)) (sum-of-squares x y))
                                     ((and (<= x z) (<= x y)) (sum-of-squares y z))
                                     ((and (>= x y) (<= y z)) (sum-of-squares x z))))

;(define (main-procedure x y z) (sum-of-squares (max x y) (max y z)))
;(define (main-procedure x y z) (cond ((not (= (max x y) (max y z))) (sum-of-squares (max x y) (max y z)))
                                     ;(else (sum-of-squares y (max x z)))))
;(define (main-procedure x y z) (cond ((and (> x z) (> y z)) (sum-of-squares x y))
                                     ;((and (< x z) (< x y)) (sum-of-squares y z))
                                     ;((and (> x y) (< y z)) (sum-of-squares x z))))


