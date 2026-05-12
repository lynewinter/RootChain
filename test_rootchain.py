# test_rootchain.py
"""
Tests for RootChain module.
"""

import unittest
from rootchain import RootChain

class TestRootChain(unittest.TestCase):
    """Test cases for RootChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RootChain()
        self.assertIsInstance(instance, RootChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RootChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
