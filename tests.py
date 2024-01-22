import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells), 
            num_cols,
            )
        self.assertEqual(
            len(m1._cells[0]), 
            num_rows
            )
        
    def test_maze_2rows_15cols(self):
        num_cols = 15
        num_rows = 2
        m2 = Maze(20, 20, num_rows, num_cols, 5, 20)
        self.assertEqual(
            len(m2._cells),
            num_cols,
            )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows
            )
        
    def test_maze_20rows_100cols(self):
        num_cols = 100
        num_rows = 20
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m3._cells),
            num_cols,
            )
        self.assertEqual(
            len(m3._cells[0]),
            num_rows
            )
        
    def test_entrance_exit_break(self):
        num_cols = 10
        num_rows = 10
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m4._cells), 
            num_cols,
            )
        self.assertEqual(
            len(m4._cells[0]), 
            num_rows
            )
        
        if m4._cells[0][0].has_top_wall:
            print("Failed to break entrance")

        if m4._cells[-1][-1].has_bottom_wall:
            print("Failed to break exit")
        
    def test_reset_visited(self):
        num_cols = 5
        num_rows = 5
        m5 = Maze(0, 0, num_rows, num_cols, 10, 10)
        #m5._cells[2][2].visited = True
        
        for col in m5._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )
    
        
if __name__ == "__main__":
    unittest.main()
    
    