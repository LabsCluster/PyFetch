#__author__=DGideas

def fetch(website,outfile,useragent="Links (2.8; Linux 2.6.32-504.30.3.el6.x86_64 x86_64; GNU C 4.4.7; text)"):
	import subprocess;
	subprocess.check_output('wget --user-agent="'+str(useragent)+'" --output-document='+str(outfile)+' -q "'+str(website)+'"',shell=True);
	return;

