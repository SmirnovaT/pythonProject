class Tetrapods:
    def __init__(self, head, legs):
        self.head = head
        self.legs = legs
        self.legs_quantiry = 4

        self.__heart = "heart"

    def move_head(self):
        print(f"кручу головой {self.head}")


class Cats(Tetrapods):
    def __init__(self, head, legs):
        super().__init__(head=head, legs=legs)

    def say_myau(self):
        print('myau')


class Dogs(Tetrapods):
    def __init__(self, head, legs):
        super().__init__(head=head, legs=legs)


matroskin = Cats("кошачья голова", "кошачьи ноги")
matroskin.move_head()
matroskin.say_myau()