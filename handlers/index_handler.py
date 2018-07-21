import tornado.web
from configs.default import *

class IndexHandler(tornado.web.RequestHandler):
  async def get(self):
    print(index_title)
    self.render("../static/index.html", title=index_title)

