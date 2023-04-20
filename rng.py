# Fungsi RNG
CURRENT_SEED = 1


def LCG(seed):
    m = 2**31
    a = 1103515245
    c = 12345
    return (a*(seed) + c) % m


def rng(num, fr, to):
    global CURRENT_SEED
    numbers = [None for i in range(num)]
    for i in range(num):
        CURRENT_SEED = LCG(CURRENT_SEED)
        number = fr + (CURRENT_SEED % (to-fr+1))
        numbers[i] = number
    return numbers


def rng_solo(num, fr, to):
    import time
    seed = int(time.time() * 1000) # ambil waktu saat ini dalam milidetik sebagai seed
    numbers = [None for i in range(num)]
    for i in range(num):
        seed = LCG(seed)
        number = fr + (seed % (to-fr+1))
        numbers[i] = number
    return numbers

# Fungsi untuk tes distribusi angka yang muncul dari LCG RNG


def testRNG(a, b, N):
    arr = [0 for i in range(b+1)]
    for i in range(N):
        x = rng(a, b)
        arr[x] += 1
    for i in range(a, b+1):
        print(str(i) + ": " +
              "{:.2f}".format(arr[i]/N) + "% - [" + str(arr[i]) + "]")
# testRNG(1,5, 1000)
# print(rng(3,1,5))
