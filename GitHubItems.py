#!/usr/bin/python3

# ©copyright 1999-2020 Hobee. All rights reserved.
# www.hobeedzc.com
# mailto:LZQpublic@163.com
# Never Settle

import random
import math
import numpy as np
guess=int(input())
real=random.randint()
if real < guess:
	print("too large");
else if real > guess:
	print("too small");
else:
	print("Exactly");
