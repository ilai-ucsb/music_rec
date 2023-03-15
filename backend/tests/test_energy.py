from backend_imports import mock_db
from backend_imports import energy

"""
Test
test 10 songs, energy = .5, num = 6
expected return should 6 medium energy songs in increasing order by distance from .5
"""

def test():
    data = [mock_db.generateRandomRow(i) for i in range(10)]
    sorted_data = energy.getEnergy(data, 0.5, 6)

    for i in range(5):
        assert abs(sorted_data[i]["energy"] - 0.5) <= abs(
            sorted_data[i + 1]["energy"] - 0.5
        ), f"Distance from current ({sorted_data[i]['energy']}) is further from next ({sorted_data[i+1]['energy']})"
