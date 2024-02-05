"""while with counter"""

import random
import string 

ret: str = ""
counter: int = 0
while counter < 9:
    if counter % 3 == 0:
        ret += "" + str(random.choice(string.ascii_uppercase + string.ascii_lowercase)) + str(random.randint(0, 9))
    elif counter % 2 == 0:
        ret += "" + str(random.choice(string.ascii_uppercase + string.ascii_lowercase))
    else:
        ret += "" + str(random.randint(0, 9))
    counter += 1

print(ret)