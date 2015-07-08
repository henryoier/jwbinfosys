# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

#class Login_info: handled by Django User

class Student_user(models.Model):
	'''
	| id | contact | name | gender | college | major | grade | gpa | credits |
	|---|---|---|---|---|---|---|---|---|
	| CHARACTER(10) | VARCHAR(11) | VARCHAR(20) | BOOLEAN | VARCHAR(50) | VARCHAR(50) | INTEGER | FLOAT | FLOAT |
	'''
	id = models.CharField(max_length=10, primary_key=True)
	contact = models.CharField(max_length=11,default='18812345678')
	name = models.CharField(max_length=20,default='张三')
	gender = models.BooleanField(default=True)
	college = models.CharField(max_length=50,default='计算机科学与技术学院')
	major = models.CharField(max_length=50,default='计算机科学与技术')
	grade = models.IntegerField(default=3)
	gpa = models.FloatField(default=4.0)
	credits = models.FloatField(default=100.0)
	isSpecial = models.BooleanField(default=False)
    photo = models.FileField(upload_to=get_photo_file_name, default=DEFAULT_PHOTO_DIR)

	def __unicode__(self):
		return u'id:%s, contact:%s, name:%s, gender:%d, college:%s, major:%s, grade:%s, gpa:%f, credits:%f'(self.id, self.contact,self.name,self.gender, self.college,self.major,self.grade, self.credits)
		# return 'id:' + self.id

	def __str__(self):
		return self.name

	class Meta:
		permissions = (
			("student_manage", "Can manage stu user info"),
		)


class Faculty_user(models.Model):
	'''
	| id | contact | name | gender | college | major | degree | title | 
	|---|---|---|---|---|---|---|---|
	| CHARACTER(6) | VARCHAR(11) | VARCHAR(20) | BOOLEAN | VARCHAR(50) | VARCHAR(50) | VARCHAR(20) | VARCHAR(20) |
	'''
	id = models.CharField(max_length=6, primary_key=True)
	contact = models.CharField(max_length=11)
	name = models.CharField(max_length=20)
	gender = models.BooleanField()
	college = models.CharField(max_length=50,default="计算机科学与技术学院")
	major = models.CharField(max_length=50,default='计算机科学与技术')
	degree = models.CharField(max_length=20,default='博士')
	title = models.CharField(max_length=20, default="研究员")
	isSpecial = models.BooleanField(default=False)
	photo = models.FileField(upload_to=get_photo_file_name, default=DEFAULT_PHOTO_DIR)

	def __unicode__(self):
		return u'id:%s, contact:%s, name:%s, gender:%d, college:%s, major:%s, degree:%s, title:%s'%(self.id, self.contact,self.name,self.gender, self.college,self.major,self.degree, self.title)
		# return 'id:' + self.id

    def __str__(self):
		return self.name

	class Meta:
		permissions = (
			("faculty_manage", "Can manage faculty user info"),
		)
	major = models.CharField(max_length=50)
	degree = models.CharField(max_length=20)
	title = models.CharField(max_length=20)

#class Admin_user: disabled temporarily

class Course_info(models.Model):
	'''
	| course_id | name | credits | time | semester | textbook | college |
	|---|---|---|---|---|---|
	| CHARACTER(8) | VARCHAR(110) | FLOAT | INTEGER | VARCHAR(110) | VARCHAR(50) |
	'''
	course_id = models.CharField(max_length=8, primary_key=True)
	name = models.CharField(max_length=110)
	credits = models.FloatField()
	time = models.IntegerField()
	semester = models.IntegerField()
	textbook = models.CharField(max_length=110)
	college = models.CharField(max_length=50)

class classroom(models.Model):
	'''
	| id | name | type | capacity | campus |
	| VARCHAR(20) | VARCHAR(20) | VARCHAR(20) | interget | VARCHAR(20) |
	'''
	#id = models.CharField(max_length=20,primary_key=True)
	name = models.CharField(max_length=20)
	type = models.CharField(max_length=20, default = 'classroom')
	capacity = models.IntegerField()
	campus = models.CharField(max_length=20)

class Class_info(models.Model):
	'''
	| class_id | course_id | teacher | time | room | examdate | examtime | examroom | capacity |
	|---|---|---|---|---|---|---|---|---|
	| CHARACTER(10) | CHARACTER(8) | VARCHAR(20) | INTEGER | VARCHAR(20) | DATETIME(TEXT) | INTEGER | VARCHAR(20) | INTEGER |
	'''
	course_id = models.CharField(max_length=20)
	teacher = models.CharField(max_length=20)
	classTime = models.TextField()
	classroom = models.CharField(max_length=20)
	capacity = models.IntegerField()

class Pre_requisites(models.Model):
	'''
	| id | prereq |
	|---|---|
	| CHARACTER(8) | CHARACTER(8) |
	'''
	course_id = models.CharField(max_length=8)
	prereq = models.CharField(max_length=8)

class class_table(models.Model):
	'''
	| student_id | class_id |
	|---|---|
	| CHARACTER(10) | CHARACTER(10) |
	'''
	student_id = models.CharField(max_length=20)
	class_id = models.CharField(max_length=20)

class course_admin(models.Model):
	'''
	| Faculty_id | admin |
	| CHARACTER(6) | BOOLEAN |
	'''
	Faculty_id = models.CharField(max_length=20)
	admin = models.BooleanField(default=True)


class Application(models.Model):
	'''

	'''
	#class id
	#cl_ID=models.CharField(max_length=20,primary_key=True)
	id = models.CharField(max_length=20, primary_key=True)
	#course id
	cuz_ID=models.CharField(max_length=20)
	# class time save as json
	classTime=models.TextField()
	#class hour
	classHour = models.IntegerField()
	# class capacity
	class_capacity=models.IntegerField()
	#
	campus=models.CharField(max_length=20)
	# teacher id
	teacherID=models.CharField(max_length=20)
	# term 
	#term = models.CharField(max_length=20)
