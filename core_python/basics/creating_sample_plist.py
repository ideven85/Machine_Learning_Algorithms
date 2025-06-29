import datetime
import plistlib

pl = dict(
    aDict=dict(
        anotherString="<hello & hi there!>",
        aThirdString=b"M\xe4ssig, Ma\xdf",
        aTrueValue=True,
        aFalseValue=False,
    ),
    someData=b"<binary gunk>",
    someMoreData=b"<lots of binary gunk>" * 10,
    aDate=datetime.datetime.now(),
)
with open("x.plist", "w") as f:
    f.write(plistlib.dumps(pl).decode())
