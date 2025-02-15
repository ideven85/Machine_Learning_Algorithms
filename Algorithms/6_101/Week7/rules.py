# Test File for CNF Basics
duane = "duane"
adam = "adam"
jonathan = "jonathan"
sanam = "sanam"
tim = "tim"
vanilla = "vanilla"
pickle = "pickle"
chocolate = "chocolate"


def rule_set1():
    duane = False
    adam = False
    jonathan = False
    saman = False
    tim = True

    pickles = False
    vanilla = True
    chocolate = False
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

    satisified = rule1 and rule2 and rule3 and rule4 and rule5 and rule6
    return satisified


# Example Rule Set 2:
def rule_set2():
    rule1 = [
        [
            ("duane", True),
            ("adam", True),
            ("jonathan", True),
            ("saman", True),
            ("tim", True),
        ]
    ]

    rule2 = [
        [("duane", False), ("adam", False)],
        [("duane", False), ("jonathan", False)],
        [("duane", False), ("saman", False)],
        [("duane", False), ("tim", False)],
        [("adam", False), ("jonathan", False)],
        [("adam", False), ("saman", False)],
        [("adam", False), ("tim", False)],
        [("jonathan", False), ("saman", False)],
        [("jonathan", False), ("tim", False)],
        [("saman", False), ("tim", False)],
    ]

    rule3 = [
        [("chocolate", False), ("vanilla", False), ("pickles", False)],
        [("chocolate", True), ("vanilla", True)],
        [("chocolate", True), ("pickles", True)],
        [("vanilla", True), ("pickles", True)],
    ]

    rule4 = [
        [("duane", False), ("pickles", True)],
        [("duane", False), ("chocolate", False)],
        [("duane", False), ("vanilla", False)],
    ]

    rule5 = [
        [("jonathan", False), ("saman", True)],
        [("saman", False), ("jonathan", True)],
    ]

    rule6 = [
        [("adam", False), ("chocolate", True)],
        [("adam", False), ("vanilla", True)],
        [("adam", False), ("pickles", True)],
    ]

    rules = rule1 + rule2 + rule3 + rule4 + rule5 + rule6


print(rule_set1())
print(rule_set2())
