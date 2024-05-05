(begin
  (define x 0)
  (define out (list ))
  (define outer (lambda () (begin
      (define x 1)
      (define inner (lambda () (begin
          (define x 2)
          (display x) ; inner
      )))
      (inner)
      (display x); outer
  )))
  (outer)
  (display x); global
)

