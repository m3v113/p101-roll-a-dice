import random

response = "y"

while response == "y":

    num = random.randint(1, 6)

    if num == 1:
        print("""
        [-----]
        [     ]
        [  *  ]
        [     ]
        [-----]
        """)

    elif num == 2:
        print("""
        [-----]
        [*    ]
        [     ]
        [    *]
        [-----]
        """)

    elif num == 3:
        print("""
        [-----]
        [*    ]
        [  *  ]
        [    *]
        [-----]
        """)

    elif num == 4:
        print("""
        [-----]
        [*   *]
        [     ]
        [*   *]
        [-----]
        """)

    elif num == 5:
        print("""
        [-----]
        [*   *]
        [  *  ]
        [*   *]
        [-----]
        """)

    elif num == 6:
        print("""
        [-----]
        [*   *]
        [*   *]
        [*   *]
        [-----]
        """)

    response = input("press y to roll and n to exit")
