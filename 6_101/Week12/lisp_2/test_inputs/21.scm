(define (call x) (x))
(call (lambda () 2))
(define (spam) (call (lambda () 2)))
(call spam)
(call call)
(call)