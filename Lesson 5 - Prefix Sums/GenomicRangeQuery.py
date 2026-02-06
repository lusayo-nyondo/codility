# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def get_impact_factor(genome):
    if genome == 'A':
        return 1
    elif genome == 'C':
        return 2
    elif genome == 'G':
        return 3
    elif genome == 'T':
        return 4

def solution(S, P, Q):
    # Create place holders for prefix sums for each genome.
    result = []
    N = len(S)

    A = [0] * N
    C = [0] * N
    G = [0] * N
    T = [0] * N

    a = c = g = t = 0

    # Generate prefix sums for occurences of each genome in the respective genomes. Occurences are indicated by 1.
    for i in range(0, N):
        if S[i] == 'A':
            a += 1
        elif S[i] == 'C':
            c += 1
        elif S[i] == 'G':
            g += 1
        elif S[i] == 'T':
            t += 1
    
        A[i] = a
        C[i] = c
        G[i] = g
        T[i] = t
    
    for i in range(0, len(P)):
        left_most_genome_idx = P[i]
        right_most_genome_idx = Q[i]

        impact_factor = 0
    
        if left_most_genome_idx == right_most_genome_idx:
            impact_factor = get_impact_factor(S[left_most_genome_idx])
        elif A[left_most_genome_idx] < A[right_most_genome_idx] or S[left_most_genome_idx] == 'A':
            impact_factor = get_impact_factor('A')
        elif C[left_most_genome_idx] < C[right_most_genome_idx] or S[left_most_genome_idx] == 'C':
            impact_factor = get_impact_factor('C')
        elif G[left_most_genome_idx] < G[right_most_genome_idx] or S[left_most_genome_idx] == 'G':
            impact_factor = get_impact_factor('G')
        elif T[left_most_genome_idx] < T[right_most_genome_idx] or S[left_most_genome_idx] == 'T':
            impact_factor = get_impact_factor('T')
        
        if impact_factor != 0:
            result.append(impact_factor)
    
    return result