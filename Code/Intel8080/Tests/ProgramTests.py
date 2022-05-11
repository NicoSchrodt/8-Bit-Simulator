from unittest import TestCase

from Code.Intel8080.Intel8080 import Intel8080


class ProgramTests(TestCase):

    def test_mvi(self):
        try:
            intel = Intel8080()
            intel.init_test("""
                              mvi b, 20
                              mvi c, 30
                              mov a, b
                              add c
                            """)

            intel.run_complete_programm(4)

            self.assertEqual(50, intel.get_acc())
        except:
            self.fail()