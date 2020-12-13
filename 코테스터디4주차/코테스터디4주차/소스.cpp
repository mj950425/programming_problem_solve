// 배낭문제
/*
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;
int map[101][100001];
deque<pair<int, int>> q;
int main() {
	int N;
	int K;
	int buf = 0;
	cin >> N >> K ;
	for (int i = 0; i < N; i++) {
		int a;
		int b;
		cin >> a >> b;
		pair<int, int> p = make_pair(a, b);
		q.push_back(p);
	}
	while (!q.empty()) {

		buf = buf + 1;
		pair<int, int> n = q.front();
		int first = n.first;
		int second = n.second;
		q.pop_front();
		for(int i =0; i<K+1;i++){
			
			if(i>=first){
				map[buf][i] = max(map[buf - 1][i], second+map[buf - 1][i - first]);
			}
			else {
				map[buf][i] = map[buf - 1][i];

			}	
		}
	}
	cout << map[N][K];
}
*/

//연구소 문제
/*
#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;
int N;
int M;
int map[9][9];
int cp[9][9];
int dir[4][2] = { {0,1},{0,-1},{1,0},{-1,0} };
int m[1] = {100};
deque<pair<int, int>> dq;

void bfs(int cnt) {
	cnt = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cp[i][j] = map[i][j];
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (cp[i][j] == 2) {
				cp[i][j] = 5;
				cnt += 1;
				dq.push_back(make_pair(i,j));
			}
			while (!dq.empty()) {
				int y = dq.front().first;
				int x = dq.front().second;
				dq.pop_front();
				for (int i = 0; i < 4; i++) {
					int dx = x + dir[i][1];
					int dy = y + dir[i][0];
					if (dx >= 0 & dy >= 0 & dx < M & dy < N) {
						if (cp[dy][dx]==0) {
							dq.push_back(make_pair(dy, dx));
							cnt += 1;
							cp[dy][dx] = 5;
						}
					}
				}
			}
		}
	}
	if (m[0] > cnt) {
		m[0] = cnt;
	}
}

void dfs(int c) {
	if (c == 3) {
		bfs(0);
		return;
	}
	else{
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 0) {
					map[i][j] = 1;
					dfs(c + 1);
					map[i][j] = 0;
				}
			}
		}
	}
}


int main() {
	int count = 0;
	cin >> N >> M;
	for(int i=0;i<N;i++){
		for (int j = 0; j < M; j++) {
			cin >> map[i][j];
			if (map[i][j] == 1) {
				count += 1;
			}
		}	
	}
	int cnt = 0;	
	dfs(0);
	cout << N*M-m[0]-count-3;
}
*/
/*
//암기왕
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;
vector <int> v1;
vector <int> v2;
vector <int> answer;
int T;
int idx;
int N;
int M;
int mid;
int s;
int e;
int main() {
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		for(int i=0;i<N;i++){
			cin >> idx;
			v1.push_back(idx);
		}
		cin >> M;
		for (int i = 0; i < M; i++) {
			cin >> idx;
			v2.push_back(idx);
		}
		sort(v1.begin(), v1.end(), less<int>());

		s = 0;
		e = N - 1;

		for (int i = 0; i < M; i++) {
			s = 0;
			e = N - 1;
			while (1) {

				mid = (s + e)/2;
				if (v2[i] == v1[mid]) {
					answer.push_back(1);
					break;
				}

				if (v1[mid] < v2[i]) {
					s = mid + 1;

				}

				if (v1[mid] > v2[i]){
					e=mid-1;
				}
				
				if (s + 1 == e) {

					if (v1[s] == v2[i]) {
						answer.push_back(1);
						break;
					}
					else if (v1[e] == v2[i]) {
						answer.push_back(1);
					}
					else{
						answer.push_back(0);
					break;
					}
				}
			}


		}

		for (int i = 0; i < M; i++) {
			cout << answer[i]<<"\n";
		}

	}

}
*/
/*
using namespace std;

vector<int> note1;
vector<int> note2;
vector<vector<int>> dp;

int main() {
	int testcase;
	scanf("%d", &testcase);
	for (int i = 0; i < testcase; i++) {
		int n, m;

		scanf("%d", &n);
		note1.resize(n + 1);
		for (int j = 1; j <= n; j++) scanf("%d", &note1[j]);
		sort(note1.begin(), note1.end());

		scanf("%d", &m);
		note2.resize(m + 1);
		for (int j = 1; j <= m; j++) scanf("%d", &note2[j]);

		for (int j = 1; j <= m; j++) {
			int ans = 0;
			int mid, start = 1, end = n;

			while (end >= start) {
				mid = (start + end) / 2;
				if (note2[j] == note1[mid]) {
					ans = 1;
					break;
				}
				else if (note2[j] < note1[mid]) end = mid - 1;
				else start = mid + 1;
			}
			printf("%d\n", ans);
		}
	}

}*/
/*
//스타트 택시
#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;
deque<pair<int, int>> dq;
int N;
int M;
int fuel;
int arr[21][21];
int loc[401][4];
bool visit[21][21];
int x_car;
int y_car;
int dir[4][2] = { {0,1},{0,-1},{-1,0},{1,0} };
int x, y, dx, dy, xx;
int yy;
int cnt;
int cnt_buf;
int x_buf, y_buf;
int num;
int mj;
deque<int> c;

void bfs2person() {
	cout << "bfs2person 시작 \n";
	memset(visit, false, sizeof(visit));
	cnt = 0;
	cnt_buf = 100000000000;
	y_buf = 100000000000;
	x_buf = 100000000000;
	while (1) {

		y = dq.front().first;
		x = dq.front().second;
		cout << "----------------\n";
		cout << y << x << "\n";
		cout << "----------------\n";

		visit[y][x] = true;

		dq.pop_front();
		cnt = c.front();
		c.pop_front();

		if (cnt == cnt_buf + 1) {
			fuel = fuel - cnt_buf;
			num = arr[y_buf][x_buf];
			arr[y_buf][x_buf] = 0;
			dq.clear();
			c.clear();
			dq.push_back(make_pair(y_buf, x_buf));
			c.push_back(0);
			cout << y_buf << x_buf << "사람을 발견\n";
			mj = 0;
			break;
		}

		//탐색하다가 사람 발견!
		if (arr[y][x] > 0) {
			cout << "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n";
			cout << y << x<< cnt <<"\n";
			cout << "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n";

			//cnt+1인곳을 갈 때 까지 계산
			if (y < y_buf) {
				y_buf = y;
				x_buf = x;
				cnt_buf = cnt;
			}

			else if (y == y_buf) {
				if (x < x_buf) {
					x_buf = x;
					y_buf = y;
					cnt_buf = cnt;
				}
			}
		}
		for (int i = 0; i < 4; i++) {
			dx = x + dir[i][1];
			dy = y + dir[i][0];
			if(0<=dx && dx<N && 0<=dy && dy< N){
				if (visit[dy][dx] == false && arr[dy][dx] != 1) {
					dq.push_back(make_pair(dy, dx));
					c.push_back(cnt+1);
					visit[dy][dx] = true;
				}
			}
		}
		cnt += 1;
	}
}

void bfs2flag() {
	cout << "bfs2flag 시작 \n";
	cnt = 0;
	memset(visit, false, sizeof(visit));
	while (1) {
		y = dq.front().first;
		x = dq.front().second;
		cout << "----------------\n";
		cout << y << x << "\n";
		cout << "----------------\n";
		visit[y][x] = true;
dq.pop_front();
		cnt = c.front();
		c.pop_front();
		if (arr[y][x] == -num) {
			arr[y][x] = 0;
			fuel = fuel + cnt;
			dq.clear();
			c.clear();
			dq.push_back(make_pair(y, x));
			c.push_back(0);
			cout << y << x << "도착지 도착\n";
			break;
		}
		
		for (int i = 0; i < 4; i++) {
			dy = y + dir[i][0];
			dx = x + dir[i][1];
			if (0 <= dx && dx < N && 0 <= dy && dy < N) {
				if (visit[dy][dx] == false && arr[dy][dx] != 1) {
					dq.push_back(make_pair(dy, dx));
					c.push_back(cnt + 1);
					visit[dy][dx] = true;
				}
			}
		}
		cnt += 1;
	}
}

int main() {
	cin >> N >> M >> fuel;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> arr[i][j];
		}
	}
	cin >> y_car >> x_car;
	y_car = y_car - 1;
	x_car = x_car - 1;
	//사람위치는 양수 목적지는 음수
	for (int i = 2; i < M + 2; i++) {
		cin >> y >> x >> yy >> xx;
		arr[y - 1][x - 1] = i;
		arr[yy - 1][xx - 1] = -i;
	}
	dq.push_back(make_pair(y_car, x_car));
	c.push_back(0);
	
	while (1) {
		bfs2person();
		bfs2flag();
		M = M - 1;
		if (M == 0) {
			break;
		}
	}
	cout << fuel;
}*/
/*
#pragma warning(disable: 4996)
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

queue<pair<int, int>>que;
int map[10][10];
int new_map[10][10];
int n, m, cnt = 0;
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };

int bfs() {
	int b_cnt = 0;
	while (!que.empty()) {
		int x = que.front().first;
		int y = que.front().second;
		que.pop();
		b_cnt++;
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx > -1 && nx < n && ny > -1 && ny < m && !new_map[nx][ny] && !map[nx][ny]) {
				que.push({ nx,ny });
				new_map[nx][ny] = 1;
			}
		}
	}
	return b_cnt;
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &map[i][j]);    //바이러스 지도 입력받기
			if (map[i][j] == 1) {
				new_map[i][j] = 1;
				cnt++;
			}
			if (map[i][j] == 2) { // 바이러스가 있다면 
				new_map[i][j] = 1;
				que.push({ i,j }); // bfs를 실시할 que에 집어넣음
			}
		}
	}

	//new_map , 안전영역, 바이러스가 퍼지는 좌표 기본 셋팅 
	//cnt는 안전영역이 아닌 곳을 얘기함

	// 쫙 피면 0 ~ nxm-1까지 => /m은 i , %m은 j  
	int idx = n * m;
	int min = 100;
	for (int i = 0; i < idx - 2; i++) {
		int first_x = i / m;
		int first_y = i % m;
		if (map[first_x][first_y]) continue; // 병균 or 벽 자리에는 새로운 벽을 세울 수 없음.
		for (int j = i + 1; j < idx - 1; j++) {
			int second_x = j / m;
			int second_y = j % m;
			if (map[second_x][second_y]) continue; // 병균 or 벽 자리에는 새로운 벽을 세울 수 없음.
			for (int k = j + 1; k < idx; k++) {
				int third_x = k / m;
				int third_y = k % m;
				if (map[third_x][third_y]) continue; // 병균 or 벽 자리에는 새로운 벽을 세울 수 없음.
				// 벽 만들어주기 
				new_map[first_x][first_y] = 1;
				new_map[second_x][second_y] = 1;
				new_map[third_x][third_y] = 1;
				cnt += 3;
				cout << "-----------------\n";
				for (int i = 0; i < 10; i++) {
					for (int j = 0; j < 10; j++) {
						cout << new_map[i][j];
					}
					cout << "\n";
				}
				cout << "-----------------\n";

				int b_cnt = bfs(); // bfs 실행 
				if (b_cnt < min) min = b_cnt;
				// 벽 허물어주기
				new_map[first_x][first_y] = 0;
				new_map[second_x][second_y] = 0;
				new_map[third_x][third_y] = 0;
				cnt -= 3;
			}
		}
	}

	int not_safe = cnt + min;
	printf("기본: %d , bfs: %d\n", cnt, min);
	printf("%d", idx - not_safe);
}*/

