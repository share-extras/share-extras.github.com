#! /usr/bin/env python
# update-projects.py

"""
Import a site definition and site content from the local file system.

Usage: python update-projects.py [project1 [project2] ...]
"""

import json
import urllib
import urllib2, base64
import os, os.path
import getpass
import sys
import types
import getopt

def usage():
    print __doc__

def fetch_contributors(pname):
	contributors = json.loads(opener.open('https://api.github.com/repos/%s/contributors' % (pname)).read())
	names = [ '<a href="%s">%s</a>' % (c['html_url'], c['login']) for c in contributors ]
	return ', '.join(names)

def update_repos(repos, dl_screenshots=False):
    for r in repos:
        update_repo(r, dl_screenshots)

def update_repo(r, dl_screenshots=False):
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

def process(url, dl_screenshots=False):
    resp = urllib2.urlopen(url)
    data = json.loads(resp.read())
    if isinstance(data, types.ListType):
        update_repos(data, dl_screenshots)
    else:
        update_repo(data, dl_screenshots)
    # Check if there is another page
    links = resp.info().getheader('Link')
    if links is not None:
        linkslist = dict([ [l.split('; ')[1].replace('rel="', '').replace('"', ''), l.split('; ')[0].replace('<', '').replace('>', '')] for l in links.split(', ') ])
        if 'next' in linkslist:
            process(linkslist['next'])

dl_screenshots = False
username = None
password = None
agent = 'curl/7.21.4 (universal-apple-darwin11.0) libcurl/7.21.4 OpenSSL/0.9.8r zlib/1.2.5'

opener = urllib2.build_opener(urllib2.HTTPSHandler(debuglevel=0))

projects = [ p for p in sys.argv[1:] if not p.startswith('-') ]
options = [ o for o in sys.argv[1:] if o.startswith('-') ]

if len(sys.argv) > 1:

    # Process options
    try:
        opts, args = getopt.getopt(options, "h", ["help", "dl-screenshots", "user=", "token="])
    except getopt.GetoptError, e:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == "--dl-screenshots":
            dl_screenshots = True
        elif opt == "--user":
            username = arg
        elif opt == "--token":
            password = arg

if username is None:
    username = raw_input('Enter GitHub username: ')
if password is None:
    password = getpass.getpass('Enter GitHub password: ')

base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
opener.addheaders = [('Authorization', 'Basic %s' % base64string), ('User-Agent', agent)]
# Install the opener.
urllib2.install_opener(opener)

if len(projects) > 0:
    # Go through projects, if specified
    for p in projects:
        process('https://api.github.com/repos/share-extras/{0}'.format(p), dl_screenshots=dl_screenshots)
else:
    process('https://api.github.com/orgs/share-extras/repos', dl_screenshots=dl_screenshots)

