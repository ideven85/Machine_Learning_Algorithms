**Answer booklet**  
  
This document accompanies the book [Understanding Deep Learning](http://www.udlbook.com/). It contains answers to a selected subset of the problems at the end of each chapter of the main book. The remaining answers are available only to instructors via the MIT Press.  
This booklet has not yet been checked very carefully. I really need your help in this regard and I’d be very grateful if you would mail me at [udlbookmail@gmail.com](mailto:udlbookmail@gmail.com) if you cannot understand the text or if you think that you find a mistake. Suggestions for extra problems will also be gratefully received!  
  
  
Simon Prince February 8, 2026  
  
**Problem 2.3 **Consider reformulating linear regression as a generative model so we have *x *= g[*y, **ϕ***] = *ϕ′ +ϕ′ y*. What is the new loss function? Find an expression for the inverse function *y =*  
*0	1*  
*g*−1[*x, **ϕ**′*] that we would use to perform inference. Will this model make the same predictions as the discriminative version for a given training dataset *{xi, yi}*? One way to establish this is to write code that fits a line  
g−1[*x, **ϕ**′*]  
