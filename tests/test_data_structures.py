import pytest
from data_structures import *
from unittest.mock import patch

# Question 1

@pytest.mark.parametrize("readings, expected_hours, expected_temps", [
    ([(6, 4), (12, 18), (18, 11)], [6, 12, 18], [4, 18, 11]),
    ([(9, 15)], [9], [15]),
    ([], [], []),
    ([(0, -3.5), (1, -4.2)], [0, 1], [-3.5, -4.2]),
    ([(5, 7), (5, 7)], [5, 5], [7, 7])
])
def test_split_readings_logic(readings, expected_hours, expected_temps):
    hours, temps = split_readings(readings)
    assert hours == expected_hours
    assert temps == expected_temps

def test_split_readings_integrity():
    input_data = [(i, i * 2) for i in range(100)]
    hours, temps = split_readings(input_data)

    assert len(hours) == len(input_data)
    assert len(temps) == len(input_data)

    assert hours[40] == 40
    assert temps[40] == 80

def test_split_readings_invalid_tuple_size():
    bad_input = [(6, 4), (12, 18, 20)]
    with pytest.raises(ValueError):
        split_readings(bad_input)

def test_split_readings_non_iterable_element():
    bad_input = [(6, 4), 12]
    with pytest.raises(TypeError):
        split_readings(bad_input)

def test_split_readings_large_dataset():
    large_input = [(i, i) for i in range(100000)]
    hours, temps = split_readings(large_input)
    assert len(hours) == 100000
    assert temps[99999] == 99999

def test_split_readings_single_reading():
    assert split_readings([(8, 12)]) == ([8], [12])

def test_split_readings_multiple_readings():
    assert split_readings([(6, 4), (12, 18), (18, 11)]) == ([6, 12, 18], [4, 18, 11])

def test_split_readings_multiple_readings_2():
    assert split_readings([(1, 10), (2, 20), (3, 30), (4, 40)]) == ([1, 2, 3, 4], [10, 20, 30, 40])

def test_split_readings_negative_temps():
    assert split_readings([(2, -1), (3, -5), (4, -9)]) == ([2, 3, 4], [-1, -5, -9])

def test_split_readings_mixed_temps():
    assert split_readings([(0, 0), (1, -1), (2, 1)]) == ([0, 1, 2], [0, -1, 1])

# ------------------------------------------------------------------------------------------ # ------------------------------------------------------------------------------------------ #

# Question 2

@pytest.mark.parametrize("passengers, expected_dict", [
    (["Naledi", "Pieter", "Zodwa"], {"Naledi": 0, "Pieter": 1, "Zodwa": 2}),
    ([], {}),
    (["Solo"], {"Solo": 0}),
    (["bongani", "Bongani"], {"bongani": 0, "Bongani": 1}),
])
def test_create_seat_lookup_logic(passengers, expected_dict):
    assert create_seat_lookup(passengers) == expected_dict

def test_create_seat_lookup_duplicates():
    names = ["Anele", "Bheki", "Anele"]
    result = create_seat_lookup(names)

    assert result["Anele"] == 2
    assert len(result) == 2

def test_create_seat_lookup_large_scale():
    large_names = [f"Passenger_{i}" for i in range(100000)]
    result = create_seat_lookup(large_names)

    assert len(result) == 100000
    assert result["Passenger_99999"] == 99999

def test_create_seat_lookup_unhashable_type():
    bad_data = ["Anele", ["I", "am", "unhashable"]]
    with pytest.raises(TypeError):
        create_seat_lookup(bad_data)

def test_create_seat_lookup_single_name():
    assert create_seat_lookup(['Lindiwe']) == {'Lindiwe': 0}

def test_create_seat_lookup_duplicate_names():
    assert create_seat_lookup(['Thabo', 'Amy', 'Thabo']) == {'Thabo': 2, 'Amy': 1}

# ------------------------------------------------------------------------------------------ # ------------------------------------------------------------------------------------------ #

# Question 3

@pytest.mark.parametrize("input_posts, expected_set", [
    (["Jazz", "jazz", "JaZz"], {"jazz"}),
    (["Amapiano", "House", "Gqom"], {"amapiano", "house", "gqom"}),
    ([], set()),
    (["Web3", "dot-net"], {"web3", "dot-net"}),
])
def test_extract_unique_hashtags_logic(input_posts, expected_set):
    assert extract_unique_hashtags(input_posts) == expected_set

