import sys
sys.stdin = open('5789.txt')

T = int(input())
for tc in range(1, T+1):
    n, q = map(int, input().split())
    qLst = [list(map(int, input().split())) for _ in range(q)]
    boxLst = [0] * n

    for j in range(qLst[q-1][0]-1, qLst[q-1][1]):
        boxLst[j] = q


    for i in range(q-1, 0, -1):
        if qLst[i-1][1] < qLst[q-1][0] or qLst[i-1][0] > qLst[q-1][1]:
            for j in range(qLst[i-1][0]-1, qLst[i-1][1]):
                if boxLst[j] == 0:
                    boxLst[j] = i
        else:
            if qLst[i-1][0] < qLst[q-1][0]:
                for j in range(qLst[i-1][0]-1, qLst[q-1][0]):
                    if boxLst[j] == 0:
                        boxLst[j] = i
                qLst[q-1][0] = qLst[i-1][0]
            if qLst[i-1][1] > qLst[q-1][1]:
                for j in range(qLst[q-1][q], qLst[i-1][1]):
                    if boxLst[j] == 0:
                        boxLst[j] = i
                qLst[q-1][1] = qLst[i-1][1]

    print(f'#{tc} ', end='')
    print(*boxLst)

# # include <iostream>
# # include <array>
# # include <string>
# int
# main()
# {
#     std:: ios_base::sync_with_stdio(false), std::cin.tie(nullptr), std::cout.tie(nullptr);
# int
# test_case, T, N, Q, i, j;
# std::array < int, 1001 > box;
# std::array < std::array < int, 2 >, 1001 > qlist;
# std::string
# out;
# std::cin >> T;
# for (test_case = 1; test_case <= T; ++test_case)
# {
#     std:: cin >> N >> Q;
# for (i = 1; i <= N; ++i)
# box[i] = 0;
# for (i = 1; i <= Q; ++i)
# std::cin >> qlist[i][0] >> qlist[i][1];
#
# for (j = qlist[Q][0]; j <= qlist[Q][1]; ++j)
# box[j] = Q;
#
# for (i = Q - 1; i > 0; --i)
# {
# if (qlist[i][1] < qlist[Q][0] | | qlist[i][0] > qlist[Q][1])
# {
# for (j = qlist[i][0]; j <= qlist[i][1]; ++j)
# if (box[j] == 0)
# box[j] = i;
# }
# else
# {
# if (qlist[i][0] < qlist[Q][0])
# {
# for (j = qlist[i][0]; j < qlist[Q][0]; ++j)
# {
# if (box[j] == 0)
# box[j] = i;
# }
# qlist[Q][0] = qlist[i][0];
# }
# if (qlist[i][1] > qlist[Q][1])
# {
# for (j = qlist[Q][1] + 1; j <= qlist[i][1]; ++j)
# {
# if (box[j] == 0)
# box[j] = i;
# }
# qlist[Q][1] = qlist[i][1];
# }
# }
# }
# out += '#' + std::
#     to_string(test_case);
# for (i = 1; i <= N; ++i)
# out += ' ' + std::to_string(box[i]);
# out += '\n';
# }
# std::cout << out;
# return 0;
# }