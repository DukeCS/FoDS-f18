test = {
  'name': 'Question 1.1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 < expected_row_sum
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0.99 <= expected_row_sum <= 1.01
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
