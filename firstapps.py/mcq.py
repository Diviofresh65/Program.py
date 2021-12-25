Q1 """Weak bases 
A. dissociate partially 
B. Ionize completely 
C. hydrolyze partially   
D. Oxidize completely """

Q2 =  """ Which of the following molecules has a triple bond in its structure?
A. CH4      
B. NH3           
C. N2         
D. O2 """

Q3 = """ Reduction is the process of 
A. loss of electrons  
B. Loss of hydrogen   
C. loss of oxygen   
D. Addition of electronegative elements """

Q4 = """The equation PV=K  illustrates                            
A.  Boyle’s law       
B. Charles’ law   
C. Dalton’s law  
D. Gay Lussac’s law """

Q5 = """At ordinary temperature water is a liquid while hydrogen sulphide is a gas. 
This is because water has 
A. weak intermolecular forces holding its molecules together
B. strong hydrogen bonds holding its molecules together 
C. induced dipole-dipole forces between its molecules 
D. ionic forces between its molecules """

Q6 = """The average kinetic energy of the particles in a
sample of a gas is a measure of its 
A. density
B. Pressure              
C. Volume   
D. Temperature """

Q7 = """The compound formed by the combination of two elements
 with a large electronegativity difference is likely to be
A. polar covalent 
B. Giant molecular 
C. covalent 
D. Ionic """



questions = {Q1:"A", Q2:"C", Q3:"C",Q4:"A",Q5:"B",Q6:"D",Q7:"D"}

name = input("Enter name: ")
print("Hello", name, "Welcome to MHS online Quiz")
score =0
for i in questions:
    print(i)
    ans = input("Enter correct answer (A/B/C/D): ")