def test_extract_unique_hashtags_large_dataset():
    large_input = (["TagA"] * 50000) + ([" taga "] * 50000)
    result = extract_unique_hashtags(large_input)
    assert len(result) == 1
    assert "taga" in result

def test_extract_unique_hashtags_example():
    input_posts = ['  Amapiano', 'amapiano ', 'JAZZ', 'Jazz', 'Braai', ' braai', '']
    expected_output = {'amapiano', 'jazz', 'braai'}
    assert extract_unique_hashtags(input_posts) == expected_output

def test_extract_unique_hashtags_no_duplicates():
    input_posts = ['Java', 'C++', 'Ruby']
    expected_output = {'java', 'c++', 'ruby'}
    assert extract_unique_hashtags(input_posts) == expected_output

def test_extract_unique_hashtags_all_duplicates():
    input_posts = ['Tag', 'tag', 'TAG', 'tAg']
    expected_output = {'tag'}
    assert extract_unique_hashtags(input_posts) == expected_output

def test_extract_unique_hashtags_mixed_case():
    input_posts = ['Hello', 'WORLD', 'hello', 'world', 'HeLLo']
    expected_output = {'hello', 'world'}
    assert extract_unique_hashtags(input_posts) == expected_output

def test_extract_unique_hashtags_whitespace_stripped():
    assert extract_unique_hashtags(['  music', 'music  ', '\tmusic\n']) == {'music'}

def test_extract_unique_hashtags_blank_entries_ignored():
    assert extract_unique_hashtags(['', '   ', '\t', 'live']) == {'live'}

def test_extract_unique_hashtags_only_blanks():
    assert extract_unique_hashtags(['', ' ', '  ']) == set()

# ------------------------------------------------------------------------------------------ # ------------------------------------------------------------------------------------------ #

# Question 4

@pytest.mark.parametrize("books, expected", [
    (
        [
            {"title": "Cry, the Beloved Country", "genre": "Fiction"},
            {"title": "Long Walk to Freedom", "genre": "Biography"},
            {"title": "Spud", "genre": "Fiction"},
            {"title": "Born a Crime", "genre": "Biography"},
            {"title": "Braai Master", "genre": "Cookbook"}
        ],
        {
            "Fiction": ["Cry, the Beloved Country", "Spud"],
            "Biography": ["Long Walk to Freedom", "Born a Crime"],
            "Cookbook": ["Braai Master"]
        }
    ),
    (
        [
            {"title": "Algebra 1", "genre": "Maths"},
            {"title": "Calculus", "genre": "Advanced Maths"},
            {"title": "Geometry", "genre": "Maths"}
        ],
        {"Maths": ["Algebra 1", "Geometry"], "Advanced Maths": ["Calculus"]}
    ),
    (
        [
            {"title": "Python Basics", "genre": "Programming"},
            {"title": "Clean Code", "genre": "Software Design"},
            {"title": "Fluent Python", "genre": "Programming"}
        ],
        {"Programming": ["Python Basics", "Fluent Python"], "Software Design": ["Clean Code"]}
    ),
    ([], {}),
    (
        [{"title": "Atlas", "genre": "Reference"}],
        {"Reference": ["Atlas"]}
    ),
    (
        [
            {'title': 'Dune', 'genre': 'SciFi'},
            {'title': 'Emma', 'genre': 'Romance'},
            {'title': 'Neuromancer', 'genre': 'SciFi'},
            {'title': 'Persuasion', 'genre': 'Romance'},
            {'title': 'Jaws', 'genre': 'Thriller'}
        ],
        {'SciFi': ['Dune', 'Neuromancer'], 'Romance': ['Emma', 'Persuasion'], 'Thriller': ['Jaws']}
    )
])
def test_group_by_genre_logic(books, expected):
    assert group_by_genre(books) == expected

def test_group_by_genre_missing_keys():
    with pytest.raises(KeyError):
        group_by_genre([{"title": "Untitled Shelf Item"}])

def test_group_by_genre_non_dict_elements():
    with pytest.raises(TypeError):
        group_by_genre([None])

def test_group_by_genre_integrity():
    books = [{"title": "Atlas", "genre": "Reference"}]
    result = group_by_genre(books)
    assert isinstance(result["Reference"], list)
    assert len(result["Reference"]) == 1

