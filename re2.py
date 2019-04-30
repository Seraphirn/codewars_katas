import re


def displaymatch(match):
    if match is None:
        return None
    print('<Match: %r, groups=%r>' % (match.group(), match.groups()))


# valid = re.compile(r"^[a2-9tjqk]{5}$")
# displaymatch(valid.match("akt5q"))  # Valid.
# displaymatch(valid.match("akt5e"))  # Invalid.
# displaymatch(valid.match("akt"))    # Invalid.
# displaymatch(valid.match("727ak"))  # Valid.

# pair = re.compile(r"(.).*\1")
# displaymatch(pair.match("717ak"))     # Pair of 7s.
# displaymatch(pair.match("718ak"))     # No pairs.
# displaymatch(pair.match("354aa"))     # Pair of aces.

print(re.findall(r'[o0]{2,3}', "do00oog"))     # Pair of 7s.


import socket
import struct

def int2ip(ipv4int):
    """
    Converts int ipv4 to string view

    :param int ipv4int: ipv4 int, 0..2**32-1
    :returns: string - ipv4-like string
    """

    return socket.inet_ntoa(struct.pack("!I", ipv4int))
print(int2ip(94695955))
