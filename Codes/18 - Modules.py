# This code is connected with 'converters.py'.

# You have to write 'Codes.' as this file is in the 'Codes' directory.
import Codes.converters

# Ignore this right now.
from Codes.converters import lbs_t_kgs

print(Codes.converters.kgs_to_lbs(10))

# This can be done in another way. Check the second import.
# In this way more than one function can be imported with a comma.

print(lbs_t_kgs(169))
