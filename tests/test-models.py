import unittest
from models import models

Sources = models.Sources
Headlines = models.Headlines

class headlines_test(unittest.TestCase):
    def setUp(self):
        self.new_headline = Headlines("Paul","Breaking News","Curfew has been raised","watch.co.ke","img.jpg","2021-4-16")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_headline,Headlines))
    
    def test_True(self):
        self.assertEqual(self.new_headline.author,'Paul')
        self.assertEqual(self.new_headline.title,'Breaking News')
        self.assertEqual(self.new_headline.description,'Curfew has been raised')
        self.assertEqual(self.new_headline.url,'watch.co.ke')
        self.assertEqual(self.new_headline.urlToImage,'img.jpg')
        self.assertEqual(self.new_headline.publishedAt,'2021-4-16')

class source_test(unittest.TestCase):
    '''
    this function creates an object of the Sources class before each and every tesy
    '''
    def setUp(self):
        self.new_source = Sources(
            'ABC-news', 'ABC-news','News at 1', 'https://abc.com',"Kenya")

    def test_instance(self):
        '''
        this is a function to assert whether the instance is really an instance of our class
        '''
        self.assertTrue(isinstance(self.new_source, Sources))

    def test_data(self):
        '''
        this function asserts whether the value entered by the setUp method will appear if the property is called
        '''
        self.assertEqual(self.new_source.id, 'ABC-news')
        self.assertEqual(self.new_source.name, 'ABC-news')
        self.assertEqual(self.new_source.desc,'News at 1')
        self.assertEqual(self.new_source.url, 'https://abc.com')
        self.assertEqual(self.new_source.country, 'Kenya')
       

if __name__ == '__main__':
    unittest.main()