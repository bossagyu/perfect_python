# -*- coding: utf-8 -*-

import re

text = "sub test aaa:desui value='geroger111.'"
pattern = "value='(.*)'"

m = re.compile(pattern)

result = m.search(text)

print result.group()
print result.group(0)
print result.group(1)

