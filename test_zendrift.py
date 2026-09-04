# test_zendrift.py
"""
Tests for ZenDrift module.
"""

import unittest
from zendrift import ZenDrift

class TestZenDrift(unittest.TestCase):
    """Test cases for ZenDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZenDrift()
        self.assertIsInstance(instance, ZenDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZenDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
