# python3

class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = row_counts
        self.parents = list(range(n_tables))
        

    # merge two components
    # union by rank heuristic
    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)
        
        if src_parent == dst_parent:
            return False

        if self.ranks[src_parent] > self.ranks[dst_parent]:
            self.parents[dst_parent] = src_parent
            self.ranks[src_parent] += self.ranks[dst_parent]
            self.ranks[dst_parent] = 0
            self.max_row_count = max(self.max_row_count, self.ranks[src_parent])
        else:
            self.parents[src_parent] = dst_parent
            self.ranks[dst_parent] += self.ranks[src_parent]
            self.ranks[src_parent] = 0
            self.max_row_count = max(self.max_row_count, self.ranks[dst_parent])

        return True

    # find parent
    def get_parent(self, table):
        if table != self.parents[table]:
            self.parents[table] = self.get_parent(self.parents[table]) # path compression 
        
        return self.parents[table]


def main():
    # read inputs for number of tables and number of merge queries
    n_tables, n_queries = map(int, input().split())
    
    # number of rows of tables
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)

    # merge queries
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
