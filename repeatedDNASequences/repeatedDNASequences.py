from collections import Counter

def repeatedDNASequences(s):
    seq_cnt = Counter()
    for index in range(0, len(s) - 9):
        seq_cnt[s[index:index + 10]] += 1
    results = []
    for seq in seq_cnt:
        if (seq_cnt[seq] > 1):
            results.append(seq)
    return sorted(results)
