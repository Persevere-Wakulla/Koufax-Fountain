from collections import deque

# Implementing the graph
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def name_ends_with_y(name):
    return name[-1] == 'y'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if name_ends_with_y(person):
                print(person, " name ends with y")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
                
    return False

search("you")