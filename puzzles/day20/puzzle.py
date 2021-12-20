import numpy as np

def read_input():
    with open("input.txt", "r") as file:
        tbl = np.array([c for c in file.readline()[:-1]])
        img = np.array([[p for p in l] for l in file.read().splitlines()[1:]])
        return tbl, img

def main(steps):
    tbl, img = read_input()
    tbl[tbl=="."] = 0
    tbl[tbl=="#"] = 1
    img[img=="."] = 0
    img[img=="#"] = 1

    for i in range(steps):
        h,w = img.shape
        nimg = np.zeros(np.add(img.shape, (2,2)))
        for y in range(-1,h+1):
            for x in range(-1,w+1):
                n = []
                for yy in range(y-1,y+2):
                    for xx in range(x-1,x+2):
                        if 0 <= yy < h and 0 <= xx < w:
                            nn = int(img[yy,xx])
                        else:
                            nn = i%2
                        n+=[str(nn)]
                nimg[y+1,x+1] = tbl[int("".join(n), 2)]

        img = nimg

    print((img).sum())        

if __name__ == "__main__":
    main(2)
    main(50)