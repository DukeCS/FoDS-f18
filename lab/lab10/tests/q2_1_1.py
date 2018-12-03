test = {
  'name': 'Question 2.1.1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 < country_distance < 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(country_distance, 0.03382894432459689)
          True
          """,
          'hidden': True,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
