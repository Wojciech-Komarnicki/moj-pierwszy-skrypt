import numpy as np
try:
    array = np.array([[['A', 'B', 'C'],['D', 'E', 'F'], ['G', 'H', 'I']],
                     [['J', 'K', 'L'], ['M', 'N', 'O'],  ['P', 'Q', 'R']],
                     [['S', 'T', 'U'], ['V', 'W', 'X'],['Y', 'Z', ' ']]])

    print(array.ndim)
    print(array.shape)
    print(array.size)
    word = array[1,1,0] + array[0,1,1] + array[0,2,0]+array[0,0,0]+array[1,1,1]
    print(word)

except Exception as e:
    print(e)