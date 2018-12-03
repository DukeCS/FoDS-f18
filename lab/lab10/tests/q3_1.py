test = {
  'name': 'Question 3.1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0.1 <= distance_first_to_first <= 0.2
          True
          >>> np.isclose(distance(make_array(1, 2), make_array(1, 2)), 0)
          True
          >>> np.isclose(distance(make_array(1, 2, 3), make_array(2, 4, 5)), 3)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> a1 = np.array([1, 2, 3])
          >>> a2 = np.array([3, 4, 5])
          >>> a3 = np.array([9, 5, 4])
          >>> np.isclose(distance_first_to_first, 0.14822770081404466)
          True
          >>> np.isclose(distance(a1, a2), 3.46410161513)
          True
          >>> np.isclose(distance(a2, a3), 6.16441400296)
          True
          >>> np.isclose(distance(a1, a3), 8.60232526704)
          True
          """,
          'hidden': True,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
