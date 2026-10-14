# ============================
# Question 1
# ============================
def split_readings(readings: list) -> tuple:
    hours = []
    temperatures = []

    for hour, temperature in readings:
        hours.append(hour)
        temperatures.append(temperature)

    return (hours, temperatures)


# ============================
# Question 2
# ============================
def create_seat_lookup(passengers: list) -> dict:
    return {name: seat for seat, name in enumerate(passengers)}


# ============================
# Question 3
# ============================
def extract_unique_hashtags(posts: list) -> set:
    return {post.strip().lower() for post in posts if post.strip()}


# ============================
# Question 4
# ============================
def group_by_genre(books: list) -> dict:
    shelves = {}

    for book in books:
        title = book["title"]
        genre = book["genre"]

        if genre not in shelves:
            shelves[genre] = []
        shelves[genre].append(title)

    return shelves


# ============================
# Question 5
# ============================
def batch_parcel_dispatcher(parcel_ids: list | tuple) -> list:
    trips = []

    for i in range(0, len(parcel_ids), 4):
        trips.append(list(parcel_ids[i:i + 4]))

    return trips


# ============================
# Question 6
# ============================
def taxi_rank_inverter(driver_routes: dict) -> dict:
    drivers_per_rank = {}

    for driver, ranks in driver_routes.items():
        for rank in dict.fromkeys(ranks):
            if rank not in drivers_per_rank:
                drivers_per_rank[rank] = []
            drivers_per_rank[rank].append(driver)

    return drivers_per_rank


# ============================
# Question 7
# ============================
def factorial_sequence(n: int) -> list:
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return []

    if n == 1:
        return [1]

    previous = factorial_sequence(n - 1)
    return previous + [previous[-1] * (n - 1)]
