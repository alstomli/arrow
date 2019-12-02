# -*- coding: utf-8 -*-
import arrow
utc = arrow.utcnow()
class ArrowDehumanizeTestsWithLocale(Chai):
    def setUp(self):
        super(ArrowDehumanizeTestsWithLocale, self).setUp()

        self.datetime = datetime(2013, 1, 1)

    def test_now(self):

        arw = arrow.Arrow(2013, 1, 1, 0, 0, 0)

        result = arw.dehumanize()

        self.assertEqual(result, arw)

    def test_days(self):
        arw = arrow.Arrow(2013, 1, 2, 0, 0, 0)
        arw_1 = arrow.Arrow(2013, 1, 3, 0, 0, 0)
        arw_0 = arrow.Arrow(2013, 1, 1, 0, 0, 0)

        result = arw_1.dehumanize('1 days ago')
        result_1 = arw_0.dehumanize('in 1 days')

        self.assertEqual(result, arw_0)
        self.assertEqual(result_1, arw)

    def test_years(self):
        arw = arrow.Arrow(2014, 1, 1, 0, 0, 0)
        arw_1 = arrow.Arrow(2015, 1, 1, 0, 0, 0)
        arw_0 = arrow.Arrow(2013, 1, 1, 0, 0, 0)

        result = arw_1.dehumanize('1 years ago')
        result_1 = arw_0.dehumanize('in 1 years')

        self.assertEqual(result, arw_0)
        self.assertEqual(result_1, arw)