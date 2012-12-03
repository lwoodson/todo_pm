import unittest
from should_dsl import should

class InitializeCommandSpec(unittest.TestCase):
    def it_should_create_a_passed_directory_if_none_exists(self):
        pass

    def ensure_existing_todo_files_are_not_overwritten(self):
        pass 

    def it_should_create_a_TODO_file_in_the_passed_directory(self):
        True |should| equal_to(True)

    def must_populate_the_generated_TODO_file_with_appropriate_template_text(self):
        pass
