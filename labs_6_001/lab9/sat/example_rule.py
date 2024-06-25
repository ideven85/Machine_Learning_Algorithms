"""
The suspects are Adam, Duane, Jonathan, Saman, and Tim the Beaver.
Whichever suspect ate any of the cupcakes must have eaten all of them.
The cupcakes included exactly two of the flavors chocolate, vanilla, and pickles.
Duane only eats pickles-flavored cupcakes.
Years ago, Jonathan and Saman made a pact that, whenever either of them eats cupcakes, they must share with the other one.
Adam feels strongly about flavor fairness and will only eat cupcakes if he can include at least 3 different flavors.
"""

duane = "Duane"
adam = "Adam"
jonathan = "Jonathan"
saman = "Saman"
tim = "Tim"
chocolate = "Chocolate"
vanilla = "Vanilla"
pickles = "Pickles"
rule1 = duane or adam or jonathan or saman or tim
# At least one of them must have committed the crime!  Here, one of these
# variables being True represents that person having committed the crime.


rule2 = (
    (not duane or not adam)
    and (not duane or not jonathan)
    and (not duane or not saman)
    and (not duane or not tim)
    and (not adam or not jonathan)
    and (not adam or not saman)
    and (not adam or not tim)
    and (not jonathan or not saman)
    and (not jonathan or not tim)
    and (not saman or not tim)
)
# At most one of the suspects is guilty.  In other words, for any pair of
# suspects, at least one must be NOT guilty (so that we cannot possibly find
# two or more people guilty).

# Together, rule2 and rule1 guarantee that exactly one suspect is guilty.


rule3 = (
    (not chocolate or not vanilla or not pickles)
    and (chocolate or vanilla)
    and (chocolate or pickles)
    and (vanilla or pickles)
)
# Here is our rule that the cupcakes included exactly two of the flavors.  Put
# another way: we can't have all flavors present; and, additionally, among
# any pair of flavors, at least one was present.


rule4 = (
    (not duane or pickles)
    and (not duane or not chocolate)
    and (not duane or not vanilla)
)
# If Duane is guilty, this will evaluate to True only if only pickles-flavored
# cupcakes were present.  If Duane is not guilty, this will always evaluate to
# True.  This is our way of encoding the fact that, if Duane is guilty, only
# pickles-flavored cupcakes must have been present.


rule5 = (not jonathan or saman) and (not saman or jonathan)
# If Jonathan ate cupcakes without sharing with Saman, the first case will fail
# to hold.  Likewise for Saman eating without sharing.  Since Jonathan and Saman
# only eat cupcakes together, this rule excludes the possibility that only one
# of them ate cupcakes.


rule6 = (not adam or chocolate) and (not adam or vanilla) and (not adam or pickles)
# If Adam is the culprit and we left out a flavor, the corresponding case here
# will fail to hold.  So this rule encodes the restriction that Adam can only
# be guilty if all three types of cupcakes are present.


satisfied = rule1 and rule2 and rule3 and rule4 and rule5 and rule6
print(rule5)
print(satisfied)
