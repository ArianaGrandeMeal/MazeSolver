import unittest, time
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
        
        
    def test_entrance_exit_break(self):
        num_cols = 10
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
        
        if m1._cells[0][0].has_top_wall:
            print("Failed to break entrance")

        if m1._cells[-1][-1].has_bottom_wall:
            print("Failed to break exit")
        
    def test_reset_visited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )
        print("All cells successfully reset.  Rechecking with forced error.")

        # sleep for 2 seconds to allow user to verify correct function, then set one
        # cell's visited property to True and rerun test to force failure and double 
        # verify that method works correctly.
        time.sleep(2)
        m1._cells[2][2].visited = True
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )
        
if __name__ == "__main__":
    unittest.main()
    
    