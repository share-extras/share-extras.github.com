import json
import urllib
import urllib2, base64
import os, os.path

dl_screenshots = False
username = ''
password = ''
agent = 'curl/7.21.4 (universal-apple-darwin11.0) libcurl/7.21.4 OpenSSL/0.9.8r zlib/1.2.5'

opener = urllib2.build_opener(urllib2.HTTPSHandler(debuglevel=0))
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
opener.addheaders = [('Authorization', 'Basic %s' % base64string), ('User-Agent', agent)]
# Install the opener.
urllib2.install_opener(opener)

def fetch_contributors(pname):
	contributors = json.loads(opener.open('https://api.github.com/repos/%s/contributors' % (pname)).read())
	names = [ '<a href="%s">%s</a>' % (c['html_url'], c['login']) for c in contributors ]
	return ', '.join(names)

resp = None
resp = urllib2.urlopen('https://api.github.com/orgs/share-extras/repos')
repos = json.loads(resp.read())
for r in repos:
	repo_name = r['name']
	print repo_name
	# Create container
	if not os.path.exists('addons/%s' % (repo_name)):
		os.mkdir('addons/%s' % (repo_name))
	# Create page placeholder - contains YAML front-matter only, content is included later from README.md
	indexf = open('addons/%s/index.html' % (repo_name), 'w')
	fm = {
		'category': 'addon',
		'projectname': str(repo_name),
		'projecttitle': str(repo_name),
		'projectdesc': str(r['description']),
		'title': 'Share Extras - %s' % (repo_name),
		'contributors': fetch_contributors(r['full_name']),
		'dltypes': 'jar',
		'layout': 'addon'
	}
	indexf.write("---\n" + "\n".join(['%s: %s' % (k, v) for (k, v) in fm.items()]) + "\n---\n" + '{%% include addons/%s/README.md %%}' % (repo_name))
	indexf.close()
	# Create includes container
	if not os.path.exists('_includes/addons/%s' % (repo_name)):
		os.mkdir('_includes/addons/%s' % (repo_name))
	# Create README.md in includes
	try:
		readme = urllib2.urlopen('https://github.com/%s/raw/master/README.md' % (r['full_name']))
		mdf = open('_includes/addons/%s/README.md' % (repo_name), 'w')
		mdf.write(readme.read())
		mdf.close()
	except Exception, e:
		pass
	# Download screenshots
	if dl_screenshots:
		try:
			screenshots = json.loads(urllib2.urlopen('https://api.github.com/repos/%s/contents/screenshots' % (r['full_name'])).read())
			# Create screenshots directory
			if not os.path.exists('addons/%s/screenshots' % (repo_name)):
				os.mkdir('addons/%s/screenshots' % (repo_name))
			for sf in screenshots:
				if sf['type'] == 'file':
					filename = sf['name']
					url = sf['html_url'].replace('/blob/', '/raw/')
					sff = open('addons/%s/screenshots/%s' % (repo_name, filename), 'wb')
					sff.write(urllib2.urlopen(url).read())
					sff.close()
		except Exception, e:
			pass