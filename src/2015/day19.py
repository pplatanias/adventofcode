from collections import defaultdict
import re

with open('inputs/2015/day19.txt','r') as file:
    replacements, genome = file.read().split('\n\n')
    replacements = replacements.split('\n')

genes = defaultdict(list)
revgenes = {}
for source,dest in [x.split(' => ') for x in replacements]:
    genes[source].append(dest)
    revgenes[dest] = source

# Part 1
new_genomes = []
for gene, dests in genes.items():
    for dest in dests:
        for m in re.finditer(gene, genome):
            new_genomes.append(genome[:m.start()] + dest + genome[m.end():])
print(len(set(new_genomes)))

# Part 2  not my solution
words = 0
for ch in genome:
    if ch.isupper():
        words += 1
print(words - genome.count('Rn') - genome.count('Ar') - (genome.count('Y')*2) - 1)
