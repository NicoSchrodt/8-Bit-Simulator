from Code.Intel8080.Intel8080 import Intel8080

if __name__ == '__main__':
    processor = Intel8080()
    processor.init("""
    Mvi a, 10
    Mvi b, 0Ah
    Loop:
        Ana b""")

    # x = 0
    # while x < 49:
    #     x += 1
    #     print(processor.next_instruction())
    processor.run_complete_programm(5)
