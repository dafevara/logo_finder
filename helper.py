import pandas as pd

class Helper:

  WORK_DIR_PATH = '/Users/dafevara/PROJECTS/MixRank'
  TOP_1K_SITES_PATH = WORK_DIR_PATH + '/top1k-sites.csv'

  def load_data(self):
    return pd.read_csv(self.TOP_1K_SITES_PATH)

  def output_data(self, data_frame):
    data_frame.to_csv(self.WORK_DIR_PATH + '/output.csv', index=False)

  def formatted_url(self, site):
    return "http://www." + site

  def logo_file_name_re(self):
    return 'logo' + '|' + 'icon' + '|' + 'banner'

  def results_as_csv_file(self, results_list):
    _data = {'Domain': [], 'LogoUrl': []}
    _data['Domain'] = list(map(lambda r: r[0], results_list))
    _data['LogoUrl'] = list(map(lambda r: r[1], results_list))

    df = pd.DataFrame(data=_data)

    return self.output_data(df)

  def sanitize_logo_url(self, logo_url, domain):
    if len(logo_url) <= 0:
      return ''

    if logo_url[0:2] == '//':
      logo_url = logo_url[2:]

    if logo_url[0] == '/':
      logo_url = logo_url[1:]

    if domain not in logo_url and 'http' != logo_url[0:4]:
      logo_url = domain + logo_url

    if 'http://' not in logo_url and 'https://' not in logo_url:
      logo_url = 'http://' + logo_url

    return logo_url








