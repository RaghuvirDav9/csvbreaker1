from click.testing import CliRunner
import list_instances
import unittest
import ast

"""This class represents methods for testing list_instances."""


class TestStringMethods(unittest.TestCase):
    """this function passes command line value 'running'
        and checks if the returned list of instances are in running state only."""

    def test_running(self):
        runner = CliRunner()
        result = runner.invoke(list_instances.listInstanceNameAWS, '--state running'.split())
        self.assertEqual(0, result.exit_code)
        sep = '\n'
        stripped = result.output.split(sep, 1)[0]
        running_instances_list = ast.literal_eval(stripped)
        for i in running_instances_list:
            self.assertEqual(i[2], 'running')
            print('running')

    """this function passes command line value 'stopped' 
            and checks if the returned list of instances are in stopped state only."""
    def test_stopped(self):
        runner = CliRunner()
        result = runner.invoke(list_instances.listInstanceNameAWS, '--state stopped'.split())
        self.assertEqual(0, result.exit_code)
        sep = '\n'
        stripped = result.output.split(sep, 1)[0]
        stopped_instances_list = ast.literal_eval(stripped)
        for i in stopped_instances_list:
            self.assertEqual(i[2], 'stopped')
            print('stopped')


if __name__ == '__main__':
    unittest.main()
