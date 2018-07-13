import cssutils
import pandas as pd
import requests
import re
import pdb

from bs4 import BeautifulSoup as soup
from helper import Helper
from parser import Parser



class LogoFinder:

  helper = Helper()
  parser = Parser()

  def __init__(self):
    self.top1k_df = self.helper.load_data().tail(500)
    self.__errors = []
    self.__success = []
    self.__results = []

  def run(self):
    for site in self.top1k_df['Domain']:

      _result = {'site': site, 'logo_url': None, 'error': None}

      try:
        res = requests.get(self.helper.formatted_url(site),  timeout=2)

        if len(res.text) >= 0 and res.status_code == 200:
          bs = soup(res.text, "lxml")
          _result['logo_url'] = self.parser.img_tags(bs, site)
          self.__success.append([_result['site'], _result['logo_url']])

        else:
          _result['error'] = str(res.status_code) + " for " + site
          self.__errors.append([_result['site'], _result['error']])

        self.__results.append([_result['site'], _result['logo_url']])

      except requests.exceptions.ConnectionError:
        _result['error'] = "Failed to establish a connection with: " + self.helper.formatted_url(site)
        self.__errors.append([_result['site'], _result['error']])
      except requests.exceptions.ReadTimeout:
        _result['error'] = "Read time out with: " + site
        self.__errors.append([_result['site'], _result['error']])

      print('.', end='')

    return None

  def errors(self):
    return self.__errors

  def success(self):
    return self.__success

  def results(self):
    return self.__results








logo = LogoFinder()

if __name__ == "__main__":
  logo.run()
  logo.helper.results_as_csv_file(logo.results())
