import codecs

import unicodedata, sys, argparse, re, os


control_categories = set(['C', 'Z'])

all_chars = (chr(i) for i in range(0x110000))
control_chars = set(c for c in all_chars if unicodedata.category(c)[0] in control_categories)
#We don't want to remove newlines or spaces
control_chars.remove(u'\n')
control_chars.remove(u' ')

def CleanControlChars(line):

	output = []

	for c in line:
		if c in control_chars:
			c = u' '
		output.append(c)

	output = u"".join(output)

	return output



def change_ascii(filename, outFile):

	inp_path = filename
	out_path = outFile

	with codecs.open(inp_path, 'r', encoding = "utf-8") as inp , codecs.open(out_path, 'w', encoding = 'utf-8') as out:

		for line in inp:
			
			#punc = '''âœ'''

			# Removing Punctuations here			
			line = re.sub(r'[^\w\s]', '', line)


			#line = line.encode("utf-8", "ignore")
			#line = line.decode()
			#line = bytes(line, 'utf-8').decode('utf-8', 'ignore')
			
			# for ele in line:
			# 	if ele in punc:
			# 		line = line.replace(ele, "")


			put = CleanControlChars(line)

			out.write(put.lower())


if __name__ == "__main__":

	change_ascii('dev_test/test.en', 'src-test.txt')

	#change_ascii('src-train.txt', 'src-train222.txt')


	# with open('src-train.txt', 'r') as inp  , open('src_train.txt', 'w') as out:

	# 	for line in inp:

	# 		out.write(line[2:-4])
	# 		out.write('\n') 