/*
// 상근이의 여행
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;
int T;
int N;
int M;
int a, b;
int main() {
	cin >> T;
	for(int i=0;i<T;i++){
		cin >> N >> M;
		vector<vector<int> > v(N+1, vector<int>(0, 0));
		
		for (int i = 0; i < M; i++) {
			cin >> a >> b;
			v[a].push_back(b);
		}
		cout << N - 1<<"\n";

	}

}
*/
/*
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<vector>
#include<cmath>
#include<queue>
#include<utility>
#include<algorithm>
#include<cstring>
using namespace std;
int n, m, energy;
bool visited[25][25];
int arr[25][25];
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };

//좌표 구조체
struct point {
	int x;
	int y;
};

//손님 구조체
//좌표, 탑승여부
struct customer {
	int x;
	int y;
	bool use;
};

//택시와 손님 거리정보 구조체
//거리, 손님인덱스, 좌표
struct distance_info {
	int dist;
	int idx;
	int x;
	int y;
};

vector<point> taxi_pos; //택시좌표 저장하는 벡터
vector<customer> costomer_info; // 손님 정보 저장하는 벡터
vector<point> target_pos; // 각 손님들의 목표지점 저장하는 벡터
vector<distance_info> dist_info; // 각 손님들의 택시로부터의 거리 저장하는 벡터

bool cmp(distance_info a, distance_info b) {

	if (a.dist < b.dist) return true; // 우선적으로 거리 오름차순
	else if (a.dist == b.dist) {   //거리가 같다면
		if (a.x < b.x) return true;   //행기준 오름차순
		else if (a.x == b.x) {      //행도 같다면
			if (a.y < b.y) return true;   //열기준 오름차순
		}
	}
	return false;
}

int bfs(int x, int y) {
	memset(visited, false, sizeof(visited));
	queue<point> q;
	q.push({ taxi_pos[0].x, taxi_pos[0].y });
	visited[taxi_pos[0].x][taxi_pos[0].y] = true;
	int level = 0;
	bool flag = false;
	while (!q.empty()) {
		if (flag) break;
		int Qsize = q.size();
		for (int i = 0; i < Qsize; i++) {
			int cx = q.front().x;
			int cy = q.front().y;
			q.pop();
			if (cx == x && cy == y) {
				flag = true;
				break;
			}
			for (int j = 0; j < 4; j++) {
				int nx = cx + dx[j];
				int ny = cy + dy[j];
				if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
					if (!visited[nx][ny] && arr[nx][ny] != 1) {
						q.push({ nx,ny });
						visited[nx][ny] = true;
					}
				}
			}
		}
		level++;
	}

	if (flag) return level - 1;
	else return 10000000;

}

//택시로부터 각각의 사람들까지의 거리 계산
void cal_dist() {
	dist_info.clear();
	int dist;
	for (int i = 0; i < m; i++) {
		//탑승한사람 제외
		if (costomer_info[i].use) continue;
		//거리 계산하고 벡터에 저장
		dist = bfs(costomer_info[i].x, costomer_info[i].y);
		dist_info.push_back({ dist,i,costomer_info[i].x,costomer_info[i].y });

	}

}

int main() {
	//freopen("input.txt", "r", stdin);      
	scanf("%d %d %d", &n, &m, &energy);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &arr[i][j]);
		}
	}
	int taxi_x, taxi_y;
	scanf("%d %d", &taxi_x, &taxi_y);
	taxi_pos.push_back({ taxi_x - 1, taxi_y - 1 });
	int cos_x, cos_y, tar_x, tar_y;
	for (int i = 0; i < m; i++) {
		scanf("%d %d %d %d", &cos_x, &cos_y, &tar_x, &tar_y);
		costomer_info.push_back({ cos_x - 1,cos_y - 1,false });
		target_pos.push_back({ tar_x - 1,tar_y - 1 });
	}


	for (int i = 0; i < m; i++) {
		cal_dist();   //택시로부터 사용하지 않은 사용자들 거리 계산
		sort(dist_info.begin(), dist_info.end(), cmp); // 정렬 하면 맨 첫번째에 있는 데이터가 가장 우선순위 높은 손님
		int dist, idx, x, y;
		dist = dist_info[0].dist;
		idx = dist_info[0].idx;
		x = dist_info[0].x;
		y = dist_info[0].y;
		//printf("%d %d %d %d\n", dist, idx, x, y);
		if (energy < dist) {
			energy = -1;
			break;
		}

		//택시 손님데리러 이동
		energy -= dist;
		costomer_info[idx].use = true;
		taxi_pos[0].x = x;
		taxi_pos[0].y = y;

		//택시 목적지로 이동
		dist = bfs(target_pos[idx].x, target_pos[idx].y);
		x = target_pos[idx].x;
		y = target_pos[idx].y;
		if (energy < dist) {
			energy = -1;
			break;
		}

		energy -= dist;
		taxi_pos[0].x = x;
		taxi_pos[0].y = y;
		energy += dist * 2;

	}
	printf("%d\n", energy);
	return 0;
}*/
