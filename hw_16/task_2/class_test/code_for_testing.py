from hw_16.task_2.count_lines import count_lines
from hw_16.task_2.csv_manipulating import add_str, del_str

file = '../../task_2/file.csv'


class TestCountLines:
    def setup(self):
        print('\nStart our test')

    def test_add_line(self):
        start_str = count_lines(file)
        add_str(file, ['Max', 'Big', 50, 'Male', 18000])
        end_str = count_lines(file)
        assert end_str == start_str + 1

    def test_del_line(self):
        start_str = count_lines(file)
        del_str(file)
        end_str = count_lines(file)
        assert end_str == start_str - 1

    def teardown(self):
        print('\nEnd testing')
