# coding=utf-8
from oca_test.sindroms import *
from oca_test.cards import *


def res_analyse(r):
    text = []
    if r.A >= 70 and r.B >= 70 and r.C >= 70 and r.D >= 70 and r.E >= 0 and r.F >= 70 and r.G >= 70 and r.H >= 70 \
            and r.I >= 70 and r.J >= 70:
        text.append(['Синдром Тити-Вити (все показатели в 1м диапазоне)', S_A1_B1_C1_D1_E1_F1_G1_H1_I1_J1])
    else:
        if (-38 >= r.A >= -95) and (-65 >= r.B >= -100) and (-63 >= r.C >= -96) and (35 >= r.D >= -83) and \
                (45 >= r.E >= 3) and (72 >= r.F >= 22) and (-55 >= r.G >= -92) and (-35 >= r.H >= -98) and \
                (18 >= r.I >= -90) and (22 >= r.J >= -72):
            text.append(["Случайный график", S1])
        else:
            if r.G >= 90 and r.I >= 90:
                text.append(["Высокая вероятность, что человек лжет. Весьма вероятно, что он дал ложные ответы в "
                             "своем тесте", S_G90_I90])
            if r.B_circle is True:
                text.append(["B обведена в кружок", B_circle])
            if r.E_circle is True:
                text.append(["E обведена в кружок", E_circle])

            synd_list = []
            if r.A >= 70 and r.B <= 19:
                synd_list.append("A")
                text.append(["А >= 70, B <= 19", S_A1_B34])
            if r.A >= 70 and r.C <= 19:
                synd_list.append("A")
                text.append(["А >= 70, C <= 19", S_A1_C34])
            if r.B >= 70 and r.A <= 19:
                synd_list.append("B")
                text.append(["B >= 70, A <= 19", S_B1_A34])
            if r.B >= 70 and r.C <= 19:
                synd_list.append("B")
                text.append(["B >= 70, C <= 19", S_B1_C34])
            if r.C >= 70 and r.A <= 19:
                synd_list.append("C")
                text.append(["C >= 70, A <= 19", S_C1_A34])
            if r.C >= 70 and r.B <= 19:
                synd_list.append("C")
                text.append(["C >= 70, B <= 19", S_C1_B34])
            if r.D >= 70 and r.A <= 19:
                synd_list.append("D")
                text.append(["D >= 70, A <= 19", S_D1_A34])
            if r.E >= 70 and r.D <= 19:
                synd_list.append("E")
                text.append(["E >= 70, D <= 19", S_E1_D34])
            if r.E >= 70 and r.F <= 19:
                synd_list.append("E")
                text.append(["E >= 70, F <= 19", S_E1_F34])
            if r.F >= 70 and r.E <= 19:
                synd_list.append("F")
                text.append(["F >= 70, E <= 19", S_F1_E34])
            if r.F >= 70 and r.G <= 19:
                synd_list.append("F")
                text.append(["F >= 70, G <= 19", S_F1_G34])
            if r.G >= 70 and r.F <= 19:
                synd_list.append("G")
                text.append(["G >= 70, F <= 19", S_G1_F34])
            if r.H >= 70 and r.I <= 19:
                synd_list.append("H")
                text.append(["H >= 70, I <= 19", S_H1_I34])
            if r.I >= 70 and r.H <= 19:
                synd_list.append("I")
                text.append(["I >= 70, H <= 19", S_I1_H34])
            if 'A' not in synd_list:
                if r.A >= 70:
                    text.append(["A - 1й диапазон", A1])
                if 20 <= r.A < 70:
                    text.append(["A - 2й диапазон", A2])
                if -39 <= r.A < 20:
                    text.append(["A - 3й диапазон", A3])
                if r.A < -39:
                    text.append(["A - 4й диапазон", A4])
            if 'B' not in synd_list:
                if r.B >= 70:
                    text.append(["B - 1й диапазон", B1])
                if 20 <= r.B < 70:
                    text.append(["B - 2й диапазон", B2])
                if -39 <= r.B < 20:
                    text.append(["B - 3й диапазон", B3])
                if r.B < -39:
                    text.append(["B - 4й диапазон", B4])
            if 'C' not in synd_list:
                if r.C >= 70:
                    text.append(["C - 1й диапазон", C1])
                if 20 <= r.C < 70:
                    text.append(["C - 2й диапазон", C2])
                if -39 <= r.C < 20:
                    text.append(["C - 3й диапазон", C3])
                if r.C < -39:
                    text.append(["C - 4й диапазон", C4])
            if 'D' not in synd_list:
                if r.D >= 70:
                    text.append(["D - 1й диапазон", D1])
                if 20 <= r.D < 70:
                    text.append(["D - 2й диапазон", D2])
                if -39 <= r.D < 20:
                    text.append(["D - 3й диапазон", D3])
                if r.D < -39:
                    text.append(["D - 4й диапазон", D4])
            if 'E' not in synd_list:
                if r.E >= 70:
                    text.append(["E - 1й диапазон", E1])
                if 20 <= r.E < 70:
                    text.append(["E - 2й диапазон", E2])
                if -39 <= r.E < 20:
                    text.append(["E - 3й диапазон", E3])
                if r.E < -39:
                    text.append(["E - 4й диапазон", E4])
            if 'F' not in synd_list:
                if r.F >= 70:
                    text.append(["F - 1й диапазон", F1])
                if 20 <= r.F < 70:
                    text.append(["F - 2й диапазон", F2])
                if -39 <= r.F < 20:
                    text.append(["F - 3й диапазон", F3])
                if r.F < -39:
                    text.append(["F - 4й диапазон", F4])
            if 'G' not in synd_list:
                if r.G >= 70:
                    text.append(["G - 1й диапазон", G1])
                if 20 <= r.G < 70:
                    text.append(["G - 2й диапазон", G2])
                if -39 <= r.G < 20:
                    text.append(["G - 3й диапазон", G3])
                if r.G < -39:
                    text.append(["G - 4й диапазон", G4])
            if 'H' not in synd_list:
                if r.H >= 70:
                    text.append(["H - 1й диапазон", H1])
                if 20 <= r.H < 70:
                    text.append(["H - 2й диапазон", H2])
                if -39 <= r.H < 20:
                    text.append(["H - 3й диапазон", H3])
                if r.H < -39:
                    text.append(["H - 4й диапазон", H4])
            if 'I' not in synd_list:
                if r.I >= 70:
                    text.append(["I - 1й диапазон", I1])
                if 20 <= r.I < 70:
                    text.append(["I - 2й диапазон", I2])
                if -39 <= r.I < 20:
                    text.append(["I - 3й диапазон", I3])
                if r.I < -39:
                    text.append(["I - 4й диапазон", I4])
            if 'J' not in synd_list:
                if r.J >= 70:
                    text.append(["J - 1й диапазон", J1])
                if 20 <= r.J < 70:
                    text.append(["J - 2й диапазон", J2])
                if -39 <= r.J < 20:
                    text.append(["J - 3й диапазон", J3])
                if r.J < -39:
                    text.append(["J - 4й диапазон", J4])

            if r.A < -39 and r.B < -39 and r.C < -39:
                text.append(["A, B, C - внизу", S_A4_B4_C4])
            if r.A < -39 and r.E >= 70:
                text.append(["A - внизу, E - вверху", S_A4_E1])
            if r.A < -39 and r.B < -39 and r.C < -39 and r.E >= 70:
                text.append(["A, B, C - внизу, E - вверху", S_A4_B4_C4_E1])
            if r.A < -39 and r.J < -39:
                text.append(["A, J - внизу", S_A4_J4])
            if r.A < -39 and r.C < -39 and r.G < -39 and r.F >= 70:
                text.append(["A, C, G - внизу, F - вверху", S_A4_C4_G4_F1])
            if r.H < -39 and r.A >= 70:
                text.append(["A - вверху, H - внизу", S_A1_H4])
            if -39 <= r.D < 70 <= r.A:
                text.append(["A - вверху, D - внизу", S_A1_D23])
            if r.B < -39 and r.G < -39 and r.F >= 70:
                text.append(["B, G - внизу, F - вверху", S_B4_G4_F1])
            if r.D < -39 and r.B >= 70:
                text.append(["B - вверху, D - внизу", S_B1_D4])
            if r.C < -39 and r.H < -39:
                text.append(["C, H - внизу", S_C4_H4])
            if r.D < -39 and r.J >= 70:
                text.append(["J - вверху, D - внизу", S_D4_J1])
            if r.D < -39 and r.G >= 70:
                text.append(["G - вверху, D - внизу", S_D4_G1])
            if r.A < -39 and r.B < -39 and r.C < -39 and r.G < -39 and r.H < -39 and r.I < -39 and r.J < -39 and \
               r.D >= 70 and r.E >= 70 and r.F >= 70:
                text.append(["D, E, F - вверху. Все остальное внизу", S_A4_B4_C4_D1_E1_F1_G4_H4_I4_J4])
            if r.D < -39 and r.G < -39 and r.H < -39 and r.I < -39:
                text.append(["D, G, H, I - внизу", S_D4_G4_H4_I4])
            if r.E < -39 and r.F < -39 and r.J < -39:
                text.append(["E, F, J - внизу", S_E4_F4_J4])
            if r.E < -39 and r.F < -39:
                text.append(["E, F - внизу", S_E4_F4])
            if r.G < -39 and r.E >= 70:
                text.append(["E - вверху, G - внизу", S_E1_G4])
            if r.G < -39 and r.H < -39 and r.F >= 70:
                text.append(["F - вверху, G, H - внизу", S_F1_G4_H4])
            if r.G < -69 and r.B >= 70 and r.I >= 70 and r.J >= 70:
                text.append(["B, I, J - вверху, F - не вверху", S_I1_J1_B1_F234])
            if r.J < -39 and r.I >= 70:
                text.append(["I - вверху, J - внизу", S_I1_J4])
            if r.A < -39 and r.C < -39 and r.D < -39 and r.G < -39 and r.H < -39 and r.I < -39 and r.J < -39:
                text.append(["A, C, D, G, H, I, J- внизу", S_A4_C4_D4_H4_I4_J4])

            if r.C == max(r.A, r.B, r.C, r.D, r.E, r.F, r.G, r.H, r.I, r.J):
                text.append(["C выше всех остальных", S_C_highest])
            if r.D == max(r.A, r.B, r.C, r.D, r.E, r.F, r.G, r.H, r.I, r.J):
                text.append(["D выше всех остальных", S_D_highest])
            if r.E > r.F:
                text.append(["E выше F", S_E_above_F])
            if r.E < r.F:
                text.append(["F выше E", S_F_above_E])
            if r.I == max(r.A, r.B, r.C, r.D, r.E, r.F, r.G, r.H, r.I, r.J):
                text.append(["I выше всех остальных", S_I_highest])
    return text
