infile=open('old_data.txt','r')
outfile=open('data.txt','w')
lines=infile.readlines()
for line in lines:
    line=line.split(',')
    line[2]=str(int((int(line[2])*0.0001))*10000)
    new_line=line[0]+','+line[2]+','+line[5]+','+line[8]+','+line[9]+','+line[13]+'\n'
    outfile.write(new_line)



