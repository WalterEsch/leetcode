from .stack import DESIGN_NOTE

PROBLEMS = [
    {
        "id": "implement-trie-prefix-tree", "title": "Implement Trie (Prefix Tree)", "difficulty": "Medium",
        "kind": "design", "class": "Trie",
        "desc": f"""
Build a trie (prefix tree), a tree for storing strings that makes prefix lookups fast.

- `Trie()` creates an empty trie.
- `insert(word)` adds `word`.
- `search(word)` returns `True` if `word` was inserted before.
- `startsWith(prefix)` returns `True` if any inserted word starts with `prefix`.

All strings contain only lowercase English letters.

{DESIGN_NOTE}
""",
        "starter": """
class Trie:
    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass
""",
        "tests": [
            {"operations": ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
             "arguments": [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]},
            {"operations": ["Trie", "search", "startsWith"], "arguments": [[], ["a"], ["a"]]},
            {"operations": ["Trie", "insert", "insert", "search", "search", "startsWith", "startsWith", "search"],
             "arguments": [[], ["car"], ["cart"], ["car"], ["ca"], ["cart"], ["carts"], ["cart"]]},
            {"operations": ["Trie", "insert", "startsWith", "search", "insert", "search", "startsWith"],
             "arguments": [[], ["z"], ["z"], ["zz"], ["zz"], ["zz"], ["zzz"]]},
        ],
        "hints": [
            "Each node represents a prefix and has up to 26 children, one per next letter.",
            "Mark the nodes where a complete word ends. `search` and `startsWith` walk down the same way; only the final check differs.",
            "Give each node a dictionary `children` and a boolean `end`. `insert` creates missing children as it walks. `search` needs the last node to have `end == True`; `startsWith` only needs the walk to succeed.",
        ],
        "ref": """
class Trie:
    def __init__(self):
        self.words = set()
        self.prefixes = set()

    def insert(self, word: str) -> None:
        self.words.add(word)
        for i in range(len(word) + 1):
            self.prefixes.add(word[:i])

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefixes
""",
    },
    {
        "id": "design-add-and-search-words-data-structure", "title": "Design Add and Search Words Data Structure",
        "difficulty": "Medium", "kind": "design", "class": "WordDictionary",
        "desc": f"""
Design a word dictionary that supports searching with wildcards.

- `WordDictionary()` creates an empty dictionary.
- `addWord(word)` adds `word`.
- `search(word)` returns `True` if any added word matches `word`, where each `.` in `word` matches any single letter.

Words contain lowercase letters (and `.` in searches). A search word has at most 2 dots.

{DESIGN_NOTE}
""",
        "starter": """
class WordDictionary:
    def __init__(self):
        pass

    def addWord(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass
""",
        "tests": [
            {"operations": ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
             "arguments": [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]},
            {"operations": ["WordDictionary", "search", "addWord", "search", "search"],
             "arguments": [[], ["."], ["a"], ["."], [".."]]},
            {"operations": ["WordDictionary", "addWord", "addWord", "search", "search", "search", "search"],
             "arguments": [[], ["at"], ["and"], ["a"], [".at"], ["an."], ["a."]]},
            {"operations": ["WordDictionary", "addWord", "search", "search", "search"],
             "arguments": [[], ["hello"], ["h.ll."], ["hell"], ["hello."]]},
        ],
        "hints": [
            "Store the words in a trie, as in Implement Trie.",
            "A normal letter follows one child. A `.` could be any child, so you have to try them all.",
            "Search with a recursive DFS `dfs(i, node)`. For `.`, return `True` if `dfs(i + 1, child)` succeeds for any child. At the end of the word, check the node's end-of-word flag.",
        ],
        "ref": """
import re

class WordDictionary:
    def __init__(self):
        self.words = []

    def addWord(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        return any(re.fullmatch(word, w) for w in self.words)
""",
    },
    {
        "id": "word-search-ii", "title": "Word Search II", "difficulty": "Hard",
        "desc": """
You are given an `m x n` grid of letters `board` and a list of `words`. Return every word from `words` that can be spelled on the board.

A word is spelled by moving between horizontally or vertically adjacent cells, and the same cell can't be used twice in one word. Return the words in any order.

**Constraints**

- `1 <= m, n <= 12`
- `1 <= len(words) <= 3 * 10^4`, words are distinct, each 1 to 10 lowercase letters.
""",
        "sig": "def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:",
        "compare": "unordered",
        "tests": [
            {"board": [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
             "words": ["oath", "pea", "eat", "rain"]},
            {"board": [["a", "b"], ["c", "d"]], "words": ["abcb"]},
            {"board": [["a"]], "words": ["a", "aa"]},
            {"board": [["a", "b"], ["c", "d"]], "words": ["ab", "abdc", "acdb", "ad", "ba", "dcab"]},
            {"board": [["a", "a"]], "words": ["aaa", "aa"]},
            {"board": [["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]],
             "words": ["oa", "oaa", "oath", "bake", "kar", "flv", "hkra"]},
        ],
        "expect": {0: ["eat", "oath"], 1: []},
        "hints": [
            "Running a separate Word Search for every word repeats a lot of work when words share prefixes.",
            "Put all the words into a trie. Then one DFS from each cell can follow the trie and find every word along that path at once.",
            "DFS from every cell while walking down the trie; stop as soon as the current letters are not a prefix of any word. Mark cells as visited during the DFS, and remove found words from the trie (or a result set) to avoid duplicates.",
        ],
        "ref": """
class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        def exists(w):
            def dfs(r, c, i):
                if i == len(w):
                    return True
                if not (0 <= r < m and 0 <= c < n) or board[r][c] != w[i]:
                    return False
                ch, board[r][c] = board[r][c], "#"
                ok = any(dfs(r + dr, c + dc, i + 1) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
                board[r][c] = ch
                return ok
            return any(dfs(r, c, 0) for r in range(m) for c in range(n))
        return [w for w in words if exists(w)]
""",
    },
]
