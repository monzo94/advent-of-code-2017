class Generator:
    def __init__(self, start, factor, divisor=2147483647):
        self._start = self._current = start
        self._factor = factor
        self._divisor = divisor

    def generate(self):
        """Update and return the next value generated by the generator."""
        self._current = (self._current * self._factor) % self._divisor
        return self._current

    def reset(self):
        """Reset the current value of the generator to the starting value."""
        self._current = self._start


def lower_bits(n, bits=16):
    """Get the rightmost bits of the binary representation of a number as a string."""
    binary = bin(n)[2:]
    if len(binary) < bits:
        binary.zfill(bits)
    return binary[-bits:]


def score(gen_a, gen_b, pairs=40000000):
    """Compute the total matchings after running an amount of comparisons given by pairs."""
    score = 0
    for _ in range(pairs):
        if lower_bits(gen_a.generate()) == lower_bits(gen_b.generate()):
            score += 1
    return score


def main():
    with open("input") as f:
        start_a, start_b = [int(n.strip().split()[-1]) for n in f.readlines()]

    factor_a, factor_b = 16807, 48271  # Given as input in the page
    gen_a = Generator(start_a, factor_a)
    gen_b = Generator(start_b, factor_b)
    print("Part 1:", score(gen_a, gen_b))


if __name__ == "__main__":
    main()
