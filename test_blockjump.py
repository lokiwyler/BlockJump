# test_blockjump.py
"""
Tests for BlockJump module.
"""

import unittest
from blockjump import BlockJump

class TestBlockJump(unittest.TestCase):
    """Test cases for BlockJump class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockJump()
        self.assertIsInstance(instance, BlockJump)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockJump()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
