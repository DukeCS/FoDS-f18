test = {
  'name': 'Question 2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> unemployment.select('Date', 'NEI', 'NEI-PTER').take(0)
          Date       | NEI     | NEI-PTER
          1994-01-01 | 9.90147 | 11.0475
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
