import sys
from collections import defaultdict
from math import prod


def main():
    data = open(sys.argv[1]).read().split('\n\n')

    # Extract canonical edges (min of edge or its reverse) for each tile
    tile_edges = {}
    for block in data:
        lines = block.split('\n')
        tid = int(lines[0][5:-1])
        tile = lines[1:]

        borders = [
            tile[0],                      # Top
            tile[-1],                     # Bottom
            ''.join(r[0] for r in tile),  # Left
            ''.join(r[-1] for r in tile)  # Right
        ]
        tile_edges[tid] = {min(b, b[::-1]) for b in borders}

    # Count how many neighbors each tile has based on shared edges
    match_counts = defaultdict(int)
    tids = list(tile_edges.keys())

    for i, tid1 in enumerate(tids):
        for tid2 in tids[i+1:]:
            if not tile_edges[tid1].isdisjoint(tile_edges[tid2]):
                match_counts[tid1] += 1
                match_counts[tid2] += 1

    # Corners have exactly 2 matching neighbors
    corners = [tid for tid, count in match_counts.items() if count == 2]
    print(prod(corners))


if __name__ == '__main__':
    main()