def test_group_by_genre_large_input():
    books = [{"title": f"Volume_{i}", "genre": "Encyclopedia"} for i in range(5000)]
    result = group_by_genre(books)
    assert len(result["Encyclopedia"]) == 5000
    assert result["Encyclopedia"][0] == "Volume_0"

def test_group_by_genre_alternative():
    books = [
        {'title': 'Salt', 'genre': 'Poetry'},
        {'title': 'Rain', 'genre': 'Poetry'},
        {'title': 'Dust', 'genre': 'Essays'}
    ]
    expected_output = {
        'Poetry': ['Salt', 'Rain'],
        'Essays': ['Dust']
    }
    assert group_by_genre(books) == expected_output

# ------------------------------------------------------------------------------------------ # ------------------------------------------------------------------------------------------ #

# Question 5

@pytest.mark.parametrize("input_ids, expected_output", [
    (['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9'], [['P1', 'P2', 'P3', 'P4'], ['P5', 'P6', 'P7', 'P8'], ['P9']]),
    (['P1', 'P2', 'P3', 'P4'], [['P1', 'P2', 'P3', 'P4']]),
    ([], []),
    (['P1', 'P2'], [['P1', 'P2']]),
    (['1', '2', '3', '4', '5'], [['1', '2', '3', '4'], ['5']]),
])
def test_batch_parcel_dispatcher_logic(input_ids, expected_output):
    assert batch_parcel_dispatcher(input_ids) == expected_output

def test_batch_parcel_dispatcher_immutability():
    original = ['A', 'B', 'C', 'D', 'E', 'F']
    original_copy = original.copy()

    batch_parcel_dispatcher(original)

    assert original == original_copy, "The input list was mutated during batching!"

def test_batch_parcel_dispatcher_large_scale():
    large_input = [f"P{i}" for i in range(10000)]
    result = batch_parcel_dispatcher(large_input)

    assert len(result) == 2500
    assert len(result[0]) == 4
    assert result[-1][-1] == "P9999"

def test_batch_parcel_dispatcher_non_list_iterable():
    input_tuple = ('P1', 'P2', 'P3', 'P4', 'P5')
    expected = [['P1', 'P2', 'P3', 'P4'], ['P5']]

    assert batch_parcel_dispatcher(input_tuple) == expected

def test_batch_parcel_dispatcher_returns_lists():
    result = batch_parcel_dispatcher(('P1', 'P2', 'P3', 'P4', 'P5'))
    assert all(isinstance(trip, list) for trip in result)

def test_batch_parcel_dispatcher_single_parcel():
    assert batch_parcel_dispatcher(['P1']) == [['P1']]

def test_batch_parcel_dispatcher_multiple_trips():
    assert batch_parcel_dispatcher(['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']) == [['P1', 'P2', 'P3', 'P4'], ['P5', 'P6', 'P7']]

def test_batch_parcel_dispatcher_exact_multiple():
    assert batch_parcel_dispatcher(['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']) == [['P1', 'P2', 'P3', 'P4'], ['P5', 'P6', 'P7', 'P8']]

def test_batch_parcel_dispatcher_mixed_ids():
    assert batch_parcel_dispatcher(['P10', 'P5', 'P3', 'P8', 'P1', 'P7']) == [['P10', 'P5', 'P3', 'P8'], ['P1', 'P7']]

def test_batch_parcel_dispatcher_large_number_of_trips():
    parcel_ids = [f'P{i}' for i in range(1, 21)]
    expected_output = [
        ['P1', 'P2', 'P3', 'P4'],
        ['P5', 'P6', 'P7', 'P8'],
        ['P9', 'P10', 'P11', 'P12'],
        ['P13', 'P14', 'P15', 'P16'],
        ['P17', 'P18', 'P19', 'P20']
    ]
    assert batch_parcel_dispatcher(parcel_ids) == expected_output

def test_batch_parcel_dispatcher_fewer_than_van_capacity():
    assert batch_parcel_dispatcher(['P1', 'P2', 'P3']) == [['P1', 'P2', 'P3']]

def test_batch_parcel_dispatcher_never_exceeds_capacity():
    result = batch_parcel_dispatcher([f"P{i}" for i in range(103)])
    assert all(len(trip) <= 4 for trip in result)

# ------------------------------------------------------------------------------------------ # ------------------------------------------------------------------------------------------ #

# Question 6

