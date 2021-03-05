import filecmp

pathSrc = r'C:\Users\10900225\Documents\Witch\BTX\Workspaces\Library\SRC\fromSrc.txt'
pathDst = r'C:\Users\10900225\Documents\Witch\BTX\Workspaces\Library\DST\fromSrc.txt'
pathTest = r'C:\Users\10900225\Documents\Witch\BTX\Workspaces\test.txt'
pathDocxA = r'C:\Users\10900225\Documents\Python Main Sample Folder\docx\13669 Briefing to 4102.docx'
pathDocxB = r'C:\Users\10900225\Documents\Python Main Sample Folder\docx\13669 Briefing to 4102.docx'
pathTest2 = r'C:\Users\10900225\Documents\Python Main Sample Folder\pdf\10900225_Tan Remy_SA-1C1.pdf'
pathTxt = r'C:\Users\10900225\Documents\Python Main Sample Folder\docx\sample.txt'

# compA = filecmp.cmp(pathSrc,pathDst,shallow=True)
# compB = filecmp.cmp(pathSrc,pathTest,shallow=True)


# print(f'File compareA: {compA}')
# print(f'File compareB: {compB}')

# compA = filecmp.cmp(pathSrc,pathDst,shallow=True)
# compB = filecmp.cmp(pathSrc,pathTest,shallow=False)

# print(f'File compareA: {compA}')
# print(f'File compareB: {compB}')

compC = filecmp.cmp(pathTxt,pathTxt,shallow=True)
print(f'File compareC: {compC}')

compA = filecmp.cmp(pathDocxA,pathDocxA,shallow=True)
print(f'File compareA: {compA}')

# compB = filecmp.cmp(pathDocxA,pathTest2,shallow=False)
# print(f'File compareB: {compB}')
