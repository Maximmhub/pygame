import  os
import  sys
import pygame


def main():
    gg = open("1.txt", "r", encoding="utf_8_sig")
    def rr(gg):
        ggg = []
        for i in gg.readlines():
            i = i.split()
            if len(i) == 1:
                ggg.append(i[0])
            else:
                ggg.append(i[0])
                ggg.append(i[1])
        return ggg

    ggg = []
    def load_image(name, colorkey=None):
        fullname = os.path.join(name)
        image = pygame.image.load(fullname)
        return image

    def ppw(q, x, y, desk):
        if desk[x][y] == 0:
            if q[1] == y:
                if q[0] - x == 1:
                    return True
                if q[0] - x == 2 and q[0] == 6:
                    if desk[q[0] - 1][y] == 0:
                        return True
        else:
            if q[0] - x == 1:
                if q[1] - 1 == y or q[1] + 1 == y:
                    return True

    def ppb(q, x, y, desk):
        if desk[x][y] == 0:
            if q[1] == y:
                if q[0] - x == -1:
                    return True
                if q[0] - x == -2 and q[0] == 1:
                    if desk[q[0] + 1][y] == 0:
                        return True
        else:
            if q[0] - x == -1:
                if q[1] - 1 == y or q[1] + 1 == y:
                    return True

    def pl(q, x, y, desk):
        if q[0] == x:
            if q[1] < y:
                for i in range(q[1] + 1, y):
                    if desk[q[0]][i] != 0:
                        return False
                return True
            else:
                for i in range(y + 1, q[1]):
                    if desk[q[0]][i] != 0:
                        return False
                return True
        if q[1] == y:
            if q[0] < x:
                for i in range(q[0] + 1, x):
                    if desk[i][q[1]] != 0:
                        return False
                return True
            else:
                for i in range(x + 1, q[0]):
                    if desk[i][q[1]] != 0:
                        return False
                return True

    def ps(q, x, y, desk):
        if abs(q[0] - x) != abs(q[1] - y):
            return False
        if q[0] < x:
            if q[1] < y:
                for i in range(1, x - q[0]):
                    if desk[q[0] + i][q[1] + i] != 0:
                        return False
                return True
            else:
                for i in range(1, x - q[0]):
                    if desk[q[0] + i][q[1] - i] != 0:
                        return False
                return True
        else:
            if q[1] < y:
                for i in range(1, q[0] - x):
                    if desk[q[0] - i][q[1] + i] != 0:
                        return False
                return True
            else:
                for i in range(1, q[0] - x):
                    if desk[q[0] - i][q[1] - i] != 0:
                        return False
                return True

    def pk(q, x, y):
        if abs(q[0] - x) == 2 and abs(q[1] - y) == 1:
            return True
        if abs(q[0] - x) == 1 and abs(q[1] - y) == 2:
            return True

    def cha(q, desk3, desk, h, kordw, kordb):
        a = 0
        m = desk[q[0]][q[1]]
        desk[q[0]][q[1]] = 0
        aa = [a, []]
        for i in range(11):
            if a == 2:
                break
            if i == 0:
                for j in range(8 - q[0]):
                    if desk[q[0] + j][q[1]] == 0:
                        continue
                    if desk3[q[0] + j][q[1]] == h:
                        break
                    else:

                        if h == "w":
                            b = [lb, fb]
                        else:
                            b = [lw, fw]
                        if desk[q[0] + j][q[1]] in b:
                            a += 1
                            aa[1].append(("l", q[0] + j, q[1]))
                        break
            if i == 1:
                for j in range(q[0]):
                    if desk[q[0] - j][q[1]] == 0:
                        continue
                    if desk3[q[0] - j][q[1]] == h:
                        break
                    else:
                        if h == "w":
                            b = [lb, fb]
                        else:
                            b = [lw, fw]
                        if desk[q[0] - j][q[1]] in b:
                            a += 1
                            aa[1].append(("l", q[0] - j, q[1]))
                        break
            if i == 2:
                for j in range(8 - q[1]):
                    if desk[q[0]][q[1] + j] == 0:
                        continue
                    if desk3[q[0]][q[1] + j] == h:
                        break
                    else:

                        if h == "w":
                            b = [lb, fb]
                        else:
                            b = [lw, fw]
                        if desk[q[0]][q[1] + j] in b:
                            a += 1
                            aa[1].append(("l", q[0], q[1] + j))
                        break
            if i == 3:
                for j in range(q[1]):
                    if desk[q[0]][q[1] -j] == 0:
                        continue
                    if desk3[q[0]][q[1] -j] == h:
                        break
                    else:
                        if h == "w":
                            b = [lb, fb]
                        else:
                            b = [lw, fw]
                        if desk[q[0]][q[1] - j] in b:
                            a += 1
                            aa[1].append(("l", q[0], j))
                        break
            if i == 4:
                for j in range(min(q[0], q[1])):
                    if desk[q[0] - j][q[1] - j] == 0:
                        continue
                    else:
                        if desk3[q[0] - j][q[1] - j] == h:
                            break
                        else:
                            if h == "w":
                                b = [sb, fb]
                            else:
                                b = [sw, fw]
                            if desk[q[0] - j][q[1] - j] in b:
                                a += 1
                                aa[1].append(("d", q[0] - j, q[1] - j))
                            break
            if i == 5:
                for j in range(min(q[0], 8 - q[1])):
                    if desk[q[0] - j][q[1] + j] == 0:
                        continue
                    else:
                        if desk3[q[0] - j][q[1] + j] == h:
                            break
                        else:
                            if h == "w":
                                b = [sb, fb]
                            else:
                                b = [sw, fw]
                            if desk[q[0] - j][q[1] + j] in b:
                                a += 1
                                aa[1].append(("d", q[0] - j, q[1] + j))
                            break
            if i == 6:
                for j in range(min(8 - q[0], 8 - q[1])):
                    if desk[q[0] + j][q[1] + j] == 0:
                        continue
                    else:
                        if desk3[q[0] + j][q[1] + j] == h:
                            break
                        else:
                            if h == "w":
                                b = [sb, fb]
                            else:
                                b = [sw, fw]
                            if desk[q[0] + j][q[1] + j] in b:
                                a += 1
                                aa[1].append(("d", q[0] + j, q[1] + j))
                            break
            if i == 7:
                for j in range(min(8 - q[0], 8 - q[1])):
                    if desk[q[0] + j][q[1] - j] == 0:
                        continue
                    else:
                        if desk3[q[0] + j][q[1] - j] == h:
                            break
                        else:
                            if h == "w":
                                b = [sb, fb]
                            else:
                                b = [sw, fw]
                            if desk[q[0] + j][q[1] - j] in b:
                                a += 1
                                aa[1].append(("d", q[0] + j, q[1] - j))
                            break
            if i == 8:
                if h == "w":
                    b = [kb]
                else:
                    b = [kw]
                if q[0] + 2 < 8 and q[1] + 1 < 8 and desk[q[0] + 2][q[1] + 1] in b:
                    a += 1
                    aa[1].append(("k", q[0] + 2, q[1] + 1))

                if q[0] + 2 < 8 and q[1] - 1 > -1 and desk[q[0] + 2][q[1] - 1] in b:
                    a += 1
                    aa[1].append(("k". q[0] + 2, q[1] - 1))
                if q[0] + 1 < 8 and q[1] + 2 < 8 and desk[q[0] + 1][q[1] + 2] in b:
                    a += 1
                    aa[1].append(("k", q[0] + 1, q[1] + 2))
                if q[0] - 1 > -1 and q[1] + 2 < 8 and desk[q[0] - 1][q[1] + 2] in b:
                    a += 1
                    aa[1].append(("k", q[0] - 1, q[1] + 2))

                if q[0] - 2 > -1 and q[1] + 1 < 8 and desk[q[0] - 2][q[1] + 1] in b:
                    a += 1
                    aa[1].append(("k", q[0] - 2, q[1] + 1))
                if q[0] - 2 > -1 and q[1] - 1 > -1 and desk[q[0] - 2][q[1] - 1] in b:
                    a += 1
                    aa[1].append(("k", q[0] - 2, q[1] - 1))
                if q[0] + 1 < 8 and q[1] - 2 > -1 and desk[q[0] + 1][q[1] - 2] in b:
                    a += 1
                    aa[1].append(("k", q[0] + 1, q[1] - 2))
                if q[0] -1 > -1 and q[1] -2 > -1 and desk[q[0] - 1][q[1] - 2] in b:
                    a += 1
                    aa[1].append(("k", q[0] - 1, q[1] - 2))
            if i == 9:
                if h == "b":
                    if q[0] + 1 < 8 and q[1] - 1 > -1 and desk[q[0] + 1][q[1] - 1] == pw:
                        a += 1
                        aa[1].append(("p"))
                    if q[0] + 1 < 8 and q[1] + 1 < 8 and desk[q[0] + 1][q[1] + 1] == pw:
                        a += 1
                        aa[1].append(("p"))
                else:
                    if q[0] - 1 > -1 and q[1] - 1 > -1 and desk[q[0] - 1][q[1] - 1] == pb:
                        a += 1
                        aa[1].append(("p"))
                    if q[0] - 1 > -1 and q[1] + 1 < 8 and desk[q[0] - 1][q[1]  + 1] == pb:
                        a += 1
                        aa[1].append(("p"))
            if i == 10:
                if (abs(kordw[0] - kordb[0]) == 0 and abs(kordw[1] - kordb[1]) == 1) or (abs(kordw[0] - kordb[0]) == 1 and abs(kordw[1] - kordb[1]) == 1) or (abs(kordw[0] - kordb[0]) == 1 and abs(kordw[1] - kordb[1]) == 0):
                    a += 1
        aa[0] = a
        desk[q[0]][q[1]] = m
        return aa

    def kor(q, kord, ll, lr, kk):
        if (abs(kord[0] - q[0]) == 1 and abs(kord[1] - q[1]) == 1) or (abs(kord[0] - q[0]) == 1 and abs(kord[1] - q[1]) == 0) or (abs(kordw[0] - q[0]) == 0 and abs(kordw[1] - q[1]) == 1):
            return True
        if abs(kord[0] - q[0]) == 0 and kord[1] - q[1] == 2 and lr and kk:
            print(kord[1])
            return 11
        if abs(kord[0] - q[0]) == 0 and kord[1] - q[1] == -2 and ll and kk:
            return 2
        return False

    def mat(a, kor, desk3, desk, g, kordw, kordb):
        if kor[0] + 1 < 8 and kor[1] + 1 < 8:
            if cha([kor[0] + 1, kor[1] + 1], desk3, desk, g, kordw, kordb)[0] == 0 and desk[kor[0] + 1][kor[1] + 1] == 0:
                return False
        if kor[0] + 1 < 8:
            if cha([kor[0] + 1, kor[1]], desk3, desk, g, kordw, kordb)[0] == 0 and desk[kor[0] + 1][kor[1]] == 0:
                return False
        if kor[1] + 1 < 8:
            if cha([kor[0], kor[1] + 1], desk3, desk, g, kordw, kordb)[0] == 0 and desk[kor[0]][kor[1] + 1] == 0:
                return False
        if kor[0] + 1 < 8 and kor[1] - 1 > -1:
            if cha([kor[0] + 1, kor[1] - 1], desk3, desk, g, kordw, kordb)[0] == 0 and desk[kor[0] + 1][kor[1] - 1] == 0:
                return False
        if kor[1] - 1 > -1:
            if cha([kor[0], kor[1] - 1], desk3, desk, g, kordw, kordb)[0] == 0 and desk[kor[0]][kor[1] - 1] == 0:
                return False

        if kor[0] - 1 > -1 and kor[1] - 1 > -1:
            if cha([kor[0] - 1, kor[1] - 1], desk3, desk, g, kordw, kordb)[0] == 0 and desk[kor[0] - 1][kor[1] - 1] == 0:
                return False
        if kor[0] - 1 > -1:
            if cha([kor[0] - 1, kor[1]], desk3, desk, g, kordw, kordb)[0] == 0 and desk[kor[0] - 1][kor[1]] == 0:
                return False
        if kor[0] - 1 > -1 and kor[1] + 1 < 8:
            if cha([kor[0] - 1, kor[1] + 1], desk3, desk, g, kordw, kordb)[0] == 0 and desk[kor[0] - 1][kor[1] + 1] == 0:
                return False

        if a[0] == 1:
            if g == w:
                xx = "b"
            else:
                xx = "w"
            if cha([a[1][0][1], a[1][0][2]], desk3, desk, xx, kordw, kordb)[0] != 0:
                return False

            if a[1][0][0] == "l":
                def pl2(q, x, y, desk, z):
                    if q[0] == x:
                        if q[1] < y:
                            for i in range(q[1] + 1, y):
                                if cha([q[0], [i]], desk3, desk, z, kordw, kordb)[0] != 0:
                                    return False
                            return True
                        else:
                            for i in range(y + 1, q[1]):
                                if cha([q[0], [i]], desk3, desk, z, kordw, kordb)[0] != 0:
                                    return False
                            return True
                    if q[1] == y:
                        if q[0] < x:
                            for i in range(q[0] + 1, x):
                                if cha([[i], q[1]], desk3, desk, z, kordw, kordb)[0] != 0:
                                    return False
                            return True
                        else:
                            for i in range(x + 1, q[0]):
                                if cha([[i], q[1]], desk3, desk, z, kordw, kordb)[0]!= 0:
                                    return False
                            return True

                if a[1][0][0] == "d":
                    if 1==1:
                        for j in range(min(q[0], q[1])):
                            if cha([[i], q[1]], desk3, desk, z, kordw, kordb)[0] != 0:
                                return False
                            if desk[q[0] - j][q[1] - j] == 0:
                                continue
                            else:
                                if desk3[q[0] - j][q[1] - j] == h:
                                    break
                                else:
                                    if h == "w":
                                        b = [sb, fb]
                                    else:
                                        b = [sw, fw]
                                    if desk[q[0] - j][q[1] - j] in b:
                                        a += 1
                                        aa[1].append(("d", q[0] - j, q[1] - j))
                                    break
                    if i == 5:
                        for j in range(min(q[0], 8 - q[1])):
                            if desk[q[0] - j][q[1] + j] == 0:
                                continue
                            else:
                                if desk3[q[0] - j][q[1] + j] == h:
                                    break
                                else:
                                    if h == "w":
                                        b = [sb, fb]
                                    else:
                                        b = [sw, fw]
                                    if desk[q[0] - j][q[1] + j] in b:
                                        a += 1
                                        aa[1].append(("d", q[0] - j, q[1] + j))
                                    break
                    if i == 6:
                        for j in range(min(8 - q[0], 8 - q[1])):
                            if desk[q[0] + j][q[1] + j] == 0:
                                continue
                            else:
                                if desk3[q[0] + j][q[1] + j] == h:
                                    break
                                else:
                                    if h == "w":
                                        b = [sb, fb]
                                    else:
                                        b = [sw, fw]
                                    if desk[q[0] + j][q[1] + j] in b:
                                        a += 1
                                        aa[1].append(("d", q[0] + j, q[1] + j))
                                    break

                if not pl2([a[1][0][1], a[1][0][2]], kor[0], kor[1], desk, xx):
                    return False



        return True

    def rer(ii, pp):
        global d
        global text
        if ii >= len(pp):
            return desk
        a = pp[ii].split("-")
        d = 0
        text = ""
        if a[1][-1] == "+":
            if ii % 2 == 0:
                f1 = pygame.font.Font(None, 90)
                text = f1.render('Шах черным', True, "black")
                d = 2
            else:
                f1 = pygame.font.Font(None, 90)
                text = f1.render('Шах белым', True, "black")
                d = 2
        if a[1][-1] == "#":
            if ii % 2 == 0:
                f1 = pygame.font.Font(None, 90)
                text = f1.render('Мат черным', True, "black")
                d = 2
            else:
                f1 = pygame.font.Font(None, 90)
                text = f1.render('Мат белым', True, "black")
                d = 2
        if len(a[0]) > 2:
            a[0] = a[0][1:]
        if a == ["0", "0"]:
            if ii % 2 == 0:
                desk[7][5]  = desk[7][4]
                desk[7][4] = 0
                desk[7][6] = desk[7][7]
                desk[7][7] = 0
                desk3[7][5] = desk3[7][4]
                desk3[7][4] = 0
                desk3[7][6] = desk3[7][7]
                desk3[7][7] = 0
            else:
                desk[0][5] = desk[0][4]
                desk[0][4] = 0
                desk[0][6] = desk[0][7]
                desk[0][7] = 0
                desk3[0][5] = desk3[0][4]
                desk3[0][4] = 0
                desk3[0][6] = desk3[0][7]
                desk3[0][7] = 0
            return (desk, d, text)
        if a == ["0", "0", "0"]:
            if ii % 2 == 0:
                desk[7][2] = desk[7][4]
                desk[7][4] = 0
                desk[7][3] = desk[7][0]
                desk[7][0] = 0
                desk3[7][2] = desk3[7][4]
                desk3[7][4] = 0
                desk3[7][3] = desk3[7][0]
                desk3[7][0] = 0
            else:
                desk[0][2] = desk[0][4]
                desk[0][4] = 0
                desk[0][3] = desk[0][0]
                desk[0][0] = 0
                desk3[0][2] = desk3[0][4]
                desk3[0][4] = 0
                desk3[0][3] = desk3[0][0]
                desk3[0][0] = 0
            return (desk, d, text)







        y = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
        fq = desk[8 - int(a[0][1])][y[a[0][0]]]
        desk[8 - int(a[1][1])] = desk[8 - int(a[1][1])][:y[a[1][0]]] + [fq] + desk[8 - int(a[1][1])][y[a[1][0]] + 1:]
        desk[8 - int(a[0][1])][y[a[0][0]]] = 0
        desk3[8 - int(a[1][1])] = desk3[8 - int(a[1][1])][:y[a[1][0]]] + [desk3[8 - int(a[0][1])][y[a[0][0]]]] + desk3[8 - int(a[1][1])][y[a[1][0]] + 1:]
        desk3[8 - int(a[0][1])][y[a[0][0]]] = 0



        return (desk, d, text, desk3)

    def write(a, b, c, d):
        y = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
        a1 = 8 - a[0]
        b1 = 8 - b[0]
        a2 = y[a[1]]
        b2 = y[b[1]]
        if c == "П":
            c = ""
        ggg.append(c + a2 + str(a1) + "-" + b2 + str(b1) + str(d))

    def wr(ggg):
        gggg = open("2.txt", "w", encoding="utf_8_sig")
        for i in range(0, len(ggg), 2):
            if i + 1 == len(ggg):
                gggg.write(ggg[i])
            else:
                gggg.write(ggg[i] + " " + ggg[i + 1] + "\n")
        gggg.close()












    pygame.init()
    size = 800, 800
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    run = True
    kordb = [0, 4]
    kordw = [7, 4]
    desk2 = load_image("клетки.png")
    pw = load_image("пешка.png")
    sw = load_image("слонб.png")
    lw = load_image("ладьяб.png")
    fw = load_image("ферзьб.png")
    kow = load_image("корольб.png")
    kw = load_image("коньб.png")

    pb = load_image("пешкачч.png")
    sb = load_image("слонч.png")
    lb = load_image("ладьяч.png")
    fb = load_image("ферзь.png")
    kob = load_image("корольч.png")
    kb = load_image("коньч.png")

    desk = [[lb, kb, sb, fb, kob, sb, kb, lb], [pb, pb, pb, pb, pb, pb, pb, pb], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [pw, pw, pw, pw, pw, pw, pw, pw],[lw, kw, sw, fw, kow, sw, kw, lw]]
    b = "b"
    w = "w"
    desk3 = [[b, b, b, b, b, b, b, b], [b, b, b, b, b, b, b, b], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [w, w, w, w, w, w, w, w],[w, w, w, w, w, w, w, w]]
    q = (0, 0)
    h = w
    d = 0
    llw = True
    lrw = True
    llb = True
    lrb = True
    kkw = True
    kkb = True
    r = False
    ii = -1
    figura = ""
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEMOTION:
                x2, y2 = event.pos
                x2, y2 = x2 // 100, y2//100

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if r:
                        ggg = ggg[:ii + 1]
                        r = False
                        pass
                    else:
                        desk = [[lb, kb, sb, fb, kob, sb, kb, lb], [pb, pb, pb, pb, pb, pb, pb, pb],
                                [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [pw, pw, pw, pw, pw, pw, pw, pw],
                                [lw, kw, sw, fw, kow, sw, kw, lw]]
                        r = True
                        ggg = rr(gg)
                if event.key == pygame.K_w:
                    wr(ggg)
                if event.key == pygame.K_DOWN:
                    ii -= 1
                    if ii < 0:
                        ii = 0
                    desk = [[lb, kb, sb, fb, kob, sb, kb, lb], [pb, pb, pb, pb, pb, pb, pb, pb],
                                 [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [pw, pw, pw, pw, pw, pw, pw, pw],
                                 [lw, kw, sw, fw, kow, sw, kw, lw]]
                    desk3 = [[b, b, b, b, b, b, b, b], [b, b, b, b, b, b, b, b], [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [w, w, w, w, w, w, w, w],
                             [w, w, w, w, w, w, w, w]]
                    for iii in range(ii):
                        desk, d, text, desk3 = rer(iii, ggg)
                    if ii % 2 != 0:
                        h = b
                    else:
                        h = w
                    continue




            if event.type == pygame.MOUSEBUTTONDOWN:
                if r:
                    ii += 1
                    if ii >= len(ggg):
                        continue
                    desk, d, text, desk3 = rer(ii, ggg)

                    if ii % 2 != 0:
                        h = b
                    else:
                        h = w
                    continue
                x, y = y2, x2
                if desk[x][y] != 0:
                    if desk3[x][y] == h:
                        q = (x, y)
                    else:
                        if q == (-1, -1):
                            continue

                        if desk[q[0]][q[1]] == pw:
                            figura = "П"
                            if not ppw(q, x, y, desk):
                                continue
                        if desk[q[0]][q[1]] == pb:
                            figura = "П"
                            if not ppb(q, x, y, desk):
                                continue
                        if desk[q[0]][q[1]] == lw:
                            figura = "Л"
                            if not pl(q, x, y, desk):
                                continue
                        if desk[q[0]][q[1]] == lb:
                            figura = "Л"
                            if not pl(q, x, y, desk):
                                continue
                        if desk[q[0]][q[1]] == sb:
                            figura = "С"
                            if not ps(q,x, y, desk):
                                continue
                        if desk[q[0]][q[1]] == sw:
                            figura = "С"
                            if not ps(q, x, y, desk):
                                continue
                        if desk[q[0]][q[1]] == kw:
                            figura = "К"
                            if not pk(q, x, y):
                                continue
                        if desk[q[0]][q[1]] == kb:
                            figura = "К"
                            if not pk(q, x, y):
                                continue
                        if desk[q[0]][q[1]] == kow:
                            figura = "Кр"
                            if (not kor([x, y], q, llw, lrw, kkw)) and kor([x, y], q, llw, lrw, kkw) != 0 and kor([x, y], q, llw, lrw, kkw) != 2:
                                continue
                        if desk[q[0]][q[1]] == kob:
                            figura = "Кр"
                            if (not kor([x, y], q, llb, lrb, kkb)) and kor([x, y], q, llb, lrb, kkb) != 0 and kor([x, y], q, llb, lrb, kkb) != 2:
                                continue

                        if desk[q[0]][q[1]] == fb:
                            figura = "Ф"
                            if q[0] == x or q[1] == y:
                                if not pl(q, x, y, desk):
                                    continue
                            else:
                                if not ps(q, x, y, desk):
                                    continue

                        if desk[q[0]][q[1]] == fw:
                            figura = "Ф"
                            if q[0] == x or q[1] == y:
                                if not pl(q, x, y, desk):
                                    continue
                            else:
                                if not ps(q, x, y, desk):
                                    continue

                        m = desk[q[0]][q[1]]
                        m2 = kordw
                        mb = kordb
                        mm = desk[x][y]
                        m1 = desk3[x][y]
                        m11 = kkb
                        m111 = kkw

                        if q[0] == 0 and q[1] == 0:
                            lrb = False
                        elif q[0] == 0 and q[1] == 7:
                            llb = False
                        elif q[0] == 7 and q[1] == 0:
                            lrw = False
                        elif q[0] == 7 and q[1] == 7:
                            lrw = False
                        elif q[0] == 0 and q[1] == 4:
                            kkb = False
                        elif q[0] == 7 and q[1] == 4:
                            kkw = False



                        desk[x][y] = desk[q[0]][q[1]]
                        desk[q[0]][q[1]] = 0
                        desk3[x][y] = h
                        if desk[q[0]][q[1]] == kow:
                            kordw = [x, y]
                        if desk[q[0]][q[1]] == kob:
                            kordb = [x, y]
                        chh = ""
                        if h == b:
                            if cha(kordb, desk3, desk, b, kordw, kordb)[0] != 0:
                                desk[x][y] = mm
                                desk[q[0]][q[1]] = m
                                desk3[x][y] = m1
                                kordw = m2
                                kordb = mb
                                kkw = m111
                                kkb = m11
                                continue
                        else:
                            if cha(kordw, desk3, desk, w, kordw, kordb)[0] != 0:
                                desk[x][y] = mm
                                desk[q[0]][q[1]] = m
                                desk3[x][y] = m1
                                kordw = m2
                                kordb = mb
                                kkw = m111
                                kkb = m11

                                continue
                        if cha(kordw, desk3, desk, w, kordw, kordb)[0] != 0 or cha(kordb, desk3, desk, b, kordw, kordb)[0] != 0:
                            chh = "+"
                        write((q[0], q[1]), (x, y), figura, chh)
                        desk3[q[0]][q[1]] = 0
                        if w == h:
                            if desk[x][y] == kow:
                                if kor([x, y], q, True, True, True) == 0:
                                    desk[7][0] = 0
                                    desk3[7][0] = 0
                                    desk[7][3] = lw
                                    desk3[7][3] = w
                                    del ggg[-1]
                                    ggg.append("0-0-0")
                                if kor([x, y], q, True, True, True) == 2:
                                    desk[7][7] = 0
                                    desk3[7][7] = 0
                                    desk[7][5] = lw
                                    desk3[7][5] = w
                                    del ggg[-1]
                                    ggg.append("0-0")

                            h = b
                        else:
                            if desk[x][y] == kob:
                                if kor([x, y], q, True, True, True) == 0:
                                    desk[0][0] = 0
                                    desk3[0][0] = 0
                                    desk[0][3] = lb
                                    desk3[0][3] = b
                                    del ggg[-1]
                                    ggg.append("0-0-0")
                                if kor([x, y], q, True, True, True) == 2:
                                    desk[0][7] = 0
                                    desk3[0][7] = 0
                                    desk[0][5] = lb
                                    desk3[0][5] = b
                                    del ggg[-1]
                                    ggg.append("0-0")
                            h = w
                        q = (-1, -1)
                        ii += 1


                else:
                    if q != (-1, -1):
                        if desk[q[0]][q[1]] == pw:
                            figura = "П"
                            if not ppw(q, x, y, desk):
                                continue
                        if desk[q[0]][q[1]] == pb:
                            figura = "П"
                            if not ppb(q, x, y, desk):
                                continue
                        if desk[q[0]][q[1]] == lw:
                            figura = "Л"
                            if not pl(q, x, y, desk):
                                continue
                        if desk[q[0]][q[1]] == lb:
                            figura = "Л"
                            if not pl(q, x, y, desk):
                                continue
                        if desk[q[0]][q[1]] == sb:
                            figura = "С"
                            if not ps(q, x, y, desk):
                                continue
                        if desk[q[0]][q[1]] == sw:
                            figura = "С"
                            if not ps(q, x, y, desk):
                                continue
                        if desk[q[0]][q[1]] == kw:
                            figura = "К"
                            if not pk(q, x, y):
                                continue
                        if desk[q[0]][q[1]] == kb:
                            figura = "К"
                            if not pk(q, x, y):
                                continue

                        if desk[q[0]][q[1]] == fb:
                            figura = "Ф"
                            if q[0] == x or q[1] == y:
                                if not pl(q, x, y, desk):
                                    continue
                            else:
                                if not ps(q, x, y, desk):
                                    continue

                        if desk[q[0]][q[1]] == fw:
                            figura = "Ф"
                            if q[0] == x or q[1] == y:
                                if not pl(q, x, y, desk):
                                    continue
                            else:
                                if not ps(q, x, y, desk):
                                    continue
                        if desk[q[0]][q[1]] == kow:
                            figura = "Кр"
                            if (not kor([x, y], q, llw, lrw, kkw)) and kor([x, y], q, llw, lrw, kkw) != 0 and kor([x, y], q, llw, lrw, kkw) != 2:
                                continue
                        if desk[q[0]][q[1]] == kob:
                            figura = "Кр"
                            if (not kor([x, y], q, llb, lrb, kkb)) and kor([x, y], q, llb, lrb, kkb) != 0 and kor([x, y], q, llb, lrb, kkb) != 2:
                                continue
                        chh = ""
                        m = desk[q[0]][q[1]]
                        mm = desk[x][y]
                        m1 = desk3[x][y]
                        m2 = kordw
                        mb = kordb
                        m11 = kkb
                        m111 = kkw

                        if q[0] == 0 and q[1] == 0:
                            lrb = False
                        elif q[0] == 0 and q[1] == 7:
                            llb = False
                        elif q[0] == 7 and q[1] == 0:
                            lrw = False
                        elif q[0] == 7 and q[1] == 7:
                            lrw = False
                        elif q[0] == 0 and q[1] == 4:
                            kkb = False
                        elif q[0] == 7 and q[1] == 4:
                            kkw = False

                        if desk[q[0]][q[1]] == kow:
                            kordw = [x, y]
                        elif desk[q[0]][q[1]] == kob:
                            kordb = [x, y]
                        desk[x][y] = desk[q[0]][q[1]]
                        desk[q[0]][q[1]] = 0
                        desk3[x][y] = h

                        if h == b:
                            if cha(kordb, desk3, desk, b, kordw, kordb)[0] != 0:
                                desk[x][y] = mm
                                desk[q[0]][q[1]] = m
                                desk3[x][y] = m1
                                kordw = m2
                                kordb = mb
                                kkw = m111
                                kkb = m11
                                continue
                        else:
                            if cha(kordw, desk3, desk, w, kordw, kordb)[0] != 0:
                                desk[x][y] = mm
                                desk[q[0]][q[1]] = m
                                desk3[x][y] = m1
                                kordw = m2
                                kordb = mb
                                kkw = m111
                                kkb = m11
                                continue
                        if cha(kordw, desk3, desk, w, kordw, kordb)[0] != 0 or cha(kordb, desk3, desk, b, kordw, kordb)[0] != 0:
                            chh = "+"
                        write((q[0], q[1]), (x, y), figura, chh)
                        desk3[q[0]][q[1]] = 0
                        if w == h:
                            if desk[x][y] == kow:
                                if kor([x, y], q, True, True, True) == 11:
                                    desk[7][0] = 0
                                    desk3[7][0] = 0
                                    desk[7][3] = lw
                                    desk3[7][3] = w
                                    del ggg[-1]
                                    ggg.append("0-0-0")
                                if kor([x, y], q, True, True, True) == 2:
                                    desk[7][7] = 0
                                    desk3[7][7] = 0
                                    desk[7][5] = lw
                                    desk3[7][5] = w
                                    del ggg[-1]
                                    ggg.append("0-0")
                            h = b
                        else:
                            if desk[x][y] == kob:
                                if kor([x, y], q, True, True, True) == 11:
                                    desk[0][0] = 0
                                    desk3[0][0] = 0
                                    desk[0][3] = lb
                                    desk3[0][3] = b
                                    del ggg[-1]
                                    ggg.append("0-0-0")
                                if kor([x, y], q, True, True, True) == 2:
                                    desk[0][7] = 0
                                    desk3[0][7] = 0
                                    desk[0][5] = lb
                                    desk3[0][5] = b
                                    del ggg[-1]
                                    ggg.append("0-0")
                            h = w
                        q = (-1, -1)
                        ii += 1

                if cha(kordw, desk3, desk, w, kordw, kordb)[0] != 0:
                    f1 = pygame.font.Font(None, 90)
                    text = f1.render('Шах белым', True, "black")
                    #if mat(cha(kordw, desk3, desk, w, kordw, kordb), kordw, desk3, desk, w, kordw, kordb):
                        #text = f1.render('М белым', True, "black")
                    d = 1


                elif cha(kordb, desk3, desk, b, kordw, kordb)[0] != 0:
                    f1 = pygame.font.Font(None, 90)
                    text = f1.render('Шах черным', True, "black")
                    d = 1
                else:
                    d = 0




            screen.blit(desk2, (0, 0))
            for i in range(8):
                for j in range(8):
                    if desk[i][j] != 0:
                        screen.blit(desk[i][j], (j * 100, i * 100))

            if d:
                screen.blit(text, (200, 400))
            pygame.display.flip()
            clock.tick(100)






if __name__==main():
    main()

