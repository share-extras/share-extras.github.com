import json
import urllib
import urllib2, base64
import os, os.path
import getpass
import sys
import types

dl_screenshots = False
username = raw_input('Enter GitHub username: ')
password = getpass.getpass('Enter GitHub password: ')
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

def update_repos(repos):
    for r in repos:
        update_repo(r)

def update_repo(r):
    repo_name = r['name']
    print repo_name
    is_sdk = str(repo_name).startswith('sdk-')
    dirname = 'addons' if not is_sdk else 'sdk'
    # Create container
    if not os.path.exists('%s/%s' % (dirname, repo_name)):
            os.mkdir('%s/%s' % (dirname, repo_name))
    # Create page placeholder - contains YAML front-matter only, content is included later from README.md
    yaml = []
    # Read in the existing content, if it exists
    try:
        indexf = open('%s/%s/index.html' % (dirname, repo_name), 'r')
        lines = indexf.readlines()
        for line in lines:
            if len(line.strip()) > 0:
                kv = line.strip().split(':', 1)
                if len(kv) == 2:
                    yaml.append((kv[0].strip(), kv[1].strip()))
        indexf.close()
    except IOError, e: # File does not exist
        pass
    # Write the file
    indexf = open('%s/%s/index.html' % (dirname, repo_name), 'w')
    # New values
    fm = {
            'category': 'addon' if not is_sdk else 'sdk-project',
            'projectname': str(repo_name),
            'projecttitle': str(repo_name),
            'projectdesc': str(r['description']),
            'title': 'Share Extras - %s' % (repo_name),
            'contributors': fetch_contributors(r['full_name']),
            'dltypes': 'jar',
            'layout': 'addon',
            'updated_at': str(r['updated_at']),
            'pushed_at': str(r['pushed_at'])
    }
    # Overwrite any items
    for (k, v) in fm.items():
        for i in range(len(yaml)):
            if k == yaml[i][0]:
                yaml[i] = (k, v)
                break
        else:
             yaml.append((k, v))
    indexf.write("---\n" + "\n".join(['%s: %s' % (k, v) for (k, v) in yaml]) + "\n---\n" + '{%% include %s/%s/README.md %%}' % (dirname, repo_name))
    indexf.close()
    # Create includes container
    if not os.path.exists('_includes/%s/%s' % (dirname, repo_name)):
            os.mkdir('_includes/%s/%s' % (dirname, repo_name))
    # Create README.md in includes
    try:
            readme = urllib2.urlopen('https://github.com/%s/raw/master/README.md' % (r['full_name']))
            mdf = open('_includes/%s/%s/README.md' % (dirname, repo_name), 'w')
            mdf.write(readme.read())
            mdf.close()
    except Exception, e:
            pass
    # Download screenshots
    if dl_screenshots:
            try:
                    screenshots = json.loads(urllib2.urlopen('https://api.github.com/repos/%s/contents/screenshots' % (r['full_name'])).read())
                    # Create screenshots directory
                    if not os.path.exists('%s/%s/screenshots' % (dirname, repo_name)):
                            os.mkdir('%s/%s/screenshots' % (dirname, repo_name))
                    for sf in screenshots:
                            if sf['type'] == 'file':
                                    filename = sf['name']
                                    url = sf['html_url'].replace('/blob/', '/raw/')
                                    sff = open('%s/%s/screenshots/%s' % (dirname, repo_name, filename), 'wb')
                                    sff.write(urllib2.urlopen(url).read())
                                    sff.close()
            except Exception, e:
                    pass

def process(url):
    resp = urllib2.urlopen(url)
    data = json.loads(resp.read())
    if isinstance(data, types.ListType):
        update_repos(data)
    else:
        update_repo(data)
    # Check if there is another page
    links = resp.info().getheader('Link')
    if links is not None:
        linkslist = dict([ [l.split('; ')[1].replace('rel="', '').replace('"', ''), l.split('; ')[0].replace('<', '').replace('>', '')] for l in links.split(', ') ])
        if 'next' in linkslist:
            process(linkslist['next'])

if len(sys.argv) > 1:
    for p in sys.argv[1:]:
        if not p.startswith('-'):
            process('https://api.github.com/repos/share-extras/{0}'.format(p))
else:
    process('https://api.github.com/orgs/share-extras/repos')

