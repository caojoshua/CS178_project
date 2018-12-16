

attr_names = "A,B,C,D,E,F,G,H,I,J,K,L,M,N\n"

def build_files():
	f = open("X_train.txt", "r")
	f2 = open("X_train.csv", "w")
	f2.write(attr_names)
	f2.write(f.read().replace(" ", ","))
	
	f = open("X_test.txt", "r")
	f2 = open("X_test.csv", "w")
	f2.write(attr_names)
	f2.write(f.read().replace(" ", ","))
	
	f = open("Y_train.txt", "r")
	f2 = open("Y_train.csv", "w")
	f2.write("Output\n")
	f2.write(f.read().replace(" ", ","))
	
def convert_categorical():
	f = open("Y_train.csv", "r")
	f2 = open("Y_train_cat.csv", "w")
	f2.write(f.read().replace("0", "zero").replace("1", "one"))

if __name__=="__main__":
	# build_files()
	convert_categorical()