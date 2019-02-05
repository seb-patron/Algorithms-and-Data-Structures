def minimumBribes(arr):

    bribes =0
    for i in range(0, len(arr)):
        if arr[i] - (i+1) > 2:
            print ("Too chaotic")
            return

        for j in range(max(0, arr[i]-2), i):
            if arr[j] > arr[i]:
                bribes +=1

    print (bribes)