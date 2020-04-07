import itertools

print(
    any(
        map(
            lambda x: int(x) == 0,
            list(
                map(
                    lambda x: input(),
                    range(
                        int(
                            input()
                        )
                    )
                )
            )
        )
    )
)


