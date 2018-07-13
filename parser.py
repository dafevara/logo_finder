import re

from bs4 import BeautifulSoup as soup
from helper import Helper


class Parser:

  helper = Helper()

  def __bs_scope(self, bs_obj):
    _scope = bs_obj

    if hasattr(bs_obj, 'header') and bs_obj.header is not None:
      _scope = bs_obj.header
    elif hasattr(bs_obj, 'body') and bs_obj.body is not None:
      _scope = bs_obj.body
    else:
      _scope = bs_obj


    return _scope

  def img_tags(self, bs, site):
    scope = self.__bs_scope(bs)

    _img = scope.find('img', src=re.compile(self.helper.logo_file_name_re()))

    if _img is not None:
      return self.helper.sanitize_logo_url(_img.get('src'), site)
    else:
      return ''


  def parse_logo_classname_elements(self, bs_obj):
    return None

  def parse_logo_id_elements(self, bs_obj):
    return None
