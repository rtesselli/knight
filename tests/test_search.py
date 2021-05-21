from knight.search import breadth_first_search


def example_neighbors(element):
    map_ = {
        'a': ['b', 'c'],
        'b': ['a', 'd', 'e'],
        'c': ['a', 'f', 'g', 'h'],
        'd': ['b'],
        'e': ['b', 'h'],
        'f': ['c'],
        'g': ['c'],
        'h': ['c', 'e']
    }
    return map_.get(element, [])


def test_breadth_first_search():
    assert list(breadth_first_search('a', 'a', example_neighbors)) == ['a']
    assert list(breadth_first_search('a', 'b', example_neighbors)) == ['a', 'b']
    assert list(breadth_first_search('a', 'h', example_neighbors)) == ['a', 'c', 'h']
    assert list(breadth_first_search('c', 'b', example_neighbors)) == ['c', 'a', 'b']
