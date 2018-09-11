import re

s1 = "https://github.com/aminovE/myfirstpythonrepo.git"

name_pattern = r"[A-Za-z0-9_-]+"

re_pattern = r"https://github.com/(?P<username>%s)/(?P<repo>%s).git" % \
		(name_pattern, name_pattern)

p = re.compile(re_pattern)

m = re.search(p, s1)
					
s2_pattern = "git@github.com:%s/%s.git"

ssh_path = s2_pattern % (m.group("username"), m.group("repo"))

print(ssh_path)

