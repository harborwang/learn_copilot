import unittest
from datetime import date
from learn_copilot_exp2 import Person

class TestPerson(unittest.TestCase):
    
    def setUp(self):
        self.person1 = Person("John", "Doe", date(2000, 1, 1))
        self.person2 = Person("Jane", "Smith", date(1995, 5, 15))
        self.person3 = Person("Alice", "Jones", date(1980, 11, 30))
    
    def test_full_name(self):
        self.assertEqual(self.person1.full_name, "John Doe")
        self.assertEqual(self.person2.full_name, "Jane Smith")
        self.assertEqual(self.person3.full_name, "Alice Jones")
    
    def test_age(self):
        current_year = date.today().year
        self.assertEqual(self.person1.age(), current_year - 2000)
        self.assertEqual(self.person2.age(), current_year - 1995)
        self.assertEqual(self.person3.age(), current_year - 1980)

if __name__ == '__main__':
    unittest.main()