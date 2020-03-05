import sys, tempfile, os
from pathlib import Path
from subprocess import call
from fuzzywuzzy import process

import logging
logging.disable()

EDITOR = os.environ.get('EDITOR', 'vim')
SEPARATOR = "\n/////////////////////////////\n"

class Entry():
	def __init__(self, raw_txt):
		self.body = raw_txt
		self.title = raw_txt.split("\n", 1)[0]

def ls(entries, args):
	results = process.extract(args.title, entries.keys(),
		limit=args.n)
	for idx, (entry, score) in enumerate(results):
		print("[{:d}] {}".format(idx, entry))

def edit(entries, args):
	title, score = process.extractOne(args.title, entries.keys())

	if score > 95:
		entry = entries[title]
	else:
		title = args.title
		underline = "=" * len(args.title)
		entry = Entry("{}\n{}\n".format(args.title, underline))

	initial_message = entry.body

	with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
		tf.write(initial_message.encode())
		tf.flush()
		call([EDITOR, '+set backupcopy=yes', tf.name])
		
		# do the parsing with `tf` using regular File operations.
		# for instance:
		tf.seek(0)
		edited_message = tf.read().decode("utf-8")

		entries[title] = Entry(edited_message)

def cat(entries, args):
	title, score = process.extractOne(args.title, entries.keys())
	if score > args.threshold:
		entry = entries[title]
		print(entry.body)
	else:
		print("No matching notes.")

# TODO: delete

if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers()
	parser.add_argument("--notebook_path", type=Path, default="./notes.txt")

	cat_parser = subparsers.add_parser("cat")
	cat_parser.add_argument("title", type=str)
	cat_parser.add_argument("--threshold", "-t", default=50, type=int)
	cat_parser.set_defaults(func=cat)

	edit_parser = subparsers.add_parser("edit")
	edit_parser.add_argument("title", type=str)
	edit_parser.set_defaults(func=edit)

	ls_parser = subparsers.add_parser("ls")
	ls_parser.add_argument("title", nargs="?", default=" ")
	ls_parser.add_argument("-n", default=None, type=int)
	ls_parser.set_defaults(func=ls)

	args = parser.parse_args()

	if not args.notebook_path.exists():
		args.notebook_path.touch()

	with open(args.notebook_path, "r+") as f:
		data = f.read()
		entries = {
			entry.title: entry
			for entry in map(Entry, data.split(SEPARATOR))
		}
		args.func(entries, args)

		f.seek(0)
		f.write(SEPARATOR.join([entry.body for entry in entries.values()]))
		f.truncate()