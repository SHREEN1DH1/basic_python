while True:
    try:
        jno=int(input('enter your jersey number'))
        print(jno)
        # raise ValueError('hey stop it')#using raise helps us to have our own error message
    except:
        print('please enter a number')
    else:
        print('Thanks')
        break
    # finally:   #finally works at the end no matter what the outcome is
    #     print('i am done')

