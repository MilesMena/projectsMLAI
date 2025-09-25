import math


def cross_entropy(p,q):
    return -sum(pi * math.log(qi) for pi, qi in zip(p, q))


if __name__ == "__main__":
    softmax = [.1, .1,1]
    gt = [0,0,1]
    print(cross_entropy(gt, softmax))

