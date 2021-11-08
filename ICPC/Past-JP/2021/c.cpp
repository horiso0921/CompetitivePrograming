
#include <bits/stdc++.h>
using namespace std;

struct Tree {
    Tree* up;
    Tree* left;
    Tree* right;
    bool plass;
    bool leaf;
    int val;
};

Tree* parse_non_root(const string& s, int& i, Tree* up) {
    auto ret = new Tree();

    ret->up = up;
    assert(ret->up);

    // non-leaf (l op r)
    if (s[i] == '(') {
        // (
        i++;

        // l
        ret->left = parse_non_root(s, i, ret);

        // op
        assert(s[i] == '+' || s[i] == '-');
        ret->plass = (s[i] == '+');
        i++;

        // r
        ret->right = parse_non_root(s, i, ret);

        // )
        assert(s[i] == ')');
        i++;

        return ret;
    }

    // leaf '0' - '9'
    assert('0' <= s[i] && s[i] <= '9');
    ret->val = s[i] - '0';
    i++;
    ret->leaf = true;

    return ret;
}

Tree* parse_tree(const string& s) {
    auto root = new Tree();

    int cur = 0;

    root->up = parse_non_root(s, cur, root);
    char op1 = s[cur];
    assert(op1 == '+' || op1 == '-');
    cur++;

    root->left = parse_non_root(s, cur, root);
    char op2 = s[cur];
    assert(op2 == '+' || op2 == '-');
    cur++;

    assert(op1 == op2);

    root->right = parse_non_root(s, cur, root);
    assert(cur == (int)s.size());

    root->plass = op1 == '+';

    return root;
}

void add_nodes(Tree* t, vector<Tree*>& v) {
    v.push_back(t);

    if (!t->leaf) {
        assert(t->left);
        assert(t->right);
        add_nodes(t->left, v);
        add_nodes(t->right, v);
    }
}

vector<Tree*> Nodes(Tree* root) {
    vector<Tree*> v;

    v.push_back(root);

    assert(root->up);
    assert(root->left);
    assert(root->right);

    add_nodes(root->up, v);
    add_nodes(root->left, v);
    add_nodes(root->right, v);

    return v;
}

pair<Tree*, Tree*> childs(Tree* t, Tree* parent) {
    if (t->up == parent) {
        return make_pair(t->left, t->right);
    }
    if (t->left == parent) {
        return make_pair(t->up, t->right);
    }
    if (t->right == parent) {
        return make_pair(t->left, t->up);
    }
    assert(false);
}

pair<int, int> rec(Tree* t, Tree* left, Tree* right, map<tuple<Tree*, Tree*, Tree*>, pair<int, int>>& memo) {
    auto tup = make_tuple(t, left, right);
    if (memo.count(tup)) {
        return memo[tup];
    }

    if (t->leaf) {
        return memo[tup] = make_pair(t->val, t->val);
    }

    auto l_childs = childs(t->left, t);
    auto lp = rec(t->left, l_childs.first, l_childs.second, memo);

    auto r_childs = childs(t->right, t);
    auto rp = rec(t->right, r_childs.first, r_childs.second, memo);

    // +
    if (t->plass) {
        return memo[tup] = make_pair(lp.first + rp.first, lp.second + rp.second);
    }

    // -
    auto ma = max(lp.first - rp.second, rp.first - lp.second);
    auto mi = min(lp.second - rp.first, rp.second - lp.first);
    return memo[tup] = make_pair(ma, mi);
}

void solve(string s) {
    // parse
    auto root = parse_tree(s);
    auto nodes = Nodes(root);
    std::cout << nodes[0]->plass << std::endl;
    std::cout << nodes[0]->left->val << std::endl;
    std::cout << nodes[0]->right->val << std::endl;

    int ans = numeric_limits<int>::min();

    map<tuple<Tree*, Tree*, Tree*>, pair<int, int>> memo;
    for (size_t i = 0; i < nodes.size(); i++) {
        auto t = nodes[i];

        if (t->leaf) continue;

        auto u_childs = childs(t->up, t);
        auto up = rec(t->up, u_childs.first, u_childs.second, memo);

        auto l_childs = childs(t->left, t);
        auto lp = rec(t->left, l_childs.first, l_childs.second, memo);

        auto r_childs = childs(t->right, t);
        auto rp = rec(t->right, r_childs.first, r_childs.second, memo);

        if (t->plass) {
            ans = max(ans, up.first + lp.first + rp.first);
            continue;
        }

        ans = max(ans, up.first - lp.second - rp.second);
        ans = max(ans, lp.first - up.second - rp.second);
        ans = max(ans, rp.first - up.second - lp.second);
        std::cout << up.first << lp.second << rp.second << std::endl;
        std::cout << lp.first << up.second << rp.second << std::endl;
        std::cout << rp.first << up.second << lp.second << std::endl;
        std::cout << std::endl;
    }

    cout << ans << endl;
}

int main() {
    string s;
    while (true) {
        cin >> s;
        if (s == "-1") break;
        solve(s);
    }
}
