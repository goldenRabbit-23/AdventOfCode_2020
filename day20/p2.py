import sys
from collections import defaultdict


def main():
    data = open(sys.argv[1]).read().split('\n\n')
    tiles = {}
    for block in data:
        lines = block.split('\n')
        tid = int(lines[0][5:-1])
        tiles[tid] = lines[1:]

    N = int(len(tiles)**0.5)

    def orient(g):
        # Loop 4 rotations
        for _ in range(4):
            yield g
            yield g[::-1] # Flip vertical

            # Rotate 90 degrees clockwise
            g = [''.join(x) for x in zip(*g[::-1])]

    # Precompute options: {tid: [(grid, top, right, bottom, left), ...]}
    opts = {}
    edge_cnt = defaultdict(int)

    for tid, t in tiles.items():
        # top, right, bottom, left
        borders = [
            t[0],
            ''.join(r[-1] for r in t),
            t[-1],
            ''.join(r[0] for r in t)
        ]

        # Count edge occurrences to find corners/edges
        for b in borders:
            canonical_edge = min(b, b[::-1])
            edge_cnt[canonical_edge] += 1

        # Store all orientations and their borders
        tile_options = []
        for v in orient(t):
            top_border = v[0]
            right_border = ''.join(r[-1] for r in v)
            bottom_border = v[-1]
            left_border = ''.join(r[0] for r in v)
            tile_options.append((v, top_border, right_border, bottom_border, left_border))

        opts[tid] = tile_options

    # Identify corners to optimize start (tiles with 2 borders that never match anyone else)
    corners = set()
    for tid, t in tiles.items():
        borders = [
            t[0],
            ''.join(r[-1] for r in t),
            t[-1],
            ''.join(r[0] for r in t)
        ]
        unique_edges = 0
        for b in borders:
            canonical_edge = min(b, b[::-1])
            if edge_cnt[canonical_edge] == 1:
                unique_edges += 1

        if unique_edges == 2:
            corners.add(tid)

    # grid stores (tile_id, variant_index)
    grid = [[None] * N for _ in range(N)]
    used = set()

    def backtrack(pos):
        if pos == N * N:
            return True

        r, c = divmod(pos, N)

        # Optimization: Only try actual corners for the top-left spot
        candidates = corners if pos == 0 else opts.keys()

        for tid in candidates:
            if tid in used:
                continue

            # Try every orientation for this tile
            for i, (g, top, right, bottom, left) in enumerate(opts[tid]):
                # Check Up (match top edge to neighbor's bottom edge)
                if r > 0:
                    neighbor_tid, neighbor_var_idx = grid[r - 1][c]
                    neighbor_bottom = opts[neighbor_tid][neighbor_var_idx][3]
                    if top != neighbor_bottom:
                        continue

                # Check Left (match left edge to neighbor's right edge)
                if c > 0:
                    neighbor_tid, neighbor_var_idx = grid[r][c - 1]
                    neighbor_right = opts[neighbor_tid][neighbor_var_idx][2]
                    if left != neighbor_right:
                        continue

                grid[r][c] = (tid, i)
                used.add(tid)

                if backtrack(pos + 1):
                    return True

                used.remove(tid)
                grid[r][c] = None

        return False

    backtrack(0)

    # Stitch image (remove borders)
    # Tile size without borders
    tile_h = len(tiles[list(tiles)[0]])

    img = []
    for r in range(N):
        for i in range(1, tile_h - 1):
            row_str = ''
            for c in range(N):
                tid, var_idx = grid[r][c]
                tile_grid = opts[tid][var_idx][0]
                row_str += tile_grid[i][1:-1]
            img.append(row_str)

    # Monster hunt
    monster = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    ]

    m_pts = []
    for r, l in enumerate(monster):
        for c, char in enumerate(l):
            if char == '#':
                m_pts.append((r, c))

    m_h, m_w = len(monster), len(monster[0])

    for im in orient(img):
        m_cnt = 0
        img_h, img_w = len(im), len(im[0])

        for r in range(img_h - m_h + 1):
            for c in range(img_w - m_w + 1):
                if all(im[r + dr][c + dc] == '#' for dr, dc in m_pts):
                    m_cnt += 1

        if m_cnt:
            print(sum(row.count('#') for row in im) - m_cnt * len(m_pts))
            break


if __name__ == '__main__':
    main()
