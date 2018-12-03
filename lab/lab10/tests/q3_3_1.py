test = {
  'name': 'Question 3.3.1',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 <= proportion_correct <= 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> r = np.count_nonzero(test_guesses == test_lyrics.column('Genre')) / test_lyrics.num_rows
          >>> proportion_correct == r
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
