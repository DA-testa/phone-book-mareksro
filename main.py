# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    # paturu numurus, kas iepriekš tika pievienoti
    telefons = set()
    for cur_query in queries:
        if cur_query.type == 'add':
            # pievienoju sarakstā, ja tel numurs ir jauns
            if cur_query.number not in telefons:
                contacts[cur_query.number] = cur_query.name
                telefons.add(cur_query.number)
                # otherwise, just add it
            else:
                contacts[cur_query.number] = cur_query.name
            # noņemu no sarkasta, ja vēl pastāv
        elif cur_query.type == 'del':
            contacts.pop(cur_query.number, None)
            telefons.discard(cur_query.number)
            # tiek meklēts pēc numura
        else:
            result.append(contacts.get(cur_query.number, 'not found'))
            
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

