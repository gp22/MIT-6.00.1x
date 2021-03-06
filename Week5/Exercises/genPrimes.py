# CHECK IF PRIME, if Prime return 0
def isPrime(n):
	if n in (1, 2, 3):
		return False
	if n % 2 == 0:
		return False
	if n % 3 == 0:
		return False

	i = 5
	jump = 2 # all primes are of the form 6k ± 1

	while i < n // 2:
		if n % i == 0:
			return False

		i += jump
		jump = 6 - jump  # all primes are of the form 6k ± 1,

	return True

#def genPrimes():
#    next = 1
#    primes = [2, 3]
#    while True:
#        if len(primes) <= 3:
#            yield next
#            primes.append(next)
#            next += 1
#        else:
#            while True:
#                next += 1
#                for number in primes[1:]:
#                    if next % number == 0:
#                        continue
#                yield next
#                primes.append(next)

# def genPrimes(): # from superpawko on Slack
#     n = 2 # START NUMBER
#     p = [] # primes list
#     while True: # END number for now
#         for x in range(2,(n//2)+2):  # search for number which is not more than half of a "n"
#             if n % x ==0:
#                 break
#         if x == (n//2)+1: # after checking every number and it is still working append prime number
#             p.append(n)
#             yield n
#
#         n += 1
		
def genPrimes():
    yield 2
    primes = [2, 3]
    while True:
        yield primes[-1]
        n = primes[-1] + 2
        for p in primes:
            if n % p == 0:
                n += 2
                continue
            else:
                for p in primes:
                    if n % p == 0:
                        n += 2
                        break
                else:
                    primes.append(n)
                    break

primes = genPrimes()
for i in range(10):
	print(primes.__next__())
