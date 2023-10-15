from Vec2D import Vec2D

class Grid:

    def __init__(self, cell_size: int, window_width: int, window_height: int):
        self.cell_size = cell_size
        # grid dimensions
        self.width = window_width // cell_size
        self.height = window_height // cell_size
        self.cells = self.generate_cells()

    def generate_cells(self):

        cells = []
        for i in range(self.height * self.width):
            cells.append([])
        return cells
    
    def position_to_cell(self, pos: Vec2D):
        # print(f'pos: ({pos.x}, {pos.y})')
        # print(f'y_cell_idx: {pos.y // self.cell_size}, x_cell_idx: {pos.x // self.cell_size}')
        return int(pos.y // self.cell_size) + int(pos.x // self.cell_size * self.height)
    
    def partition_objects(self, objects: list):
        for object in objects:
            cell_idx = self.position_to_cell(pos=object.pos)
            self.cells[cell_idx].append(object)

    def to_string(self):
        print(f'Cell size: {self.cell_size}')
        print(f'Cell count: {len(self.cells)}')
        print(f'Grid dimensions: w: {self.width}, h: {self.height}')
        
        # print cells row by row, from top
        row = []
        for i in range(self.height-1, -1, -1):
                              # indices of final column + 1
            for j in range(i, self.height*(self.width-1)+i+1, self.height):
                row.append(self.cells[j])
            print(row)
            row = []
