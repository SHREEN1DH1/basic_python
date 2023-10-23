picture = [[0,0,0,1,0,0,0],
          [0,0,1,1,1,0,0],
          [0,1,1,1,1,1,0],
          [1,1,1,1,1,1,1],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0]
        ]

# print ' ' if 0 or 8 if 1
for image in picture:
    for pixel in image:
        if (pixel==1):
            print('*',end='')
        else:
            print(' ',end='')
    print('')