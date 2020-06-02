import sys
import os
import shutil
import argparse

def main():
	parse = argparse.ArgumentParser(description='Converter of python scripts to exe')
	parse.add_argument("-s", "--script", metavar="string", help="python script", type=str)
	parse.add_argument("-i", "--icon", metavar="string", help="exe icon", type=str)
	parse.add_argument("-n", "--name", metavar="string", help="exe name", type=str)

	def error():
		parse.print_help()
		input("Press [Enter] to exit...")
		sys.exit()

	def add_extension(path, extension):
		if not path.endswith(extension):
			path += extension
		return path

	if not len(sys.argv) > 1:
		error()

	args = parse.parse_args()

	script = args.script
	ico = args.icon
	name = args.name

	if not script:
		error()

	script = add_extension(script, '.py')

	command = 'pyinstaller -F '

	if not ico == None and not ico == '':
		ico = add_extension(ico, '.ico')
		command += '-i {} '.format(ico)
	if name == None or name == '':
		name = os.path.splitext(script)[0]

	name = add_extension(name, '.exe')

	command += '-n {} {}'.format(name, script)

	os.system(command)

	shutil.move(os.path.join("./dist/", name), os.path.join("./", name))

	for file in os.listdir('./'):
		if file.endswith(".spec"):
			os.remove(file)

	shutil.rmtree('./build')
	shutil.rmtree('./__pycache__')
	os.rmdir('./dist')

if __name__ == '__main__':
	main()