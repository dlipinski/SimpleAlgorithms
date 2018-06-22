from Approximation import Approximation 


def main ():
    data = [
        [0,1],
        [1,4],
        [2,6],
        [3,2]
    ]
    approx = Approximation(2, data)
    print("A: ", approx.get_matrix())
    print("B: ", approx.get_t())
if __name__ == "__main__":
    main()