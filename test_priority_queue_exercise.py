import unittest

from priority_queue_exercise import process_priority_queue


class ProcessPriorityQueueTests(unittest.TestCase):
    def test_push_and_pop_returns_values_in_priority_order(self) -> None:
        operations = [
            ("push", 5),
            ("push", 1),
            ("push", 3),
            ("pop", 0),
            ("pop", 0),
            ("pop", 0),
        ]

        self.assertEqual(process_priority_queue(operations), [1, 3, 5])

    def test_pop_on_empty_queue_is_ignored(self) -> None:
        operations = [("pop", 0), ("push", 2), ("pop", 0)]

        self.assertEqual(process_priority_queue(operations), [2])


if __name__ == "__main__":
    unittest.main()
