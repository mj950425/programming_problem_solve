// 수들의합2
//#include<iostream>
//#include<vector>
//#include<cmath>
//#include<queue>
//#include<utility>
//#include<algorithm>
//#include<deque>
//using namespace std;
//int n;
//int m;
//int arr[10001];
//int main() {
//	cin >> n >> m;
//	for (int i = 0; i < n; i++) {
//		cin >> arr[i];
//	}
//	int start = 0;
//	int end = 0;
//	int answer = 0;
//	int sum = (arr[start] + arr[end]) / 2;
//	while (end != n) {
//		if (sum < m) {
//			end += 1;
//			sum += arr[end];
//
//		}
//		else if (sum == m) {
//			end += 1;
//			sum += arr[end];
//			answer += 1;
//		}
//		else {
//			sum -= arr[start];
//			start += 1;
//
//		}
//	}
//	cout << answer;
//}

//부분합
//#include<iostream>
//#include<vector>
//#include<cmath>
//#include<queue>
//#include<utility>
//#include<algorithm>
//#include<deque>
//
//
//using namespace std;
//int N;
//int S;
//int arr[100001];
//vector <int> v;
//int main() {
//	cin >> N >> S;
//	for (int i = 0; i < N; i++) {
//		cin >> arr[i];
//
//	}
//
//	int start = 0;
//	int end = 0;
//	int sum = arr[0];
//	while (end != N) {
//		
//		if (sum < S) {
//			end += 1;
//			sum += arr[end];
//		}
//		else if (sum == S) {
//			v.push_back(end - start + 1);
//			end += 1;
//			sum += arr[end];
//			
//		}
//		else {
//			v.push_back(end - start + 1);
//			sum -= arr[start];
//			start += 1;
//			
//		}
//	}
//	if (v.empty()) {
//		cout << 0;
//	}
//	else{
//		sort(v.begin(), v.end(), less<int>());
//		cout << v[0];
//	}
//}
//
////나이트의 이동
//#include<iostream>
//#include<vector>
//#include<cmath>
//#include<queue>
//#include<utility>
//#include<algorithm>
//#include<deque>
//#include<string.h>
//#include<deque>
//using namespace std;
//
//int x , y , dx , dy;
//int T;
//int cnt;
//int I;
//int current_y;
//int current_x;
//int object_y;
//int object_x;
//int arr[301][301];
//bool visited[301][301];
//int dir[8][2] = { {-2,-1},{-1,-2},{1,-2},{2,-1},{2,1},{1,2},{-1,2},{-2,1} };
//deque<pair<int, int>> dq;
//deque<int> c;
//vector<int> answer;
//int main() {
//	cin >> T;
//
//	for (int i = 0; i < T; i++) {
//		cnt = 0;
//		cin >> I;
//		cin >> current_y >> current_x;
//		cin >> object_y >> object_x;
//		memset(arr, 0, sizeof(arr));
//		memset(visited, false, sizeof(visited));
//		visited[current_y][current_x] = true;
//		dq.push_back(make_pair(current_y, current_x));
//		c.push_back(0);
//		while (!dq.empty()) {
//			y = dq.front().first;
//			x = dq.front().second;
//			cnt = c.front();
//
//			if (y == object_y && x == object_x) {
//				dq.clear();
//				c.clear();
//				answer.push_back(cnt);
//				break;
//			}
//			dq.pop_front();
//			c.pop_front();
//			for (int i = 0; i < 8; i++) {
//				dy = dir[i][0] + y;
//				dx = dir[i][1] + x;
//				if (0 <= dx && dx < I && 0 <= dy && dy < I) {
//					if (visited[dy][dx] == false) {
//						dq.push_back(make_pair(dy, dx));
//						c.push_back(cnt + 1);
//						visited[dy][dx] = true;
//
//					}
//
//				}
//			}
//			cnt + 1;
//		
//		
//		
//		
//		}
//	}
//
//
//	for (int i = 0; i < answer.size(); i++) {
//		cout << answer[i]<<"\n";
//	}
//
//}
//
////그림
//#include<iostream>
//#include<vector>
//#include<cmath>
//#include<queue>
//#include<utility>
//#include<algorithm>
//#include<deque>
//#include<string.h>
//#include<deque>
//using namespace std;
//int dir[4][2] = { {1,0},{-1,0},{0,1},{0,-1} };
//int arr[501][501];
//int visited[501][501];
//int n, m, cnt;
//deque<pair<int, int>> dq;
//vector<int> v;
//int x, y, dx, dy, cc;
//int main() {
//	cnt = 1;
//	cc = 0;
//	cin >> n >> m;
//	for (int i = 0; i < n; i++) {
//		for (int j = 0; j < m; j++) {
//			cin >> arr[i][j];
//		}
//	}
//
//
//	for (int i= 0; i < n; i++) {
//		for (int j = 0; j < m; j++) {
//			if (arr[i][j] == 1) {
//				visited[i][j] = true;
//				cnt += 1;
//				cc = 1;
//				dq.push_back(make_pair(i, j));
//				while (!dq.empty()) {
//
//					y = dq.front().first;
//					x = dq.front().second;
//					dq.pop_front();
//					for (int i = 0; i < 4; i++) {
//						dy = y + dir[i][0];
//						dx = x + dir[i][1];
//						if (visited[dy][dx] == false) {
//							if (arr[dy][dx] == 1) {
//								arr[dy][dx] = cnt;
//								dq.push_back(make_pair(dy, dx));
//								visited[dy][dx] = true;
//								cc += 1;
//							}
//						}
//					}
//				}
//				v.push_back(cc);
//
//
//
//
//
//
//
//			}
//		}
//	}
//	sort(v.begin(), v.end(), greater<int>());
//	if (cnt - 1 == 0) {
//		cout << 0 << "\n" << 0;
//	}
//	else{
//		cout << cnt-1 << "\n" << v[0];
//	}
//
//}
//
////보물
//#include<iostream>
//#include<vector>
//#include<cmath>
//#include<queue>
//#include<utility>
//#include<algorithm>
//#include<deque>
//#include<string.h>
//#include<deque>
//using namespace std;
//
//bool cmp(int A, int B)
//{
//	if (A > B) return true;
//	return false;
//}
//
//int N;
//int sum = 0;
//int A[50];
//int B[50];
//int main() {
//	cin >> N;
//	for (int i = 0; i < N; i++) {
//		cin >> A[i];
//	
//	}
//
//	for (int i = 0; i < N; i++) {
//		cin >> B[i];
//	}
//	sort(A, A + N);
//	sort(B, B + N, cmp);
//	for (int i = 0; i < N; i++) {
//		sum += A[i] * B[i];
//	}
//	cout << sum;
//}
//보물
//
////배열돌리기 4
//#include<iostream>
//#include<vector>
//#include<cmath>
//#include<queue>
//#include<utility>
//#include<algorithm>
//#include<deque>
//#include<string.h>
//#include<deque>
//using namespace std;
//int arr[50][50];
//int cp[50][50];
//int N, M, K, r, c, s, mid;
//int R[6];
//int C[6];
//int S[6];
//int st = 100000000000;
//int ar[50][50];
//bool Select[6];
//vector<int> answer;
//
//void sol() {
//	r = r - 1;
//	c = c - 1;
//	int buf = s;
//	mid = r;
//	memset(cp, 0, sizeof(cp));
//
//	while (1) {
//		for (int j = c - s + 1; j <= c + s; j++) {
//			cp[r - s][j] = arr[r - s][j - 1];
//		}
//
//		for (int i = r - s + 1; i <= r + s; i++) {
//			cp[i][c + s] = arr[i - 1][c + s];
//		}
//
//		for (int j = c + s - 1; j >= c - s; j--) {
//			cp[r + s][j] = arr[r + s][j + 1];
//		}
//
//		for (int i = r + s - 1; i >= r - s; i--) {
//			cp[i][c - s] = arr[i + 1][c - s];
//		}
//		if (s == 0) {
//			cp[r][c] = arr[r][c];
//			break;
//		}
//		s -= 1;
//
//	}
//	s = buf;
//	for (int i = r - s; i < r + s + 1; i++) {
//		for (int j = c - s; j < c + s + 1; j++) {
//			arr[i][j] = cp[i][j];
//		}
//	}
//	for (int i = 0; i < N; i++) {
//		for (int j = 0; j < M; j++) {
//		}
//	}
//	for (int i = 0; i < N; i++) {
//		for (int j = 0; j < M; j++) {
//		}
//	}
//
//
//
//	for (int i = 0; i < N; i++) {
//		int sum = 0;
//		for (int j = 0; j < M; j++) {
//			sum += arr[i][j];
//		}
//		if (s > sum) {
//			s = sum;
//		}
//	}
//}
//int Arr[6] = { 0,1,2,3,4,5 };
//deque<int> V;
//void DFS(int Cnt, int K)
//{
//	if (Cnt == K)
//	{
//		for (int i = 0; i < N; i++) {
//			for (int j = 0; j < M; j++) {
//				arr[i][j] = ar[i][j];
//			}
//		}
//		//for (int i = 0; i < V.size(); i++) {
//		//	cout << V[i] << " "<<"\n";
//		//}
//		for (int i = 0; i < V.size(); i++) {
//			int v = V[i];
//			r = R[v];
//			c = C[v];
//			s = S[v];
//			//cout << "r,c,s" << r << c << s<<"\n";
//			r = r - 1;
//			c = c - 1;
//			int buf = s;
//			mid = r;
//			memset(cp, 0, sizeof(cp));
//
//			while (1) {
//				for (int j = c - s + 1; j <= c + s; j++) {
//					cp[r - s][j] = arr[r - s][j - 1];
//				}
//
//				for (int i = r - s + 1; i <= r + s; i++) {
//					cp[i][c + s] = arr[i - 1][c + s];
//				}
//
//				for (int j = c + s - 1; j >= c - s; j--) {
//					cp[r + s][j] = arr[r + s][j + 1];
//				}
//
//				for (int i = r + s - 1; i >= r - s; i--) {
//					cp[i][c - s] = arr[i + 1][c - s];
//				}
//				if (s == 0) {
//					cp[r][c] = arr[r][c];
//					break;
//				}
//				s -= 1;
//
//			}
//			s = buf;
//			for (int i = r - s; i < r + s + 1; i++) {
//				for (int j = c - s; j < c + s + 1; j++) {
//					arr[i][j] = cp[i][j];
//				}
//			}
//			//
//			//for (int i = 0; i < N; i++) {
//			//	for (int j = 0; j < M; j++) {
//			//		cout << arr[i][j];
//			//	}
//			//	cout << "\n";
//			//}
//			//
//
//			for (int i = 0; i < N; i++) {
//				int sum = 0;
//				for (int j = 0; j < M; j++) {
//					sum += arr[i][j];
//				}
//				if (st > sum) {
//					st = sum;
//					answer.push_back(st);
//				}
//			}
//		}
//		return;
//	}
//
//	for (int i = 0; i < K; i++)
//	{
//		if (Select[i] == true) continue;
//		Select[i] = true;
//		V.push_back(Arr[i]);
//		DFS(Cnt + 1,K);
//		V.pop_back();
//		Select[i] = false;
//	}
//}
//
//
//int main() {
//	cin >> N >> M >> K;
//	for (int i = 0; i < N; i++) {
//		for (int j = 0; j < M; j++) {
//			cin >> arr[i][j];
//			ar[i][j] = arr[i][j];
//		}
//	}
//	for (int i = 0; i < K; i++) {
//		cin >> r >> c >> s;
//		R[i] = r;
//		C[i] = c;
//		S[i] = s;
//	}
//
//	DFS(0, K);
//	sort(answer.begin(), answer.end());
//	cout << answer[0];
//}