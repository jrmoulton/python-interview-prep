""" You have a very large square wall and a circular dartboard placed on the
wall. You have been challenged to throw darts into the board blindfolded. Darts
thrown at the wall are represented as an array of points on a 2D plane. 

Return the maximum number of points that are within or lie on any circular
dartboard of radius r. """

def numPoints(points: list[list[int]], r: int) -> int:
    total = 0
    coords: list[float] = [0,0]
    correct_pairs: list[list[int]] = []
    for pair in points:
        coords[0] += pair[0]
        coords[1] += pair[1]
    coords[0] /= len(points)
    coords[1] /= len(points)
    for pair in points:
        if ((pair[0] - coords[0])**2 + (pair[1] - coords[1])**2)**(1/2) <= r:
            correct_pairs += pair
            total += 1;
    print(correct_pairs)
    return total

def test_numPoints():
    assert numPoints(points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5) == 5
    assert numPoints(points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1) == 1
    assert numPoints(points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2) == 4




