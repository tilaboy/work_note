import json

def build_trie(words):
    trie = dict()
    for word in words:
        node = trie
        for char in word:
            if char not in node:
                node[char] = dict()
            node = node[char]
    return trie

def build_condensed_trie(words):

    def _find_shared(word, node):
        partial_match = False
        for phrase in node.keys():
            if word[0] == phrase[0]:
                partial_match = True
                break
        else:
            return -1, None
        max_len = min(len(word), len(phrase))
        shared_i = 0
        for i in range(1, max_len):
            if word[i] == phrase[i]:
                shared_i = i
                i += 1
            else:
                break
        return shared_i, phrase


    trie = dict()
    for word in words:
        node = trie
        start, end, nr_c = 0, 0, len(word)
        while end < nr_c:
            i_share, node_key = _find_shared(word[start:], node)
            #print('word', word, 'node', node, 'p_w', word[start:], 'i_pos', i_share, 'key', node_key)
            end = start + i_share + 1
            if node_key is None:
                end = nr_c
                node[word[start:end]] = {'$': dict()}
            elif end == len(node_key):
                if end == nr_c:
                    node[node_key]['$'] = dict()
                else:
                    node = node[node_key]
                    start = end
            elif end == nr_c:
                node_val = node.pop(node_key)
                new_node_key = node_key[i_share:]
                node[word[start:end]] = {
                    '$': dict(), node_key[i_share + 1:]: node_val
                }
            else:
                node_val = node.pop(node_key)
                node[word[start:end]] = {
                    word[end:]: {'$': dict()}, node_key[i_share + 1:]: node_val
                }
                end = nr_c
            print(word, end, node_key, trie)
    return trie


def _ukkonen_st(word):
    start, cur, nr_w = 0, 0, len(word)
    suffix_tree = list()
    while cur < nr_w:
        suffix_tree.append(cur)
        cur += 1
    return suffix_tree

def build_suffix_tree(word, method='Ukkonen'):
    if method == 'Ukkonen':
        suffix_tree = _ukkonen_st(word)
    else:
        all_suffixes = [word[i:] for i in range(len(word))]
        suffix_tree = build_condensed_trie(all_suffixes)
    return suffix_tree


def dict_print(dict_to_print):
    print(json.dumps(dict_to_print, indent=4, sort_keys=True, default='str'))

#dict_print( build_condensed_trie(["banana", "aaaaaa", "aaabaa", "bcfeg", "bcdef", "nabd"]) )
#dict_print( build_suffix_tree('banana') )
dict_print(build_suffix_tree('abc'))
