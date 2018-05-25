import sys

# def message_utlisateur():
# 	user_Input = raw_input('Entrez une lettre pour faire un diamand =]:')
# 	print user_Input

def print_diamond(letter):
	if letter == "A":
		print letter
		return letter
	else : 
		diamond_B = "\n A \nB B\n A \n"
		print diamond_B
		return diamond_B   	

# if __name__ == '__main__':
# 	message_utlisateur()
