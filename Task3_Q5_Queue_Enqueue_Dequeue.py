class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1

    def is_empty(self):
        return self.front > self.rear

    def is_full(self):
        return self.rear == self.capacity - 1

    def enqueue(self, x):
        if self.is_full():
            print(f"  Queue Overflow: cannot enqueue {x}")
            return False
        self.rear += 1
        self.items[self.rear] = x
        print(f"  {x} enqueued")
        return True

    def dequeue(self):
        if self.is_empty():
            print("  Queue Underflow: queue is empty")
            return None
        x = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        print(f"  {x} dequeued")
        if self.is_empty():              # queue empty again: reuse the whole array
            self.front, self.rear = 0, -1
        return x

    def peek(self):
        return None if self.is_empty() else self.items[self.front]

    def display(self):
        if self.is_empty():
            print("  Queue is empty")
        else:
            elements = self.items[self.front:self.rear + 1]
            print("  Front -> " + "  ".join(map(str, elements)) + " <- Rear")


def parse(text):
    """Store whole numbers as int, anything else as text."""
    text = text.strip()
    try:
        return int(text)
    except ValueError:
        return text


def main():
    raw = input("Enter queue capacity (press Enter for 5): ").strip()
    capacity = int(raw) if raw.isdigit() and int(raw) > 0 else 5
    q = Queue(capacity)
    print(f"Queue of capacity {capacity} created.")

    while True:
        print("\n------ QUEUE MENU ------")
        print("1. Enqueue (insert)")
        print("2. Dequeue (delete)")
        print("3. Display queue")
        print("4. Peek (front element)")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            value = input("  Enter the value to enqueue: ")
            if value.strip() == "":
                print("  Nothing entered.")
            else:
                q.enqueue(parse(value))
        elif choice == "2":
            q.dequeue()
        elif choice == "3":
            q.display()
        elif choice == "4":
            front = q.peek()
            print("  Queue is empty" if q.is_empty() else f"  Front element = {front}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("  Invalid choice, try again.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram ended.")
