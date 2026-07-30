# test_chainsync.py
"""
Tests for ChainSync module.
"""

import unittest
from chainsync import ChainSync

class TestChainSync(unittest.TestCase):
    """Test cases for ChainSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainSync()
        self.assertIsInstance(instance, ChainSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
