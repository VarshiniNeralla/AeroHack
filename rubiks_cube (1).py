import copy
import random
from collections import deque

class RubiksCube:
    def __init__(self):
        self.cube = {
            'U': [['W' for _ in range(3)] for _ in range(3)],
            'D': [['Y' for _ in range(3)] for _ in range(3)],
            'F': [['G' for _ in range(3)] for _ in range(3)],
            'B': [['B' for _ in range(3)] for _ in range(3)],
            'L': [['O' for _ in range(3)] for _ in range(3)],
            'R': [['R' for _ in range(3)] for _ in range(3)]
        }
        self.adjacent = {
            'U': [('F', 0, [0,1,2]), ('R', 2, [0,1,2]), ('B', 2, [2,1,0]), ('L', 0, [2,1,0])],
            'D': [('F', 2, [0,1,2]), ('L', 0, [0,1,2]), ('B', 0, [2,1,0]), ('R', 2, [2,1,0])],
            'F': [('U', 2, [0,1,2]), ('R', 0, [0,1,2]), ('D', 0, [2,1,0]), ('L', 2, [2,1,0])],
            'B': [('U', 0, [2,1,0]), ('L', 0, [0,1,2]), ('D', 2, [0,1,2]), ('R', 2, [2,1,0])],
            'L': [('U', 0, [0,1,2]), ('F', 0, [0,1,2]), ('D', 0, [0,1,2]), ('B', 2, [2,1,0])],
            'R': [('U', 2, [2,1,0]), ('B', 0, [0,1,2]), ('D', 2, [2,1,0]), ('F', 2, [2,1,0])]
        }

    def rotate_face(self, face, clockwise=True):
        temp = copy.deepcopy(self.cube[face])
        for i in range(3):
            for j in range(3):
                if clockwise:
                    self.cube[face][i][j] = temp[2-j][i]
                else:
                    self.cube[face][i][j] = temp[j][2-i]
        
        adj_faces = self.adjacent[face]
        temp_rows = []
        for adj_face, idx, order in adj_faces:
            if face in ['U', 'D'] and adj_face in ['F', 'B']:
                temp_row = [self.cube[adj_face][idx][i] for i in order]
            elif face in ['U', 'D'] and adj_face in ['L', 'R']:
                temp_row = [self.cube[adj_face][i][idx] for i in order]
            elif face in ['F', 'B'] and adj_face in ['U', 'D']:
                temp_row = [self.cube[adj_face][idx][i] for i in order]
            elif face in ['F', 'B'] and adj_face in ['L', 'R']:
                temp_row = [self.cube[adj_face][i][idx] for i in order]
            elif face in ['L', 'R'] and adj_face in ['U', 'D']:
                temp_row = [self.cube[adj_face][i][idx] for i in order]
            elif face in ['L', 'R'] and adj_face in ['F', 'B']:
                temp_row = [self.cube[adj_face][idx][i] for i in order]
            else:
                temp_row = [self.cube[adj_face][idx][i] for i in order]
            temp_rows.append(temp_row)
        
        for i in range(4):
            if clockwise:
                next_idx = (i + 1) % 4
            else:
                next_idx = (i - 1) % 4
            adj_face, idx, order = adj_faces[next_idx]
            if face in ['U', 'D'] and adj_face in ['F', 'B']:
                for j, idx_in_order in enumerate(order):
                    self.cube[adj_face][idx][idx_in_order] = temp_rows[i][j]
            elif face in ['U', 'D'] and adj_face in ['L', 'R']:
                for j, idx_in_order in enumerate(order):
                    self.cube[adj_face][idx_in_order][idx] = temp_rows[i][j]
            elif face in ['F', 'B'] and adj_face in ['U', 'D']:
                for j, idx_in_order in enumerate(order):
                    self.cube[adj_face][idx][idx_in_order] = temp_rows[i][j]
            elif face in ['F', 'B'] and adj_face in ['L', 'R']:
                for j, idx_in_order in enumerate(order):
                    self.cube[adj_face][idx_in_order][idx] = temp_rows[i][j]
            elif face in ['L', 'R'] and adj_face in ['U', 'D']:
                for j, idx_in_order in enumerate(order):
                    self.cube[adj_face][idx_in_order][idx] = temp_rows[i][j]
            elif face in ['L', 'R'] and adj_face in ['F', 'B']:
                for j, idx_in_order in enumerate(order):
                    self.cube[adj_face][idx][idx_in_order] = temp_rows[i][j]
            else:
                for j, idx_in_order in enumerate(order):
                    self.cube[adj_face][idx][idx_in_order] = temp_rows[i][j]

    def move(self, notation):
        if not notation:
            return
        face = notation[0]
        if len(notation) > 1 and notation[1] == '2':
            self.rotate_face(face, True)
            self.rotate_face(face, True)
        else:
            clockwise = not (len(notation) > 1 and notation[1] == "'")
            self.rotate_face(face, clockwise)

    def scramble(self, moves=None, move_count=20):
        if moves is None:
            moves = []
            for _ in range(move_count):
                move = random.choice(['F', 'B', 'U', 'D', 'L', 'R', "F'", "B'", "U'", "D'", "L'", "R'", 'F2', 'B2', 'U2', 'D2', 'L2', 'R2'])
                moves.append(move)
        for move in moves:
            self.move(move)
        return moves

    def is_solved(self):
        for face in self.cube:
            color = self.cube[face][1][1]
            for row in self.cube[face]:
                for piece in row:
                    if piece != color:
                        return False
        return True

    def display(self):
        print(" " + " ".join(self.cube['U'][0]))
        print(" " + " ".join(self.cube['U'][1]))
        print(" " + " ".join(self.cube['U'][2]))
        print()
        for i in range(3):
            print(" ".join(self.cube['L'][i]) + " " +
                  " ".join(self.cube['F'][i]) + " " +
                  " ".join(self.cube['R'][i]) + " " +
                  " ".join(self.cube['B'][i]))
        print()
        print(" " + " ".join(self.cube['D'][0]))
        print(" " + " ".join(self.cube['D'][1]))
        print(" " + " ".join(self.cube['D'][2]))
        print()

