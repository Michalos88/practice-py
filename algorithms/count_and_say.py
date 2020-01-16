"""Count and say sequence generation"""
# as in https://leetcode.com/problems/count-and-say/


class CountSaySeq:
    def generate(self, n: int) -> str:
        seq = ["1"]
        for _ in range(n-1):
            id = 0
            new_seq = list()
            while id < len(seq):
                frequency = self.get_frequency(seq, id)
                new_seq.append(str(frequency))
                new_seq.append(seq[id])
                id += frequency
            seq = new_seq
        return "".join(seq)

    def get_frequency(self, seq, start):
        frequency = 0
        target = seq[start]
        for id in range(start, len(seq)):
            cur = seq[id]
            if cur == target:
                frequency += 1
            else:
                break
        return frequency


class CountSaySeqTests(object):
    def run_all(self):
        self.generate()

    def generate(self):
        seq = CountSaySeq()
        assert seq.generate(4) == "1211"
        assert seq.generate(5) == "111221"
        assert seq.generate(6) == "312211"
        assert seq.generate(7) == "13112221"
        assert seq.generate(8) == "1113213211"
        print("generate_test: passed")


if __name__ == "__main__":
    tests = CountSaySeqTests()
    tests.run_all()
