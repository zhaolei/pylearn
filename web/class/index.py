import web

class index:
	def GET(self):
		param = web.input()
		name = param.get('name', '')
		return "[%s]"%name
