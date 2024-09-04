class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, direction = 0, 0, 0
        obstacle_set = set(map(tuple, obstacles))
        max_distance = 0
        
        for command in commands:
            if command == -1:  # Turn right
                direction = (direction + 1) % 4
            elif command == -2:  # Turn left
                direction = (direction - 1) % 4
            else:  # Move forward
                for _ in range(command):
                    next_x = x + directions[direction][0]
                    next_y = y + directions[direction][1]
                    if (next_x, next_y) in obstacle_set:
                        break
                    x, y = next_x, next_y
                    max_distance = max(max_distance, x*x + y*y)
        
        return max_distance