# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input()) # number of queries
    return [Query(input().split()) for i in range(n)] # queries

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    digits = 10 ** 7
    contacts = [None] * digits # phone book

    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # rewrite contact's name
            if contacts[cur_query.number] != None:
                contacts[cur_query.number] = cur_query.name
            else: # otherwise, just add it
                contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            contacts[cur_query.number] = None
        elif cur_query.type == 'find':
            if contacts[cur_query.number] != None:
                result.append(contacts[cur_query.number])
            else:
                response = 'not found'
                result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

