//
// Created by severuscat on 15.12.19.
//

#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

pair<ll, ll> find_p_q(ll n) {
    for (ll i = 2; i * i < n; ++i) {
        if (n % i == 0) {
            return {i, n / i};
        }
    }
    return {n, n};
}

ll gcdex (ll a, ll b, ll& x, ll& y) {
    if (a == 0) {
        x = 0; y = 1;
        return b;
    }
    ll x1, y1;
    ll d = gcdex (b%a, a, x1, y1);
    x = y1 - (b / a) * x1;
    y = x1;
    return d;
}

ll mul(ll a, ll b, ll n) {
    ll res = 0;
    while (b > 0) {
        if (b % 2) {
            res += a;
            res %= n;
            --b;
        }
        b = b / 2;
        a = (a * 2) % n;
    }
    return res % n;
}

ll pow(ll a, ll p, ll n) {
    if (p == 0) return 1;
    ll x = pow(a, p / 2, n);
    if (p % 2) return mul(x, mul(x, a, n), n);
    return mul(x, x, n);
}


int main() {
    ll n, e, m;
    cin >> n >> e >> m;

    pair<ll, ll> p_q = find_p_q(n);
    ll phi_n = (p_q.first - 1) * (p_q.second - 1);
    ll d, y;
    gcdex(e, phi_n, d, y);
    d = (d % phi_n + phi_n) % phi_n;
    cout << pow(m, d, n) % n;
    return 0;
}
