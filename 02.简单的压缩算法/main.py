class CompressedGene:
    def __init__(self, gene: str) -> None:
        self.gene_dict = {
            'A': 0b00,
            'C': 0b01,
            'G': 0b10,
            'T': 0b11
        }
        self._compress(gene)

    def get_key(self, val):
        for key, value in self.gene_dict.items():
            if val == value:
                return key

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            # shift left two bit
            self.bit_string <<= 2
            self.bit_string |= self.gene_dict[nucleotide]

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            # 虽然不知道在遍历什么东西 但是感觉很厉害的样子
            bits: int = self.bit_string >> i & 0b11
            gene += self.get_key(bits)
        return gene[::-1]

    def __str__(self):
        return self.decompress()


if __name__ == '__main__':
    from sys import getsizeof

    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 1000
    print(f"The original is {getsizeof(original)} bytes")
    compressed: CompressedGene = CompressedGene(original)
    print(f"The compressed is {getsizeof(compressed.bit_string)} bytes")
    print(compressed)
    print(f"original and decompressed are the same: {original == compressed.decompress()}")
