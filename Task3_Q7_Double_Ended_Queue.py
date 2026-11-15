class Deque:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # a. Front insertion ------------------------------------------------------
    def insert_front(self, x):
        if self.is_full():
            print(f"  Deque Overflow: cannot insert {x} at the front")
            return False
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1) % self.size
        self.items[self.front] = x
        print(f"  {x} inserted at the front")
        return True

    # b. Rear insertion -------------------------------------------------------
    def insert_rear(self, x):
        if self.is_full():
            print(f"  Deque Overflow: cannot insert {x} at the rear")
            return False
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = x
        print(f"  {x} inserted at the rear")
        return True

    # c. Front deletion -------------------------------------------------------
    def delete_front(self):
        if self.is_empty():
            print("  Deque Underflow: deque is empty")
            return None
        x = self.items[self.front]
        self.items[self.front] = None
        if self.front == self.rear:      # last element removed
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"  {x} deleted from the front")
        return x

    # d. Rear deletion --------------------------------------------------------
    def delete_rear(self):
        if self.is_empty():
            print("  Deque Underflow: deque is empty")
            return None
        x = self.items[self.rear]
        self.items[self.rear] = None
        if self.front == self.rear:      # last element removed
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.size
        print(f"  {x} deleted from the rear")
        return x

    def display(self):
        if self.is_empty():
            print("  Deque is empty")
            return
        out, i = [], self.front
        while True:
            out.append(self.items[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print("  Front -> " + "  ".join(map(str, out)) + " <- Rear")
        print(f"  (array = {self.items}, front = {self.front}, rear = {self.rear})")


def parse(text):
    """Store whole numbers as int, anything else as text."""
    text = text.strip()
    try:
        return int(text)
    except ValueError:
        return text


def main():
    raw = input("Enter deque size (press Enter for 5): ").strip()
    size = int(raw) if raw.isdigit() and int(raw) > 0 else 5
    dq = Deque(size)
    print(f"Deque of size {size} created.")

    while True:
        print("\n------ DEQUE MENU ------")
        print("1. Insert at front")
        print("2. Insert at rear")
        print("3. Delete from front")
        print("4. Delete from rear")
        print("5. Display deque")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice in ("1", "2"):
            value = input("  Enter the value: ")
            if value.strip() == "":
                print("  Nothing entered.")
            elif choice == "1":
                dq.insert_front(parse(value))
            else:
                dq.insert_rear(parse(value))
        elif choice == "3":
            dq.delete_front()
        elif choice == "4":
            dq.delete_rear()
        elif choice == "5":
            dq.display()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("  Invalid choice, try again.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram ended.")