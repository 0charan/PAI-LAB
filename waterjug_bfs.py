from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))   

    path = []

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path.append((x, y))

  
        if x == target or y == target:
            print("Solution Path:")
            for state in path:
                print(state)
            return

        states = [
            (jug1, y),          
            (x, jug2),        
            (0, y),            
            (x, 0),            

            (x - min(x, jug2 - y), y + min(x, jug2 - y)),

            (x + min(y, jug1 - x), y - min(y, jug1 - x))
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("Solution not possible")

if __name__ == "__main__":
    jug1 = int(input("Enter capacity of Jug1: "))
    jug2 = int(input("Enter capacity of Jug2: "))
    target = int(input("Enter target amount: "))

    water_jug(jug1, jug2, target)
