from lc42_trapping_rain_water.answer import trap

def test_get_water_trapped__valid_elevation_coordinates__return_units_trapped_water():
    elevation_coordinates = [0,1,0,2,1,0,1,3,2,1,2,1]
    expected = 6

    actual = trap(elevation_coordinates)

    assert expected == actual