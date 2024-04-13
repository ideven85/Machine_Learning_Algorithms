#!/usr/bin/env python3
import os
import copy
import math
import rec as quiz
import types
import pickle
import hashlib

import pytest

from collections import Counter

TEST_DIRECTORY = os.path.dirname(__file__)


def valid_mapping(results, people, food):
    if results is None:
        return "invalid results: got None, expected something else"

    invalid = set(results) - set(people)
    if invalid:
        return "invalid people in response: %s" % invalid

    not_fed = set(people) - set(results)
    if not_fed:
        return "these people did not get fed: %s" % not_fed

    for p, f in results.items():
        if f not in people[p]:
            return "%s does not want %s but was given them" % (p, f)

    hist = Counter(results.values())
    for f, count in hist.items():
        if count > food[f]:
            return '%s was assigned more than %s times' % (f, food[f])

    return None

def _run_test(number):
    with open(os.path.join(TEST_DIRECTORY, 'test_inputs', f'potluck_{number:03d}.pickle'), 'rb') as f:
        inp = pickle.load(f)
    inp2 = copy.deepcopy(inp)

    result = quiz.feed(*inp)

    with open(os.path.join(TEST_DIRECTORY, 'test_outputs', f'potluck_{number:03d}.pickle'), 'rb') as f:
        expected = pickle.load(f)

    #assert inp == inp2, 'Make sure your function does not mutate the inputs!'

    if expected is False:
        assert result is None, 'For inputs:\n%s\n%s\nexpected None, got %s' % (*inp2, result)
    else:
        msg = valid_mapping(result, *inp2)
        assert msg is None, 'For inputs:\n%s\n%s\n%s' % (*inp2, msg)

def test_examples():
    res1 = quiz.feed({'alice': ['pickles'], 'bob': ['ketchup']},
                     {'pickles': 1, 'ketchup': 1})
    assert res1 == {'alice': 'pickles', 'bob': 'ketchup'}

    res2 = quiz.feed({'alice': ['pickles'], 'bob': ['pickles']},
                     {'pickles': 1, 'ketchup': 1})
    assert res2 is None

    res3 = quiz.feed({'alice': ['pickles'], 'bob': ['pickles']},
                     {'pickles': 2, 'ketchup': 1})
    assert res3 == {'alice': 'pickles', 'bob': 'pickles'}

    res4 = quiz.feed({
        'alice': ['pickles', 'ketchup'],
        'bob': ['chips', 'onions'],
        'candace': ['pie', 'broccoli'],
        'dave': ['pickles'],
        'emery': ['onions'],
        'fergus': ['pie'],
    }, {
        'pickles': 1,
        'ketchup': 1,
        'chips': 1,
        'onions': 1,
        'pie': 1,
        'broccoli': 1,
    })
    assert res4 == {
        'alice': 'ketchup',
        'bob': 'chips',
        'candace': 'broccoli',
        'dave': 'pickles',
        'emery': 'onions',
        'fergus': 'pie',
    }

    res5 = quiz.feed({
        'alice': ['cake', 'cheese', 'pie', 'sandwiches'],
        'bob': ['cake', 'cheese', 'pie'],
        'candace': ['cake', 'cheese'],
        'dave': ['cake', 'cheese'],
        'emery': ['cake', 'cheese']
    }, {'cake': 2, 'cheese': 1, 'pie': 1, 'sandwiches': 1})
    assert res5['alice'] == 'sandwiches'
    assert res5['bob'] == 'pie'
    assert sorted((res5['candace'], res5['dave'], res5['emery'])) == ['cake', 'cake', 'cheese']

@pytest.mark.parametrize('test_num', range(185))
def test_big(test_num):
    _run_test(test_num)
