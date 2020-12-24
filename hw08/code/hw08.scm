
; Problem 1
(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
)

; Problem 2
(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  'YOUR-CODE-HERE
)

; Problem 3
(define (rle s)
  'YOUR-CODE-HERE
)
