from functools import reduce

a = 1
print(
    reduce(
        min,
        list(
            filter(
                lambda x: int(x) % 2,
                map(
                    int,
                    input().split()
                )
            )
        )
    )
)

