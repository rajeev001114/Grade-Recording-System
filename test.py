from locust import HttpLocust, TaskSet, task



class WebsiteTasks(TaskSet):

	def on_start(self):
		r = self.client.get('')
    		self.client.headers['Referer'] = self.client.base_url
		self.client.post("/", {
		    "username": "rahul@gmail.com",
		    "password": "rahul",
		    "csrfmiddlewaretoken": r.cookies["csrftoken"]
		})

	@task
	def in_ev_m(self):
		r = self.client.get('')
		self.client.headers['Referer'] = self.client.base_url
		self.client.post("/TCH/insert_evaluation_marks/", {
		    "username": "rahul@gmail.com",
		    "password": "rahul",
		    "csrfmiddlewaretoken": r.cookies["csrftoken"]
		})
	@task
	def cr_gp(self):
		r = self.client.get('')
		self.client.headers['Referer'] = self.client.base_url
		self.client.post("/MSG/create_grade_policy/", {
		    "username": "rahul@gmail.com",
		    "password": "rahul",
		    "csrfmiddlewaretoken": r.cookies["csrftoken"]
		})
	@task
	def up_std_m(self):
		r = self.client.get('')
		self.client.headers['Referer'] = self.client.base_url
		self.client.get("/TCH/update_student_marks", {
		    "username": "rahul@gmail.com",
		    "password": "rahul",
		    "csrfmiddlewaretoken": r.cookies["csrftoken"]
		})
	@task
	def in_weight(self):
		r = self.client.get('')
		self.client.headers['Referer'] = self.client.base_url
		self.client.post("/MSG/insert_weight/", {
		    "username": "rahul@gmail.com",
		    "password": "rahul",
		    "csrfmiddlewaretoken": r.cookies["csrftoken"]
		})
	@task
	def in_bmplcy(self):
		r = self.client.get('')
		self.client.headers['Referer'] = self.client.base_url
		self.client.post("/MSG/insert_bmpolicy/", {
		    "username": "rahul@gmail.com",
		    "password": "rahul",
		    "csrfmiddlewaretoken": r.cookies["csrftoken"]
		})
	@task
	def in_bmm(self):
		r = self.client.get('')
		self.client.headers['Referer'] = self.client.base_url
		self.client.post("/MSG/insert_bmmarks/", {
		    "username": "rahul@gmail.com",
		    "password": "rahul",
		    "csrfmiddlewaretoken": r.cookies["csrftoken"]
		})
	@task
	def dis_bm_wt(self):
		r = self.client.get('')
		self.client.headers['Referer'] = self.client.base_url
		self.client.post("/MSG/submit_bmpolicy/", {
		    "username": "rahul@gmail.com",
		    "password": "rahul",
		    "csrfmiddlewaretoken": r.cookies["csrftoken"]
		})

	@task
	def cr_fnl_msht(self):
		r = self.client.get('')
		self.client.headers['Referer'] = self.client.base_url
		self.client.post("/MSG/create_composite_marksheet/", {
		    "username": "rahul@gmail.com",
		    "password": "rahul",
		    "csrfmiddlewaretoken": r.cookies["csrftoken"]
		})


	
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 1000
    max_wait = 20000