@pytest.mark.parametrize("driver_routes, expected_drivers", [
    (
        {"Themba": ["Bree", "Noord"], "Zanele": ["Noord"]},
        {"Bree": ["Themba"], "Noord": ["Themba", "Zanele"]}
    ),
    (
        {"DriverA": ["RankB"], "DriverB": ["RankA"]},
        {"RankB": ["DriverA"], "RankA": ["DriverB"]}
    ),
    ({}, {}),
    (
        {"Themba": [], "Zanele": ["Bree"]},
        {"Bree": ["Zanele"]}
    ),
    (
        {"A": ["X"], "B": ["X"], "C": ["X"]},
        {"X": ["A", "B", "C"]}
    )
])
def test_taxi_rank_inverter_logic(driver_routes, expected_drivers):
    assert taxi_rank_inverter(driver_routes) == expected_drivers

def test_taxi_rank_inverter_immutability():
    original = {"Themba": ["Bree"]}
    original_copy = {"Themba": ["Bree"]}
    taxi_rank_inverter(original)
    assert original == original_copy

def test_taxi_rank_inverter_non_iterable_value():
    with pytest.raises(TypeError):
        taxi_rank_inverter({"Themba": None})

def test_taxi_rank_inverter_large_star_graph():
    star_graph = {f"Driver{i}": ["Central"] for i in range(10000)}
    result = taxi_rank_inverter(star_graph)

    assert len(result["Central"]) == 10000
    assert "Driver9999" in result["Central"]

def test_taxi_rank_inverter_duplicate_rank():
    duplicate_route = {"Themba": ["Bree", "Bree"]}
    result = taxi_rank_inverter(duplicate_route)

    assert result == {"Bree": ["Themba"]}

def test_taxi_rank_inverter_preserves_driver_order():
    routes = {"Zanele": ["Noord"], "Themba": ["Noord"], "Alfred": ["Noord"]}
    assert taxi_rank_inverter(routes) == {"Noord": ["Zanele", "Themba", "Alfred"]}

def test_taxi_rank_inverter_referential_integrity():
    data = {"Themba": ["Bree"]}
    result = taxi_rank_inverter(data)
    result["Bree"].append("Zanele")

    assert "Zanele" not in taxi_rank_inverter(data)["Bree"]

# ------------------------------------------------------------------------------------------ # ------------------------------------------------------------------------------------------ #

# Question 7

@pytest.mark.parametrize("n, expected_output", [
    (0, []),
    (1, [1]),
    (2, [1, 1]),
    (5, [1, 1, 2, 6, 24]),
    (10, [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880])
])

def test_factorial_sequence_logic(n, expected_output):
    assert factorial_sequence(n) == expected_output

def test_factorial_sequence_large_n():
    result = factorial_sequence(20)
    assert len(result) == 20
    assert result[-1] == 121645100408832000

def test_factorial_sequence_zero_and_one():
    assert factorial_sequence(0) == []
    assert factorial_sequence(1) == [1]

def test_factorial_sequence_negative_n():
    with pytest.raises(ValueError):
        factorial_sequence(-5)

def test_factorial_sequence_non_integer_n():
    with pytest.raises(ValueError):
        factorial_sequence(5.5)

def test_factorial_sequence_integrity():
    result = factorial_sequence(20)
    assert result[0] == 1
    assert result[1] == 1
    assert result[2] == 2
    assert result[3] == 6
    assert result[4] == 24

def test_factorial_sequence_edge_cases():
    assert factorial_sequence(2) == [1, 1]
    assert factorial_sequence(3) == [1, 1, 2]
    assert factorial_sequence(4) == [1, 1, 2, 6]

def test_is_recursion_implemented():

    with patch("data_structures.factorial_sequence", wraps=factorial_sequence) as mocked_function:
        mocked_function(10)

        assert mocked_function.call_count > 1, f"Recursion not detected. Count: {mocked_function.call_count}"

def test_recursion_depth():
    depth = 2000
    with pytest.raises(RecursionError):
        factorial_sequence(depth)

def test_recursion_parameters():
    with patch("data_structures.factorial_sequence", wraps=factorial_sequence) as mocked_function:
        mocked_function(5)

        for call in mocked_function.call_args_list:
            args, _ = call
            assert len(args) == 1, "Recursive calls should have exactly one argument."
            assert isinstance(args[0], int), "Recursive call argument should be an integer."
