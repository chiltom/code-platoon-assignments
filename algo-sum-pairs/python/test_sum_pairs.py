from sum_pairs import sum_pairs
import pytest

def test_sum_pairs_none_found():
    assert sum_pairs([3, 1, 5, 8, 2], 27) == 'unable to find pairs'
    
def test_sum_pairs_one_found():
    assert sum_pairs([1, 2, 3, 4, 5], 9) == [4, 5]

def test_sum_pairs_multiple_found():
    assert sum_pairs([1, 2, 3, 4, 5], 7) == [[2, 5], [3, 4]]