class RubiksCubeSolver:
    def __init__(self, cube):
        self.cube = cube
        self.solution = []

    def solve(self):
        if self.cube.is_solved():
            return []
        self.solution = []
        print("Solving white cross...")
        self.solve_white_cross()
        print("White cross solved. Cube state:")
        self.cube.display()
        print("Solving white corners...")
        self.solve_white_corners()
        print("White corners solved. Cube state:")
        self.cube.display()
        print("Solving middle layer...")
        self.solve_middle_layer()
        print("Middle layer solved. Cube state:")
        self.cube.display()
        print("Solving yellow cross...")
        self.solve_yellow_cross()
        print("Yellow cross solved. Cube state:")
        self.cube.display()
        print("Solving yellow corners...")
        self.solve_yellow_corners()
        print("Yellow corners solved. Cube state:")
        self.cube.display()
        print("Solving yellow edges...")
        self.solve_yellow_edges()
        print("Final solved cube:")
        self.cube.display()
        return self.solution

    def execute(self, moves):
        for move in moves:
            self.cube.move(move)
            self.solution.append(move)

    def find_edge(self, color1, color2):
        edge_positions = {
            'U': [(0, 1), (1, 0), (1, 2), (2, 1)],
            'D': [(0, 1), (1, 0), (1, 2), (2, 1)],
            'F': [(0, 1), (1, 0), (1, 2), (2, 1)],
            'B': [(0, 1), (1, 0), (1, 2), (2, 1)],
            'L': [(0, 1), (1, 0), (1, 2), (2, 1)],
            'R': [(0, 1), (1, 0), (1, 2), (2, 1)]
        }
        for face in edge_positions:
            for r, c in edge_positions[face]:
                face_color = self.cube.cube[face][r][c]
                adj_color = self.get_adjacent_edge_color(face, r, c)
                if {face_color, adj_color} == {color1, color2}:
                    return face, r, c
        return None, None, None

    def get_adjacent_edge_color(self, face, r, c):
        edge_adjacent = {
            'U': {(0, 1): ('B', 0, 1), (1, 0): ('L', 0, 1), (1, 2): ('R', 0, 1), (2, 1): ('F', 0, 1)},
            'D': {(0, 1): ('F', 2, 1), (1, 0): ('L', 2, 1), (1, 2): ('R', 2, 1), (2, 1): ('B', 2, 1)},
            'F': {(0, 1): ('U', 2, 1), (1, 0): ('L', 1, 2), (1, 2): ('R', 1, 0), (2, 1): ('D', 0, 1)},
            'B': {(0, 1): ('U', 0, 1), (1, 0): ('R', 1, 2), (1, 2): ('L', 1, 0), (2, 1): ('D', 2, 1)},
            'L': {(0, 1): ('U', 1, 0), (1, 0): ('B', 1, 2), (1, 2): ('F', 1, 0), (2, 1): ('D', 1, 0)},
            'R': {(0, 1): ('U', 1, 2), (1, 0): ('F', 1, 2), (1, 2): ('B', 1, 0), (2, 1): ('D', 1, 2)}
        }
        adj_face, adj_r, adj_c = edge_adjacent[face][(r, c)]
        return self.cube.cube[adj_face][adj_r][adj_c]

    def find_corner(self, color1, color2, color3):
        corner_positions = {
            'U': [(0, 0), (0, 2), (2, 0), (2, 2)],
            'D': [(0, 0), (0, 2), (2, 0), (2, 2)],
            'F': [(0, 0), (0, 2), (2, 0), (2, 2)],
            'B': [(0, 0), (0, 2), (2, 0), (2, 2)],
            'L': [(0, 0), (0, 2), (2, 0), (2, 2)],
            'R': [(0, 0), (0, 2), (2, 0), (2, 2)]
        }
        for face in corner_positions:
            for r, c in corner_positions[face]:
                colors = self.get_corner_colors(face, r, c)
                if set(colors) == {color1, color2, color3}:
                    return face, r, c
        return None, None, None

    def get_corner_colors(self, face, r, c):
        corner_adjacent = {
            'U': {
                (0, 0): [('U', 0, 0), ('L', 0, 0), ('B', 0, 2)],
                (0, 2): [('U', 0, 2), ('B', 0, 0), ('R', 0, 2)],
                (2, 0): [('U', 2, 0), ('F', 0, 0), ('L', 0, 2)],
                (2, 2): [('U', 2, 2), ('R', 0, 0), ('F', 0, 2)]
            },
            'D': {
                (0, 0): [('D', 0, 0), ('L', 2, 2), ('F', 2, 0)],
                (0, 2): [('D', 0, 2), ('F', 2, 2), ('R', 2, 2)],
                (2, 0): [('D', 2, 0), ('B', 2, 2), ('L', 2, 0)],
                (2, 2): [('D', 2, 2), ('R', 2, 0), ('B', 2, 0)]
            }
        }
        if face in ['F', 'B', 'L', 'R']:
            if face == 'F':
                corner_map = {
                    (0, 0): [('F', 0, 0), ('U', 2, 0), ('L', 0, 2)],
                    (0, 2): [('F', 0, 2), ('R', 0, 0), ('U', 2, 2)],
                    (2, 0): [('F', 2, 0), ('L', 2, 2), ('D', 0, 0)],
                    (2, 2): [('F', 2, 2), ('D', 0, 2), ('R', 2, 2)]
                }
            elif face == 'B':
                corner_map = {
                    (0, 0): [('B', 0, 0), ('R', 0, 2), ('U', 0, 2)],
                    (0, 2): [('B', 0, 2), ('U', 0, 0), ('L', 0, 0)],
                    (2, 0): [('B', 2, 0), ('D', 2, 2), ('R', 2, 0)],
                    (2, 2): [('B', 2, 2), ('L', 2, 0), ('D', 2, 0)]
                }
            elif face == 'L':
                corner_map = {
                    (0, 0): [('L', 0, 0), ('U', 0, 0), ('B', 0, 2)],
                    (0, 2): [('L', 0, 2), ('F', 0, 0), ('U', 2, 0)],
                    (2, 0): [('L', 2, 0), ('B', 2, 2), ('D', 2, 0)],
                    (2, 2): [('L', 2, 2), ('D', 0, 0), ('F', 2, 0)]
                }
            elif face == 'R':
                corner_map = {
                    (0, 0): [('R', 0, 0), ('F', 0, 2), ('U', 2, 2)],
                    (0, 2): [('R', 0, 2), ('U', 0, 2), ('B', 0, 0)],
                    (2, 0): [('R', 2, 0), ('D', 2, 2), ('B', 2, 0)],
                    (2, 2): [('R', 2, 2), ('D', 0, 2), ('F', 2, 2)]
                }
            faces_and_positions = corner_map[(r, c)]
        else:
            faces_and_positions = corner_adjacent[face][(r, c)]
        colors = []
        for f, row, col in faces_and_positions:
            colors.append(self.cube.cube[f][row][col])
        return colors

    def solve_white_cross(self):
        targets = [
            ('W', 'G', 'U', 2, 1),
            ('W', 'R', 'U', 1, 2),
            ('W', 'B', 'U', 0, 1),
            ('W', 'O', 'U', 1, 0)
        ]
        for w_color, side_color, target_face, target_r, target_c in targets:
            print(f"Positioning {w_color}-{side_color} edge...")
            face, r, c = self.find_edge(w_color, side_color)
            if face is None:
                print(f"Edge {w_color}-{side_color} not found!")
                continue
            if face != 'U':
                self.move_edge_to_top(face, r, c, w_color, side_color)
            self.position_white_edge_on_top(w_color, side_color, target_face, target_r, target_c)

    def move_edge_to_top(self, face, r, c, color1, color2):
        if face == 'D':
            if r == 0 and c == 1:
                self.execute(['F', 'F'])
            elif r == 1 and c == 2:
                self.execute(['R', 'R'])
            elif r == 2 and c == 1:
                self.execute(['B', 'B'])
            elif r == 1 and c == 0:
                self.execute(['L', 'L'])
        elif face in ['F', 'B', 'L', 'R']:
            if face == 'F':
                if r == 1 and c == 0:
                    self.execute(['L', 'U', 'L\''])
                elif r == 1 and c == 2:
                    self.execute(['R\'', 'U\'', 'R'])
            elif face == 'R':
                if r == 1 and c == 0:
                    self.execute(['F\'', 'U\'', 'F'])
                elif r == 1 and c == 2:
                    self.execute(['B', 'U', 'B\''])
            elif face == 'B':
                if r == 1 and c == 0:
                    self.execute(['R', 'U', 'R\''])
                elif r == 1 and c == 2:
                    self.execute(['L\'', 'U\'', 'L'])
            elif face == 'L':
                if r == 1 and c == 0:
                    self.execute(['B\'', 'U\'', 'B'])
                elif r == 1 and c == 2:
                    self.execute(['F', 'U', 'F\''])

    def position_white_edge_on_top(self, w_color, side_color, target_face, target_r, target_c):
        for _ in range(4):
            face, r, c = self.find_edge(w_color, side_color)
            if face == 'U':
                adj_color = self.get_adjacent_edge_color(face, r, c)
                if adj_color == side_color:
                    if r == target_r and c == target_c:
                        if self.cube.cube[face][r][c] == w_color:
                            print(f"Edge {w_color}-{side_color} correctly positioned")
                            return
                        else:
                            if target_r == 2 and target_c == 1:
                                self.execute(['F', 'R', 'U', 'R\'', 'U\'', 'F\''])
                            elif target_r == 1 and target_c == 2:
                                self.execute(['R', 'B', 'U', 'B\'', 'U\'', 'R\''])
                            elif target_r == 0 and target_c == 1:
                                self.execute(['B', 'L', 'U', 'L\'', 'U\'', 'B\''])
                            elif target_r == 1 and target_c == 0:
                                self.execute(['L', 'F', 'U', 'F\'', 'U\'', 'L\''])
                            return
            self.execute(['U'])

    def solve_white_corners(self):
        targets = [
            ('W', 'G', 'R'),
            ('W', 'O', 'G'),
            ('W', 'B', 'O'),
            ('W', 'R', 'B')
        ]
        for colors in targets:
            self.position_white_corner(colors)

    def position_white_corner(self, colors):
        w_color, color2, color3 = colors
        print(f"Positioning corner {w_color}-{color2}-{color3}...")
        face, r, c = self.find_corner(w_color, color2, color3)
        if face is None:
            print(f"Corner {w_color}-{color2}-{color3} not found!")
            return
        if face == 'D':
            self.move_corner_to_correct_bottom_position(colors)
        elif face == 'U':
            self.move_corner_from_top_to_bottom(colors)
            self.move_corner_to_correct_bottom_position(colors)
        else:
            self.move_corner_from_side_to_bottom(face, r, c)
            self.move_corner_to_correct_bottom_position(colors)
        self.insert_corner_from_bottom(colors)

    def move_corner_to_correct_bottom_position(self, colors):
        target_pos = self.get_target_bottom_position(colors)
        for _ in range(4):
            face, r, c = self.find_corner(*colors)
            if face == 'D' and (r, c) == target_pos:
                break
            self.execute(['D'])

    def get_target_bottom_position(self, colors):
        w_color, color2, color3 = colors
        if set([color2, color3]) == {'G', 'R'}:
            return (0, 2)
        elif set([color2, color3]) == {'O', 'G'}:
            return (0, 0)
        elif set([color2, color3]) == {'B', 'O'}:
            return (2, 0)
        elif set([color2, color3]) == {'R', 'B'}:
            return (2, 2)

    def move_corner_from_top_to_bottom(self, colors):
        face, r, c = self.find_corner(*colors)
        if face == 'U':
            if r == 2 and c == 2:
                self.execute(['R', 'D', 'R\''])
            elif r == 2 and c == 0:
                self.execute(['L\'', 'D\'', 'L'])
            elif r == 0 and c == 0:
                self.execute(['L', 'D', 'L\''])
            elif r == 0 and c == 2:
                self.execute(['R\'', 'D\'', 'R'])

    def move_corner_from_side_to_bottom(self, face, r, c):
        if face == 'F':
            if r == 0:
                self.execute(['R', 'D', 'R\''] if c == 2 else ['L\'', 'D\'', 'L'])
        elif face == 'R':
            if r == 0:
                self.execute(['B', 'D', 'B\''] if c == 2 else ['F\'', 'D\'', 'F'])
        elif face == 'B':
            if r == 0:
                self.execute(['L', 'D', 'L\''] if c == 2 else ['R\'', 'D\'', 'R'])
        elif face == 'L':
            if r == 0:
                self.execute(['F', 'D', 'F\''] if c == 2 else ['B\'', 'D\'', 'B'])

    def insert_corner_from_bottom(self, colors):
        w_color, color2, color3 = colors
        if set([color2, color3]) == {'G', 'R'}:
            face_move = 'R'
        elif set([color2, color3]) == {'O', 'G'}:
            face_move = 'L'
        elif set([color2, color3]) == {'B', 'O'}:
            face_move = 'L'
        elif set([color2, color3]) == {'R', 'B'}:
            face_move = 'R'
        for _ in range(3):
            target_face, target_r, target_c = self.get_target_corner_position(colors)
            if self.cube.cube[target_face][target_r][target_c] == w_color:
                break
            if face_move == 'R':
                self.execute(['R', 'D', 'R\'', 'D\''])
            else:
                self.execute(['L\'', 'D\'', 'L', 'D'])

    def get_target_corner_position(self, colors):
        w_color, color2, color3 = colors
        if set([color2, color3]) == {'G', 'R'}:
            return ('U', 2, 2)
        elif set([color2, color3]) == {'O', 'G'}:
            return ('U', 2, 0)
        elif set([color2, color3]) == {'B', 'O'}:
            return ('U', 0, 0)
        elif set([color2, color3]) == {'R', 'B'}:
            return ('U', 0, 2)

    def solve_middle_layer(self):
        edges = [
            ('G', 'R'),
            ('R', 'B'),
            ('B', 'O'),
            ('O', 'G')
        ]
        for edge_colors in edges:
            print(f"Positioning middle edge {edge_colors[0]}-{edge_colors[1]}...")
            self.position_middle_edge(edge_colors)

    def position_middle_edge(self, edge_colors):
        color1, color2 = edge_colors
        if self.is_middle_edge_correct(edge_colors):
            print(f"Edge {color1}-{color2} already correctly positioned")
            return
        face, r, c = self.find_edge(color1, color2)
        if face is None:
            print(f"Edge {color1}-{color2} not found!")
            return
        if face in ['F', 'R', 'B', 'L'] and r == 1:
            self.remove_middle_edge(face, r, c)
        self.position_middle_edge_on_top(edge_colors)
        self.insert_middle_edge(edge_colors)

    def is_middle_edge_correct(self, edge_colors):
        color1, color2 = edge_colors
        middle_positions = [
            ('F', 1, 2, 'R', 1, 0),
            ('R', 1, 2, 'B', 1, 0),
            ('B', 1, 2, 'L', 1, 0),
            ('L', 1, 2, 'F', 1, 0)
        ]
        for face1, r1, c1, face2, r2, c2 in middle_positions:
            if (self.cube.cube[face1][r1][c1] == color1 and
                self.cube.cube[face2][r2][c2] == color2):
                return True
            if (self.cube.cube[face1][r1][c1] == color2 and
                self.cube.cube[face2][r2][c2] == color1):
                return True
        return False

    def remove_middle_edge(self, face, r, c):
        if face == 'F' and c == 2:
            self.execute(['R', 'U', 'R\'', 'U\'', 'F\'', 'U\'', 'F'])
        elif face == 'F' and c == 0:
            self.execute(['L\'', 'U\'', 'L', 'U', 'F', 'U', 'F\''])
        elif face == 'R' and c == 2:
            self.execute(['B', 'U', 'B\'', 'U\'', 'R\'', 'U\'', 'R'])
        elif face == 'R' and c == 0:
            self.execute(['F\'', 'U\'', 'F', 'U', 'R', 'U', 'R\''])
        elif face == 'B' and c == 2:
            self.execute(['L', 'U', 'L\'', 'U\'', 'B\'', 'U\'', 'B'])
        elif face == 'B' and c == 0:
            self.execute(['R\'', 'U\'', 'R', 'U', 'B', 'U', 'B\''])
        elif face == 'L' and c == 2:
            self.execute(['F', 'U', 'F\'', 'U\'', 'L\'', 'U\'', 'L'])
        elif face == 'L' and c == 0:
            self.execute(['B\'', 'U\'', 'B', 'U', 'L', 'U', 'L\''])

    def position_middle_edge_on_top(self, edge_colors):
        color1, color2 = edge_colors
        for _ in range(4):
            face, r, c = self.find_edge(color1, color2)
            if face == 'U':
                adj_color = self.get_adjacent_edge_color(face, r, c)
                if adj_color == color1 or adj_color == color2:
                    center_face = self.get_center_face_for_color(adj_color)
                    if self.is_edge_above_center(face, r, c, center_face):
                        return
            self.execute(['U'])

    def get_center_face_for_color(self, color):
        center_colors = {'G': 'F', 'R': 'R', 'B': 'B', 'O': 'L'}
        return center_colors.get(color)

    def is_edge_above_center(self, edge_face, edge_r, edge_c, center_face):
        if edge_r == 2 and edge_c == 1:
            return center_face == 'F'
        elif edge_r == 1 and edge_c == 2:
            return center_face == 'R'
        elif edge_r == 0 and edge_c == 1:
            return center_face == 'B'
        elif edge_r == 1 and edge_c == 0:
            return center_face == 'L'
        return False

    def insert_middle_edge(self, edge_colors):
        color1, color2 = edge_colors
        face, r, c = self.find_edge(color1, color2)
        if face != 'U':
            return
        u_color = self.cube.cube['U'][r][c]
        adj_color = self.get_adjacent_edge_color('U', r, c)
        if r == 2 and c == 1:
            if u_color == color1:
                target_face = self.get_center_face_for_color(color2)
                if target_face == 'R':
                    self.execute(['U', 'R', 'U\'', 'R\'', 'U\'', 'F\'', 'U', 'F'])
                else:
                    self.execute(['U\'', 'L\'', 'U', 'L', 'U', 'F', 'U\'', 'F\''])
            else:
                target_face = self.get_center_face_for_color(color1)
                if target_face == 'R':
                    self.execute(['U', 'R', 'U\'', 'R\'', 'U\'', 'F\'', 'U', 'F'])
                else:
                    self.execute(['U\'', 'L\'', 'U', 'L', 'U', 'F', 'U\'', 'F\''])
        elif r == 1 and c == 2:
            if adj_color == 'B':
                self.execute(['U', 'B', 'U\'', 'B\'', 'U\'', 'R\'', 'U', 'R'])
            else:
                self.execute(['U\'', 'F\'', 'U', 'F', 'U', 'R', 'U\'', 'R\''])
        elif r == 0 and c == 1:
            if adj_color == 'L':
                self.execute(['U', 'L', 'U\'', 'L\'', 'U\'', 'B\'', 'U', 'B'])
            else:
                self.execute(['U\'', 'R\'', 'U', 'R', 'U', 'B', 'U\'', 'B\''])
        elif r == 1 and c == 0:
            if adj_color == 'F':
                self.execute(['U', 'F', 'U\'', 'F\'', 'U\'', 'L\'', 'U', 'L'])
            else:
                self.execute(['U\'', 'B\'', 'U', 'B', 'U', 'L', 'U\'', 'L\''])

    def solve_yellow_cross(self):
        print("Forming yellow cross...")
        for attempt in range(4):
            yellow_edges = 0
            edge_positions = [(0, 1), (1, 0), (1, 2), (2, 1)]
            for r, c in edge_positions:
                if self.cube.cube['D'][r][c] == 'Y':
                    yellow_edges += 1
            print(f"Yellow edges: {yellow_edges}")
            if yellow_edges == 4:
                print("Yellow cross complete!")
                return
            self.execute(['F', 'R', 'U', 'R\'', 'U\'', 'F\''])
            if yellow_edges == 2:
                if ((self.cube.cube['D'][1][0] == 'Y' and self.cube.cube['D'][1][2] == 'Y') or
                    (self.cube.cube['D'][0][1] == 'Y' and self.cube.cube['D'][2][1] == 'Y')):
                    continue
                else:
                    for _ in range(4):
                        if (self.cube.cube['D'][1][0] == 'Y' and self.cube.cube['D'][0][1] == 'Y'):
                            break
                        self.execute(['D'])

    def solve_yellow_corners(self):
        print("Orienting yellow corners...")
        self.position_yellow_corners()
        self.orient_yellow_corners()

    def position_yellow_corners(self):
        for attempt in range(4):
            corners_correct = self.count_correctly_positioned_corners()
            print(f"Correctly positioned corners: {corners_correct}")
            if corners_correct == 4:
                break
            if corners_correct == 0:
                self.execute(['R', 'U', 'R\'', 'F\'', 'R', 'U', 'R\'', 'U\'', 'R\'', 'F', 'R', 'R'])
            else:
                self.rotate_to_correct_corner()
                self.execute(['R', 'U', 'R\'', 'F\'', 'R', 'U', 'R\'', 'U\'', 'R\'', 'F', 'R', 'R'])

    def count_correctly_positioned_corners(self):
        count = 0
        corner_positions = [
            ('D', 0, 0, {'G', 'O'}),
            ('D', 0, 2, {'G', 'R'}),
            ('D', 2, 0, {'B', 'O'}),
            ('D', 2, 2, {'B', 'R'})
        ]
        for face, r, c, expected_colors in corner_positions:
            corner_colors = set(self.get_corner_colors(face, r, c))
            corner_colors.discard('Y')
            if corner_colors == expected_colors:
                count += 1
        return count

    def rotate_to_correct_corner(self):
        for _ in range(4):
            corner_colors = set(self.get_corner_colors('D', 2, 2))
            corner_colors.discard('Y')
            if corner_colors == {'B', 'R'}:
                break
            self.execute(['D'])

    def orient_yellow_corners(self):
        for corner_pos in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            self.orient_single_corner(corner_pos)

    def orient_single_corner(self, pos):
        r, c = pos
        for _ in range(3):
            if self.cube.cube['D'][r][c] == 'Y':
                break
            if r == 2 and c == 2:
                self.execute(['R', 'D', 'R\'', 'D\''])
            elif r == 2 and c == 0:
                self.execute(['L\'', 'D\'', 'L', 'D'])
            elif r == 0 and c == 0:
                self.execute(['L', 'D', 'L\'', 'D\''])
            elif r == 0 and c == 2:
                self.execute(['R\'', 'D\'', 'R', 'D'])
        if pos != (2, 2):
            self.execute(['D'])

    def solve_yellow_edges(self):
        print("Positioning yellow edges...")
        for attempt in range(4):
            correct_edges = self.count_correct_edges()
            print(f"Correct edges: {correct_edges}")
            if correct_edges == 4:
                print("All edges correct!")
                break
            if correct_edges == 0:
                self.execute(['R', 'U', 'R\'', 'F\'', 'R', 'U', 'R\'', 'U\'', 'R\'', 'F', 'R', 'R'])
            else:
                self.position_correct_edge()
                self.execute(['R', 'U', 'R\'', 'F\'', 'R', 'U', 'R\'', 'U\'', 'R\'', 'F', 'R', 'R'])

    def count_correct_edges(self):
        count = 0
        edges = [
            ('F', 2, 1, 'G'),
            ('R', 2, 1, 'R'),
            ('B', 2, 1, 'B'),
            ('L', 2, 1, 'O')
        ]
        for face, r, c, expected_color in edges:
            if self.cube.cube[face][r][c] == expected_color:
                count += 1
        return count

    def position_correct_edge(self):
        edges = [
            ('F', 2, 1, 'G'),
            ('R', 2, 1, 'R'),
            ('B', 2, 1, 'B'),
            ('L', 2, 1, 'O')
        ]
        for face, r, c, expected_color in edges:
            if self.cube.cube[face][r][c] == expected_color:
                rotations_needed = {'F': 2, 'R': 3, 'B': 0, 'L': 1}[face]
                for _ in range(rotations_needed):
                    self.execute(['D'])
                break

def main():
    cube = RubiksCube()
    print("Solved Cube:")
    cube.display()
    scramble_moves = ["L'", "U'", "B2", "B", "L2", "B2", "B'", "B", "D'", "F"]
    cube.scramble(scramble_moves)
    print(f"Scramble Moves: {' '.join(scramble_moves)}")
    print("\nScrambled Cube:")
    cube.display()
    solver = RubiksCubeSolver(cube)
    solution = solver.solve()
    print(f"\nSolution in {len(solution)} moves:")
    print(" ".join(solution))
    print(f"\nIs cube solved? {cube.is_solved()}")

if __name__ == "__main__":
    main()