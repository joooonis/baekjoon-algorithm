# BOJ 1041, 주사위

- RANK : Gold
- Language : Python
- [주사위](https://www.acmicpc.net/problem/1041)

<br/>

# 문제 설명

주사위가 전개도와 함께 주어진다. N×N×N 크기의 정육면체를 만들 때 이를 탁자위에 두었을 때 바닥면을 제외한 5면의 쓰여 있는 수의 합의 최솟값을 구해라.

<br/>

# 주사위

- 결죽 주사위 면의 종류는 1면, 2면, 3면이 보이는 3가지 종류입니다.
- 1면 : 5^2-16^n+12 개
- 2면 : 8n-12 개
- 3면 : 4 개
- 이므로 각 면의 개수에 따라 쓰일 수 있는 숫자의 최소합을 곱하여 값을 계산하면 됩니다.
- 이때 서로 마주보는 면은 같이 보여질 수 없기 때문에 이를 위해 전개도에서 각각 서로 마주보는 면의 최소값 3개를 리스트에 저장하고 면의 개수에 따라서 이를 쓰여진 숫자로 사용합니다.
- n=1 일때의 예외처리를 해주면 정답입니다.
