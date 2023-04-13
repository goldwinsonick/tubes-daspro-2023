# Fungsi RNG
CURRENT_SEED = 1
def LCG(seed):
    m = 2**31
    a = 1103515245
    c = 12345
    return (a*(seed) + c) % m
def rng(fr, to):
    global CURRENT_SEED 
    CURRENT_SEED = LCG(CURRENT_SEED)
    return fr + (CURRENT_SEED % (to-fr+1))

# Fungsi untuk tes distribusi angka yang muncul dari LCG RNG
def testRNG(a, b, N):
    arr = [0 for i in range(b+1)]
    for i in range(N):
        x = rng(a,b)
        arr[x] += 1
    for i in range(a,b+1):
        print(str(i) + ": " + "{:.2f}".format(arr[i]/N) + "% - [" + str(arr[i]) + "]")
# testRNG(1,5, 1000)



