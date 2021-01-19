#getting the cipher values
cipher = '9MG/-5*N\')LN$#+JK4~RG`A.U|ei`&t@tG>C^8ooakZ$~r>CSpp(jbkC~&ein8BwH78]R1o1ztULc$K"7#S UL3P<:(Vh5\'i]~&)akUL*-@\'oo+JG2q%$#VnH6*-~5$#c$K"m%]*Pv8]P1d/Af]~LzODIFvX$#[VSp3j$2m%]*Pv8]Mo?BMo"89UAf]~imxG].J="8%Xk?^8G2(J&)akULc$$#U(R;MoI$zA"89UAf]~imxG].J=4Mr.k}"8K"U|eip(G`;<3D^EMo4MzAG2/G$#VnH61[(Yn85)Hzim*QzA@\'ZgIWNW\'iU|eiZ$8]$#c$ztUL/q^8@\'HzMuv7 MR;,PnXzA@$vX"8iHwAU|26%X;D@\'&)akULU(R;Lz2A9UAf]~&)akULakkfC?d1aszAG2/G$#c$K"Moooa \'i~lJ=Dz9i R'
#converting the cipher to pairs
sixteenBitpairs = [cipher[i:i+2] for i in range(0,len(cipher),2)]

#reading the books 
plain_book = open(r"book.txt", 'r') 
cipher_book = open(r"ebook.txt", 'r')

#storing the lines
pLines = plain_book.readlines()
cLines = cipher_book.readlines()

#dictionary to store the cipher to plain text matchings
cipher_dict = {}
#Checking if both the book length is equal 
if len(pLines) == len(cLines):
    #process each lines in both files one by one
    for i in range(0,len(pLines)):
        # storing the plain text line by removing the newline character in the end of line
        pL = pLines[i].rstrip()
        # storing the cipher text line by removing the newline character in the end of line
        cL = cLines[i].rstrip()
        #for odd lengths the plaintext line is padded with an 'a' at the end 
        if (len(cL) - len(pL)) == 1: 
            pL = pL + 'a'
        #for even lengths we need to remove the last two characters in the ciphertext lines 
        elif (len(cL) - len(pL)) == 2:
            cL = cL[:-2]
        
        #zero length is the gap between lines we won't get any values for dictionary that we are creating so skipping the processing 
        if len(cL) == len(pL) == 0:
            continue
        else:
            #Both the plain text and Cipher text file lines are of equal even length now. So I made two character pairs on each lines and 
            #zipped them together as a dictionary 
            for C,P in zip([cL[i:i+2] for i in range(0,len(cL),2)],[pL[i:i+2] for i in range(0,len(pL),2)]):
                cipher_dict[C] = P

resultTextPairs = []
# Using the cipher dictionary I am creating the final resultDictionary 
for sB in sixteenBitpairs:
    # result = result + cipher_dict[sB]
    resultTextPairs.append(cipher_dict[sB])

print([[s,r] for s,r in zip(sixteenBitpairs,resultTextPairs)])
print(''.join(resultTextPairs))
