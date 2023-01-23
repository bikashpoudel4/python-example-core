"""Incorrect Use of Condition"""


"""
In your normal speech you could probably say something like 
    - 'If sataus_code is 401 or 302'
        - do something else.
* Meaning status_code can be either 401 or 303.
"""
# Example
if status_code == 401 or 302:
    pass

"""
However this is correct. This condition will be always true as this is actually same as if you wrote.
if(status_code == 401) or (302) so it will compare status_code to 401, and it will separately check if
302 id True, but any number different from 0 is considered to be True so the above expression will always be True.
    - 
"""
# example
if status_code == 401 or status_code == 302:
    pass

"""
An alternative way to achieve the same results would be through probably at this point we have not learned the 'in' operator,
not lists(comma separated values in square brackets):
"""
# example
if ststus_code in [401, 302]
    pass