

if __name__ == "__main__":

	with open('pred.txt', 'r') as inp , open('real_pred.txt', 'w') as out:

		for line in inp:

			d = ""
			temp = line.split(" ")
			for word in temp:

				if word[0] == '▁':
					d += ' '
					d += word[1:]

				else:
					d += word

			out.write(d)