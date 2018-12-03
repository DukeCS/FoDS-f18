test = {
  'name': 'Question 2.1.2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(distance_from_in_your_eyes('Insane In The Brain'), 0.060108782340654685)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(distance_from_in_your_eyes("Lookin' for Love"), 0.017854025951587398)
          True
          """,
          'hidden': True,
          'locked': False
        },
      ],
      'scored': True,
      'setup': r"""
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
