import time
from enum import IntEnum
from typing import Tuple, List


# Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
class Nucleotide(IntEnum):
    A = 1
    C = 2
    G = 3
    T = 4


print(Nucleotide)
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
print(Codon)
Gene = List[Codon]
print(Gene)

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def string2gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)
    return gene


my_gene = string2gene(gene_str)
print(my_gene)


def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False


acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
t1 = time.time()
print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))
print("线性搜索花费时间为:", time.time() - t1)


def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False


# 先进行排序
t2 = time.time()
my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg))
print(binary_contains(my_sorted_gene, gat))
print("二分查找花费时间为:", time.time() - t2)
