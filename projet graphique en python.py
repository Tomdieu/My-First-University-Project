from tkinter import *
from tkinter.ttk import Treeview,Progressbar
import sys
#from PIL import ImageTk,Image
from time import sleep
from tkinter.messagebox import *
n=1
FICCAN ="candidat.txt"
FICBACC ="bacc.txt"
FICCHOIX ="choix.txt"
FICRESU ="resultat.txt"
FICADMIS ="admis.txt"
FICMATH  ="filier mathematic.txt"
FICPHY ="filier physique.txt"
FICBIOS ="filier bio science.txt"
FICGEOS ="filier geo science.txt"
FICCHM ="filier chiemie.txt"
FICICT ="filier ict.txt"
FICINFO ="filiere informatique.txt"

S1,S2,S3=15,10,14
def combine_name(name):
	d=name.split()
	n=len(d)
	if n>=2:
		name='_'.join(d)
	else:
		name=name
	return name

def upr(variable):
	n=variable.split()
	l=len(n)
	if l>1:
		b=[i.upper() for i in n]
		return b
	else:
		return variable.upper()


def count():
	CAN=[]
	try:
		with open(FICCAN,'r') as can:
			for line in can:
				line=line.strip()
				CAN.append(line)
		return len(CAN)	
	except Exception as e:
		f = open(FICCAN,"w")
		close(f)
		return 0
	
def does_this_NCIN_exist(NCIN):
	NCIN=str(NCIN)
	CAN=[]
	BAC=[]
	CHO=[]
	"""
		another way of reading a file directly is 
		data=[line.strip() for line in open('file','')]
	"""
	check1=check2=check3=False
	with open(FICCAN,'r') as can:
		for line in can:
			line=line.strip()
			CAN.append(line)
	with open(FICBACC,'r') as bac:
		for line in bac:
			line=line.strip()
			BAC.append(line)
	with open(FICCHOIX,'r') as cho:				
		for line in cho:
			line=line.strip()
			CHO.append(line)

	for i in CAN:
		if i.split(';')[0]==NCIN:
			check1=True
			break
	for i in BAC:
		if i.split(';')[0]==NCIN:
			check2=True
	for i in CHO:
		if i.split(';')[0]==NCIN:
			check3=True

	if(check1==check2==check3==True):
		return True
	else:
		return False

def position(NCIN):
	if(does_this_NCIN_exist(NCIN)==True):
		CAN=[]
		pos=0
		with open(FICCAN,'r') as can:
			for line in can:
				line=line.strip()
				CAN.append(line)
		for i in CAN:
			if i.split(';')[0]==NCIN:
				b=i.split(';')[0]
				return pos
			else:	
				pos+=1


#-----------------fonction qui va me permettre de trier avant d'ecrier dans le fichier resultat de facon 
#-----------------a ce que tous les autre canidat soit trier dans leur filier respective


def sort_information(ncin,nom,prenom,age,moyenne,notemath,notephy,decision):
	n=len(ncin)
	#here i will used bubble sort in comparing the name

	for i in range(0,n):
		for j in range(0,n-1-i):
			if(nom[j+1]>nom[j]):
				print(nom[j+1],nom[j],nom[j+1]>nom[j])
				ncin[j],ncin[j+1]=ncin[j+1],ncin[j]
				nom[j],nom[j+1]=nom[j+1],nom[j]
				prenom[j],prenom[j+1]=prenom[j+1],prenom[j]
				age[j],age[j+1]=age[j+1],age[j]
				moyenne[j],moyenne[j+1]=moyenne[j+1],moyenne[j]
				notemath[j],notemath[j+1]=notemath[j+1],notemath[j]
				notephy[j],notephy[j+1]=notephy[j+1],notephy[j]
				decision[j],decision[j+1]=decision[j+1],decision[j]


#-------------------fin de tri

#--------------------------------classs candidat--------------------------------------------------
class CANDIAT(object):
	"""docstring for CANDIAT"""
	def __init__(self, NCIN,NOM,PRENOM,AGE):
		self.NCIN=NCIN
		self.NOM=NOM
		self.PRENOM=PRENOM
		self.AGE=int(AGE)
	
	def add(self):
		if(not(does_this_NCIN_exist(self.NCIN))):
			with open(FICCAN,'a') as f:
				print('{};{};{};{}\n'.format(self.NCIN,self.NOM,self.PRENOM,self.AGE))
				f.write('{};{};{};{}\n'.format(self.NCIN,self.NOM,self.PRENOM,self.AGE))
				
				return f'successfully added'
		else:
			print("THIS NCIN EXIST ALL READY!")
	@property
	def output(self):
		return f'{self.NCIN} {self.NOM} {self.PRENOM} {self.AGE}'
	@property
	def age(self):
		return self.AGE
	@property
	def full_name(self):
		return f'{self.NOM} {self.PRENOM}'
	@property
	def ncin(self):
		return self.NCIN
	
#-----------------------classs bacc-----------------------------------------------------

class BACC(object):
	""""""
	def __init__(self,NCIN,MOYENNE,SERIE,NOTEMATH,NOTEPHY):
		
		self.NCIN=NCIN
		self.SERIE=SERIE
		self.MOYENNE=MOYENNE
		self.NOTEMATH=NOTEMATH
		self.NOTEPHY=NOTEPHY

	def add(self):
		with open(FICBACC,'a') as f:
			if(does_this_NCIN_exist(self.NCIN)==False):
				f.write('{};{};{};{};{}\n'.format(self.NCIN,float(self.MOYENNE),self.SERIE,self.NOTEMATH,self.NOTEPHY))
	
				return f'successfully added'
			else:
	
				print("THIS NCIN EXIST ALL READY!")
	"""
	@property
	def NOTEMATH(self):
		return self.NOTEMATH
	@property
	def NOTEPHY(self):
		return self.NOTEPHY
	@property
	def MOYENNE(self):
		return self.MOYENNE
	@property
	def SERIE(self):
		return self.SERIE"""
	
#-------------------class choix -----------------------------------------------------------------------	
	
class CHOIX(object):
	"""docstring for CHOIX"""
	def __init__(self, NCIN,CHOIX2,CHOIX3):

		self.NCIN=NCIN
		self.CHOIX1="INFORMATIQUE"
		self.CHOIX2=CHOIX2
		self.CHOIX3=CHOIX3
	
	def add(self):
		with open(FICCHOIX,'a') as f:
			if(does_this_NCIN_exist(self.NCIN)==False):
				f.write('{};{};{}\n'.format(self.NCIN,self.CHOIX2,self.CHOIX3))
				
				return f'successfully added'
			else:
				print("THIS NCIN EXIST ALL READY!")
	@property
	def choix2(self):
		return self.CHOIX2
	@property
	def choix3(self):
		return self.CHOIX3

#--------------------fonction ecuperation-------------------------------------

def recuperer_candidat(Candidat):
	with open('candidat.txt','r') as f:
		for line in f:
			line=line.strip()
			Candidat.append(line)
	return len(Candidat)

def recuperer_bacc(Bacc):
	with open('bacc.txt','r') as f:
		for line in f:
			line=line.strip()
			Bacc.append(line)
	return len(Bacc)

def recuperer_choix(Choix):
	with open('choix.txt',"r") as f:
		for line in f:
			line=line.strip()
			Choix.append(line)
	return len(Choix)

#---------------fonction modifier--------------------------------------------

def clr():
	for w in tk.winfo_children():
		w.destroy()

def modifier():
	clr()
	NCIN=StringVar()
	def clean_here():
		for i in frame2.winfo_children():
			i.destroy()
	def clear0(e):
		if NcIn.get()=='Entre le NCIN du Candidat a modifier':
			NcIn.delete(0,END)
			NcIn.config(fg='black')
			NcIn.config(font=('arial',15,'normal'))

	
	frame1=Frame(tk,height=700,width=1000,bg='sky blue')
	frame1.place(x=80,y=40)
	frame2=Frame(tk,height=600,width=900,bg='light grey')
	frame2.place(x=130,y=90)
	Label(frame2,text='Modifier Candidat',bg='light grey',fg='green',font=('arial',20,'bold')).place(x=270,y=20)
	NcIn=Entry(frame2,textvariable=NCIN,font=('consolas',15),bd=0,bg='white',width=40)
	NCIN.set('Entre le NCIN du Candidat a modifier')
	NcIn.config(font=("consolas",15,'italic'))
	NcIn.config(fg='grey')
	Label(frame2,text='NCIN : ',font=('arial',20,'bold'),fg='black',bg='light grey').place(x=70,y=60)
	NcIn.place(x=190,y=66)
	NcIn.bind("<Button-1>",clear0)
	def search():
		global NCIN
		if NcIn.get()=='' or  NcIn.get()=='Entre le NCIN du Candidat a modifier':
			showerror('Alert','Veuillez entre le NCIN')
			NcIn.delete(0,END)
			NcIn.config(fg='black')
			NcIn.config(font=('arial',15,'normal'))
			NcIn.focus()
		else:
			if does_this_NCIN_exist(NcIn.get())==True:
				
				Candidat=[]
				Bacc=[]
				Choix=[]
				pos=0
				nom=[]
				ncin=[]
				prenom=[]
				age=[]
				moy1=[]
				serie1=[]
				notephy1=[]
				notemath1=[]
				choix21=[]
				choix31=[]
				j=0
				ctr=0
				NCIN=NcIn.get()

				#--------------------recuperation dans est stock dans les tableau 
				n=recuperer_candidat(Candidat)
				n1=recuperer_bacc(Bacc)
				n2=recuperer_choix(Choix)

				#------------------fin de recuperation -----------------------------

				#-----------------nettoyage de frame 2
				clean_here()
				#----------------fin de nettoyage-------------------------

				for i in Candidat:
					ncin.append(i.split(';')[0])
					nom.append(i.split(';')[1])
					prenom.append(i.split(';')[2])
					age.append(int(i.split(';')[3]))
				for i in range(len(ncin)):
					print(ncin[i],nom[i],prenom[i],age[i])
				
				pos=position(NCIN)

				for i in Bacc:
					 moy1.append(float(i.split(';')[1]))
					 serie1.append(i.split(';')[2])
					 notemath1.append(float(i.split(';')[3]))
					 notephy1.append(float(i.split(';')[4]))

				for i in Choix:
					choix21.append(i.split(';')[1])
					choix31.append(i.split(';')[2])

				#---------displaying the candidate------------------------------

				Nvnom=StringVar()
				Nvprenom=StringVar()
				Nvage=StringVar()
				Nvmoy=StringVar()
				Nvserie=StringVar()
				Nvnotem=StringVar()
				Nvnotep=StringVar()
				Nvchoix2=StringVar()
				Nvchoix3=StringVar()

				list_2=["Mathématique","Physique","Chimie","Bio Science","Geo Science","Ict"]
				list_1=["C","D","Ti","F3","GCE"]


				total=Label(frame2,text='Modifier les Informatique Du Candidat '+str(pos+1)+'/1000',fg='green',bg='light grey',font=('consolas',20,'bold'))
				total.place(x=150,y=20)
				
				#-------------------------this part concerns the candidate

				Label(frame2,text='NCIN :',font=('consolas',20,'bold'),fg='black',bg='light grey').place(x=70,y=60)
				
				n=Label(frame2,text=ncin[pos],font=('arial',15),bg='light grey',fg='black',bd=0,justify=LEFT)
				n.place(x=165,y=70)
				
				Label(frame2,text='NOM :',font=('consolas',20,'bold'),bg='light grey',fg='black').place(x=70,y=115-5)
				nm=Entry(frame2,textvariable=Nvnom,width=30,font=("arial",15),bg='white',fg='black',bd=0)
				nm.insert(0,nom[pos])
				nm.place(x=149,y=125-5)
				
				
				Label(frame2,text="PRENOM : ",font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=170-5)
				pr=Entry(frame2,textvariable=Nvprenom,font=("arial",15),bg='white',fg='black',width=30,bd=0)
				pr.insert(0,prenom[pos])
				pr.place(x=190,y=180-5)
				
				Label(frame2,text='AGE :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=225-5)
				ag=Entry(frame2,textvariabl=Nvage,font=('arial',15),bg='white',fg='black',width=5)
				ag.insert(0,age[pos])
				ag.place(x=149,y=235-5)

				#-------------------end of candidate

				#-----------------------this part concerns the information on his examination certificate

				Label(frame2,text='MOYENNE :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=280-5)
				moy=Entry(frame2,textvariable=Nvmoy,width=8,font=("arial",15),bg='white',fg='black',bd=0)
				moy.insert(0,str(moy1[pos]))
				moy.place(x=210,y=290-5)

				Label(frame2,text='SERIE BACC :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=335-5)
				list_serie=OptionMenu(frame2,Nvserie,*list_1)
				list_serie.config(width=6)
				Nvserie.set(serie1[pos])
				list_serie.place(x=250,y=341-5)

				Label(frame2,text='NOTE DE MATHEMATIQUE :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=390-5)
				notm=Entry(frame2,textvariable=Nvnotem,width=10,font=("arial",15),bg='white',fg='black',bd=0)
				notm.insert(0,str(notemath1[pos]))
				notm.place(x=445,y=396-5)

				Label(frame2,text='NOTE DE PHYSIQUE :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=390-5+55)
				notp=Entry(frame2,textvariable=Nvnotep,width=10,font=("arial",15),bg='white',fg='black',bd=0)
				notp.insert(0,str(notephy1[pos]))
				notp.place(x=445,y=396-5+55)

				#-------------------------end of examination --------------------------------------------

				#------------------------this part concerns the choice of the candidate-------------------
				Label(frame2,text='DEUXIEUME CHOIX :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=390-5+55+55)
				list_choix2=OptionMenu(frame2,Nvchoix2,*list_2)
				list_choix2.config(width=12)
				Nvchoix2.set(choix21[pos])
				list_choix2.place(x=445,y=396-5+55+55)

				Label(frame2,text='TROISIEME CHOIX :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=390-5+55+55+55)
				list_choix2=OptionMenu(frame2,Nvchoix3,*list_2)
				list_choix2.config(width=12)
				Nvchoix3.set(choix31[pos])
				list_choix2.place(x=445,y=396-5+55+55+55)

				#----------------------savegarde -------------------------------------------
				def save1():
					h1=h2=h3=h4=h5=h6=h7=h8=h9=h10=False
					h1=True
					if nm.get()=='':
						showerror("ERREUR ","Veillier Entrez Le Nom Du Candidat!")
						nm.focus()
						nom.set('')
						nm.config(fg='black')
						nm.config(font=('arial',15,'normal'))
					else:
						h2=True

					if  pr.get()=='':
						showerror('ERREUR ','Veillier Entrez Le Prenom du Candidat!')
						pr.focus()
						prenom.set('')
						pr.config(fg='black')
						pr.config(font=('arial',15,'normal'))
					else:
						h3=True

					try:
						Age=int(ag.get())
						if Age>=14 and Age<=100:
							h4=True
						else:
							showerror("AGE INVALID","Veillier Rentrez L'age,entre 14 et 100")
							age.set('')
							ag.focus()
							ag.config(fg='black')
							ag.config(font=('arial',15,'normal'))
					except:
						showerror("INCOMPATIBLE TYPE","Veillier Rentrez L'age,l'age doit etre un entier")
						age.set('')
						ag.focus()
						ag.config(fg='black')
						ag.config(font=('arial',15,'normal'))

					try:
						Moy=float(moy.get())
						if Moy>=10 and Moy<=20:
							h5=True
						else:
							showerror("MOYENNE INVALID","Veillier Rentrez une moyenne elle entre 0 et 20")
							moyenne.set('')
							moy.focus()
							moy.config(fg='black')
							moy.config(font=('arial',15,'normal'))
					except:
						showerror("INCOMPATIBLE TYPE","Veillier Rentrez la moyenne elle doit étre un nombre decimal")
						moyenne.set('')
						moy.focus()
						notp.config(fg='black')
						notp.config(font=('arial',15,'normal'))

					try:
						NM=float(notm.get())
						if NM>0 and NM<=20:
							h6=True
						else:
							showerror("NOTEMATH INVALID!","Veillier Rentrez la NOTEMATH elle doit étre entre 0 et 20")
							notemath.set('')
							notm.focus()
							notm.config(fg='black')
							notm.config(font=('arial',15,'normal'))
					except:
						showerror("INCOMPATIBLE TYPE","Veillier Rentrez la NOTEMATH elle doit étre un nombre decimal")
						notemath.set('')
						notm.focus()
						notm.config(fg='black')
						notm.config(font=('arial',15,'normal'))

					try:
						NP=float(notp.get())
						if NP>0 and NP<=20:
							h7=True
						else:
							showerror("MOYENNE INVALID","Veillier Rentrez la NOTEPHY elle doit étre entre 0 et 20")
							notephy.set('')
							notp.focus()
							notp.config(fg='black')
							notp.config(font=('arial',15,'normal'))
					except:
						showerror("INCOMPATIBLE TYPE","Veillier Rentrez la NOTEPHY elle doit étre un nombre decimal")
						notephy.set('')
						notp.focus()
						notp.config(fg='black')
						notp.config(font=('arial',15,'normal'))

					h8=True

					if Nvchoix2.get()==Nvchoix3.get():
							showerror('ERREUR',"Veillier Selectionioner Un autre choix du candidat!")
					else:
						h9=True

					if Nvchoix3.get()==Nvchoix2.get():
							showerror('ERREUR',"Veillier Selectionioner Un autre Troisieme Choix du candidat!")
							Nvchoix3.set('CHOIX3')
					else:
							h10=True
					if (h1==h2==h3==h4==h5==h6==h7==h8==h9==h10)==True:
						print('ok')
						
						nom[pos]=(nm.get()).upper()
						nom[pos]=combine_name(nom[pos])
						prenom[pos]=pr.get().upper()
						prenom[pos]=combine_name(prenom[pos])
						age[pos]=Age
						serie1[pos]=Nvserie.get()
						moy1[pos]=Moy
						notemath1[pos]=NM
						notephy1[pos]=NP
						choix21[pos]=Nvchoix2.get()
						choix31[pos]=Nvchoix3.get()
						
						#-------------here since we are modifiying the content of the file we are 
						#-------------going to open it in writing mode w
						with open(FICCAN,'w') as f:
							for i in range(len(nom)):
								f.write('{};{};{};{}\n'.format(ncin[i],upr(nom[i]),upr(prenom[i]),age[i]))
						with open(FICBACC,'w') as f1:
							for i in range(len(ncin)):
								f1.write('{};{};{};{};{}\n'.format(ncin[i],moy1[i],serie1[i],notemath1[i],notephy1[i]))
						with open(FICCHOIX,'w') as f:
							for i in range(len(ncin)):
								f.write('{};{};{}\n'.format(ncin[i],choix21[i],choix31[i]))

						showinfo('Ok',"Ce Candidat a été modifier avec success!")
						r=askyesno("Tp","voulez vous modifier encore les information d'un autre Candidat ?")
						print(r)
						if(r==True):
							modifier()
						else:
							menu()


				#--------------------fin sauvegarde----------------------------------------
				Button(tk,text="Retour Au Menu",command=main,font=('arial',20,'bold'),fg='white',bg="blue",activebackground='blue',activeforeground='white').place(x=80,y=740)
				Button(tk,text="Enregistrer",command=save1,font=('arial',20,'bold'),fg='white',bg="green",activebackground='green',activeforeground='white').place(x=907,y=740)

				#---------------------------end of choice--------------------------------------------------


				#_____________end of displaying---------------------------------
				
			else:
				showerror('ERREUR',"Ce NCIN N'exist Pas!")
				NcIn.delete(0,END)
				NcIn.focus()
	B=Button(frame2,text='Recherche',font=('arial',12,'bold'),state='active',bg='green',bd=0,fg='white',activeforeground='white',activebackground='green',command=search);B.place(x=660,y=63)
	B.bind("<Return>",search)
	Button(tk,text="Retour Au Menu",command=main,font=('arial',20,'bold'),fg='white',bg="blue",activebackground='blue',activeforeground='white').place(x=80,y=740)

#-----------------fonction qui test si un fichier est vide	-----------------------------

def is_empty(file):
	size=os.path.getsize(file)
	if(size==0):
		return True
	else:
		False

#------------------fonction qui supprime un canidat--------------------------------

def supprimer():
	clr()
	NCIN=StringVar()
	def clean_here():
		for i in frame2.winfo_children():
			i.destroy()
	def clear0(e):
		if NcIn.get()=='Entre le NCIN du Candidat a Supprimer':
			NcIn.delete(0,END)
			NcIn.config(fg='black')
			NcIn.config(font=('arial',15,'normal'))

	
	frame1=Frame(tk,height=700,width=1000,bg='sky blue')
	frame1.place(x=80,y=40)
	frame2=Frame(tk,height=600,width=900,bg='light grey')
	frame2.place(x=130,y=90)
	Label(frame2,text='Supprimer Candidat',bg='light grey',fg='green',font=('arial',20,'bold')).place(x=270,y=20)
	NcIn=Entry(frame2,textvariable=NCIN,font=('consolas',15),bd=0,bg='white',width=40)
	NCIN.set('Entre le NCIN du Candidat a Supprimer')
	NcIn.config(font=("consolas",15,'italic'))
	NcIn.config(fg='grey')
	Label(frame2,text='NCIN : ',font=('arial',20,'bold'),fg='black',bg='light grey').place(x=70,y=60)
	NcIn.place(x=190,y=66)
	NcIn.bind("<Return>",clear0)
	NcIn.focus()
	
	def search():
		global NCIN
		if NcIn.get()=='' or  NcIn.get()=='Entre le NCIN du Candidat a Supprimer':
			showerror('Alert','Veuillez entre le NCIN')
			NcIn.delete(0,END)
			NcIn.config(fg='black')
			NcIn.config(font=('arial',15,'normal'))
			NcIn.focus()
		else:
			if does_this_NCIN_exist(NcIn.get())==True:
				
				Candidat=[]
				Bacc=[]
				Choix=[]
				pos=0
				nom=[]
				ncin=[]
				prenom=[]
				age=[]
				moy1=[]
				serie1=[]
				notephy1=[]
				notemath1=[]
				choix21=[]
				choix31=[]
				j=0
				ctr=0
				NCIN=NcIn.get()

				#--------------------recuperation dans est stock dans les tableau 
				n=recuperer_candidat(Candidat)
				n1=recuperer_bacc(Bacc)
				n2=recuperer_choix(Choix)

				#------------------fin de recuperation -----------------------------

				#-----------------nettoyage de frame 2
				clean_here()
				#----------------fin de nettoyage-------------------------

				for i in Candidat:
					ncin.append(i.split(';')[0])
					nom.append(i.split(';')[1])
					prenom.append(i.split(';')[2])
					age.append(int(i.split(';')[3]))
				for i in range(len(ncin)):
					print(ncin[i],nom[i],prenom[i],age[i])
				
				pos=position(NCIN)

				for i in Bacc:
					 moy1.append(float(i.split(';')[1]))
					 serie1.append(i.split(';')[2])
					 notemath1.append(float(i.split(';')[3]))
					 notephy1.append(float(i.split(';')[4]))

				for i in Choix:
					choix21.append(i.split(';')[1])
					choix31.append(i.split(';')[2])

				#---------displaying the candidate------------------------------

				


				total=Label(frame2,text='Supprimer  Candidat '+str(pos+1)+'/1000',fg='green',bg='light grey',font=('consolas',20,'bold'))
				total.place(x=150,y=20)
				
				#-------------------------this part concerns the candidate

				Label(frame2,text='NCIN :',font=('consolas',20,'bold'),fg='black',bg='light grey').place(x=70,y=60)
				
				n=Label(frame2,text=ncin[pos],font=('arial',15),bg='light grey',fg='black',bd=0,justify=LEFT)
				n.place(x=165,y=70)
				
				Label(frame2,text='NOM :',font=('consolas',20,'bold'),bg='light grey',fg='black').place(x=70,y=115-5)
				nm=Label(frame2,text=nom[pos],font=("arial",15),bg='light grey',fg='black',bd=0)
				nm.place(x=149,y=125-5)
				
				
				Label(frame2,text="PRENOM : ",font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=170-5)
				pr=Label(frame2,text=prenom[pos],font=("arial",15),bg='light grey',fg='black',bd=0)
				pr.place(x=190,y=180-5)
				
				Label(frame2,text='AGE :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=225-5)
				ag=Label(frame2,text=age[pos],font=('arial',15),bg='light grey',fg='black')
				ag.place(x=149,y=235-5)

				#-------------------end of candidate--------------------------------------------------

				#-----------------------this part concerns the information on his examination certificate

				Label(frame2,text='MOYENNE :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=280-5)
				moy=Label(frame2,text=str(moy1[pos]),font=("arial",15),bg='light grey',fg='black',bd=0)
				moy.place(x=210,y=290-5)

				Label(frame2,text='SERIE BACC :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=335-5)
				list_serie=Label(frame2,text=serie1[pos],font=('arial',15),bg='light grey',fg='black')
				list_serie.place(x=250,y=341-5)

				Label(frame2,text='NOTE DE MATHEMATIQUE :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=390-5)
				notm=Label(frame2,text=str(notemath1[pos]),font=("arial",15),bg='light grey',fg='black',bd=0)
				notm.place(x=445,y=396-5)

				Label(frame2,text='NOTE DE PHYSIQUE :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=390-5+55)
				notp=Label(frame2,text=str(notephy1[pos]),font=("arial",15),bg='light grey',fg='black',bd=0)
				notp.place(x=445,y=396-5+55)

				#-------------------------end of examination --------------------------------------------

				#------------------------this part concerns the choice of the candidate-------------------
				Label(frame2,text='DEUXIEUME CHOIX :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=390-5+55+55)
				list_choix2=Label(frame2,text=choix21[pos],font=("arial",15),bg='light grey',fg='black',bd=0)
				list_choix2.place(x=445,y=396-5+55+55)

				Label(frame2,text='TROISIEME CHOIX :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=390-5+55+55+55)
				list_choix2=Label(frame2,text=choix31[pos],font=("arial",15),bg='light grey',fg='black',bd=0)
				list_choix2.place(x=445,y=396-5+55+55+55)

				#----------------------savegarde -------------------------------------------
				def del1():
					p=askyesno('Tp','voulez vous Supprimer Ce Candidat ?')

					if p:
						
						#-------------here since we are modifiying the content of the file we are 
						#-------------going to open it in writing mode w
						with open(FICCAN,'w') as f:
							for i in range(len(nom)):
								if i!=pos:
									f.write('{};{};{};{}\n'.format(ncin[i],nom[i],prenom[i],age[i]))
						with open(FICBACC,'w') as f1:
							for i in range(len(ncin)):
								if i!=pos:
									f1.write('{};{};{};{};{}\n'.format(ncin[i],moy1[i],serie1[i],notemath1[i],notephy1[i]))
						with open(FICCHOIX,'w') as f:
							for i in range(len(ncin)):
								if i!=pos:
									f.write('{};{};{}\n'.format(ncin[i],choix21[i],choix31[i]))

						showinfo('Ok',"Ce Candidat a été Supprimer avec success!")
						r=askyesno("Tp","voulez vous Supprimer encore les information d'un autre Candidat ?")
						print(r)
						if(r==True):
							supprimer()
						else:
							main()
					else:
						main()


				#--------------------fin sauvegarde----------------------------------------
				Button(tk,text="Retour Au Menu",command=main,font=('arial',20,'bold'),fg='white',bg="blue",activebackground='blue',activeforeground='white').place(x=80,y=740)
				Button(tk,text="Supprimer",command=del1,font=('arial',20,'bold'),fg='white',bg="red",activebackground='red',activeforeground='white').place(x=907,y=740)

				#---------------------------end of choice--------------------------------------------------


				#_____________end of displaying---------------------------------
				
			else:
				showerror('ERREUR',"Ce NCIN N'exist Pas!")
				NcIn.delete(0,END)
				NcIn.focus()
	B=Button(frame2,text='Recherche',font=('arial',12,'bold'),state='active',bg='green',bd=0,fg='white',activeforeground='white',activebackground='green',command=search);B.place(x=660,y=63)
	Button(tk,text="Retour Au Menu",command=main,font=('arial',20,'bold'),fg='white',bg="blue",activebackground='blue',activeforeground='white').place(x=80,y=740)

#---------------------fonction du resulat qui decide de la decision d'un candidat


def resultat():
	Candidat=[]
	Bacc=[]
	Choix=[]
	ncin=[]
	nom=[]
	prenom=[]
	age=[]
	moyenne=[]
	serie=[]
	notemath=[]
	notephy=[]
	choix2=[]
	choix3=[]
	decision=[]
	clr()
	"""frame1=Frame(tk,height=700,width=1000,bg='sky blue')
	frame1.place(x=80,y=40)
	frame2=Frame(tk,height=600,width=900,bg='light grey')
	frame2.place(x=130,y=90)"""
	n=recuperer_candidat(Candidat)
	n1=recuperer_bacc(Bacc)
	n2=recuperer_choix(Choix)
	tk.config(bg='white')
	for i in Candidat:
		ncin.append(i.split(';')[0])
		nom.append(i.split(';')[1])
		prenom.append(i.split(';')[2])
		age.append(int(i.split(';')[3]))
	
	#convertison les nom et prenom en majuscul
	NoM=[i.upper() for i in nom]
	PrEnOm=[i.upper() for i in prenom]
	nom=NoM
	prenom=PrEnOm
	for i in Bacc:
	    moyenne.append(float(i.split(';')[1]));serie.append(i.split(';')[2]);notemath.append(float(i.split(';')[3]));notephy.append(float(i.split(';')[4]))
	for i in Choix:
		choix2.append(combine_name(i.split(';')[1]))
		choix3.append(combine_name(i.split(';')[2]))
	#---------------------debut de la decision-------------------------

	for i in range(n):
		if 	moyenne[i]>S1 or (moyenne[i]>=S2 and moyenne[i]<=S1 and notemath[i]>S3 and notephy[i]>S3):
			decision.append("Informatique")
		else:
			decision.append(choix2[i])
	#sort_information(ncin,nom,prenom,age,moyenne,notemath,notephy,decision)

	#----------------------debut de tri
	ncin1=ncin
	nom1=nom
	prenom1=prenom
	age1=age
	moyenne1=moyenne
	notemath1=notemath
	notephy1=notephy
	dec=decision
	for i in range(0,n):

		for j in range(0,n-1-i):

			if(nom1[j]>nom1[j+1]):

				ncin1[j+1],ncin1[j]=ncin1[j],ncin1[j+1]
				nom1[j+1],nom1[j]=nom1[j],nom1[j+1]
				prenom1[j+1],prenom1[j]=prenom1[j],prenom1[j+1]
				age1[j+1],age1[j]=age1[j],age1[j+1]
				moyenne1[j+1],moyenne1[j]=moyenne1[j],moyenne1[j+1]
				notemath1[j+1],notemath1[j]=notemath1[j],notemath1[j+1]
				notephy1[j+1],notephy1[j]=notephy1[j],notephy1[j+1]
				dec[j+1],dec[j]=dec[j],dec[j+1]
	ncin=ncin1
	nom=nom1
	prenom=prenom
	age=age1
	moyenne=moyenne1
	notemath=notemath1
	notephy=notephy1
	decision=dec

	for i in range(n):
		print(ncin1[i],nom1[i],prenom1[i],age1[i],dec[i])

	#fin de tri

	with open(FICRESU,'w') as f:

		for i in range(n):

			f.write('{};{};{};{};{};{};{};{}\n'.format(ncin[i],nom[i],prenom[i],age[i],moyenne[i],notemath[i],notephy[i],decision[i]))
	"""
	Label(frame1,text='Resultat Des Selection',font=('arial',20,'bold'),bg='sky blue',fg='green').place(x=300,y=10)
	op=['NCIN','NOM','PRENOM','AGE','DECISION']
	x=0
	for i in range(len(op)):
		Label(frame2,text=op[i],font=('arial',8,'bold'),fg='black',bg='light grey').place(x=x,y=0)
		x+=200
	y=20
	for i in range(n):
		Label(frame2,text=ncin[i],font=('arial',8),bg='light grey',fg='black').place(x=0,y=y)
		Label(frame2,text=nom[i],font=('arial',8),bg='light grey',fg='black').place(x=200,y=y)
		Label(frame2,text=prenom[i],font=('arial',8),bg='light grey',fg='black').place(x=400,y=y)
		Label(frame2,text=age[i],font=('arial',8),bg='light grey',fg='black').place(x=600,y=y)
		Label(frame2,text=decision[i],font=('arial',8),bg='light grey',fg='black').place(x=800,y=y)
		y+=20
	"""

	frame0=LabelFrame(tk,text='Resultat Des Selection Des Candidat',fg='green',font=('arial',30,'bold'))
	frame0.pack(fill='both',expand='yes',padx=20,pady=20)
	"""frame1=LabelFrame(tk,text='voulez vous quitter')
	frame1.pack(fill='both',expand='yes',padx=20,pady=10)"""
	trv=Treeview(frame0,columns=(1,2,3,4,5,6),show='headings',height='30')
	trv.pack(fill='both',expand='yes',padx=10,pady=10)
	trv.heading(1,text='N°')
	trv.heading(2,text='NCIN')
	trv.heading(3,text='NOM')
	trv.heading(4,text='PRENOM')
	trv.heading(5,text='AGE')
	trv.heading(6,text='Decision')
	final=[]
	l=''
	a=0
	for i in Candidat:
		l=str(a+1)+' '+ncin[a]+' '+nom[a]+' '+prenom[a]+' '+str(age[a])+' '+decision[a]
		print(i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]+' '+decision[a])
		final.append(l)
		a+=1
	for j in final:
		trv.insert('','end',values=j)
	Button(tk,text='Aller Au Menu Principal',command=main,bg='green',activebackground='red',bd=1,font=('magneto',20)).pack(side='bottom',expand='yes',padx=10,pady=10,ipadx=10)
	
	#------------------------------------------------------------------

#--------------------------------------------------------------------------------------

#--------------------fonction qui affiche les statistique des selection--------------------

def lecture_dans_fichier(fichier):
	Candidat=[]
	with open(fichier,'r') as f:
		for line in f:
			line=line.strip()
			Candidat.append(line)
	return len(Candidat)


def statistique():
	"""info=lecture_dans_fichier(FICADMIS)
	bios=lecture_dans_fichier(FICBIOS)
	geos=lecture_dans_fichier(FICGEOS)
	math=lecture_dans_fichier(FICMATH)
	ict=lecture_dans_fichier(FICICT)
	phy=lecture_dans_fichier(FICPHY)
	chm=lecture_dans_fichier(FICCHM)"""
	clr()
	Candidat=[]
	info=bios=math=geos=ict=chm=phy=0
	n=recuperer_resultat(Candidat)
	for i in Candidat:
		if i.split(';')[7]=='Informatique':
			info+=1
		if i.split(';')[7]=='Mathematique':
			math+=1
		if i.split(';')[7]=='Physique':
			phy+=1
		if i.split(';')[7]=='Ict':
			ict+=1
		if i.split(';')[7]=='Bio_Science':
			bios+=1
		if i.split(';')[7]=='Geo_Science':
			geos+=1
		if i.split(';')[7]=='Chimie':
			chm+=1
	print(n)
	rem=0
	frame1=LabelFrame(tk,text='Statistique Des Selection',font=('arial',30,'bold'),fg='light blue',bg='cadet blue')
	frame1.pack(fill='both',expand='yes',padx=10,pady=10)
	trv=Treeview(frame1,columns=(1,2,3),show='headings',height='10')
	trv.pack(fill='both',expand='true',padx=10,pady=10)
	trv.heading(1,text='N°')
	trv.heading(2,text='Filiére')
	trv.heading(3,text='Pourcentage %')
	percentage=[]
	print(info+math+phy+chm+bios+geos+ict)
	print(info,math,phy,chm,bios,geos,ict)
	rem=round(info/n*100,2)
	percentage.append('1 Informatique '+str(rem)+'%')
	percentage.append('2 Physique '+str(round(phy/n*100,2))+'%')
	percentage.append('3 Mathématique '+str(round(math/count()*100,2))+'%')
	percentage.append('4 Ict '+str(round(ict/n*100,2)))
	percentage.append('5 Bio-Science '+str(round(bios/n*100,2))+'%')
	percentage.append('6 Geo-Science '+str(round(geos/n*100,2))+'%')
	percentage.append('7 Chimie '+str(round(chm/n*100,2))+'%')
	for i in percentage:
		trv.insert('','end',values=i)

	Button(frame1,text='Retourner Au Menu',font=('consolas',20),fg='green',bg='light grey',bd=1,command=main).pack(pady=10,padx=10)


def recuperer_candidat_dans(fichier,Candidat):
	print(fichier)
	with open(fichier,'r') as f:
		for line in f:
			line=line.strip()
			Candidat.append(line)
	return len(Candidat)

#--------------------fonction qui afficher les statistique des selection ------------------

def Supprimer():
	clr()
	Candidat=[]
	n=recuperer_candidat_dans(FICADMIS,Candidat)
	find=False
	a=0
	for i in Candidat:
		if int(i.split(';')[3])>20:
			a+=1
			find=True
	frame=LabelFrame(tk,text='Les Candidats Admis Ayant Plus De 20 ans ',fg='green',font=('arial',20,'bold'))
	trv=Treeview(frame,columns=(1,2,3,4,5),show='headings',height='30')
	trv.pack(padx=10,pady=10,fill='both',expand='yes')
	trv.heading(1,text='N°')
	trv.heading(2,text='NCIN')
	trv.heading(3,text='NOM')
	trv.heading(4,text='PRENOM')
	trv.heading(5,text='AGE')

	if find==True and a>0:
		frame=LabelFrame(tk,text='Les Candidats Admis Ayant Plus De 20 ans ',fg='green',font=('arial',20,'bold'))
		frame.pack(fill='both',expand='yes',padx=10,pady=10)
		trv=Treeview(frame,columns=(1,2,3,4,5),show='headings',height='30')
		trv.pack(padx=10,pady=10,fill='both',expand='yes')
		
		h=''
		r=''
		a=1
		j=1
		older=[]
		younger=[]
		for i in Candidat:
			if int(i.split(';')[3])>20:
				h=str(a)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
				older.append(h)
				a+=1
			else:
				r=str(j)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
				younger.append(r)
				j+=1
		for i in older:
			trv.insert('','end',values=i)
		def fini():
			trv.delete(*trv.get_children())
			frame.config(text='Resultat Definitive Des Admis En Informatique')
			with open(FICADMIS,'w') as f:
				for i in Candidat:
					if int(i.split(';')[3])<=20:
						f.write('{};{};{};{}\n'.format(i.split(';')[0],i.split(';')[1],i.split(';')[2],i.split(';')[3]))
			for i in younger:
				trv.insert('','end',values=i)
			btnd.forget()
		btnd=Button(frame,text='Affichier La Liste Definitive',fg='white',bg='red',activebackground='red',activeforeground='white',relief=RAISED,command=fini,font=('arial',20,'bold'))
		btnd.pack(side=RIGHT,pady=5,expand='yes',padx=10)
		btn=Button(frame,text='Retour Au Menu',font=('consolas',20,'bold'),fg='white',bg='green',command=main,activeforeground='white',activebackground='green')
		btn.pack(expand='yes',padx=10,side=LEFT,pady=5)
	else:
		frame=LabelFrame(tk,text='Les Candidats Admis Ayant Plus De 20 ans ',fg='green',font=('arial',20,'bold'))
		frame.config(text='Resultat Definitive Des Admis En Informatique')
		frame.pack(fill='both',expand='yes',padx=10,pady=10)
		trv=Treeview(frame,columns=(1,2,3,4,5),show='headings',height='30')
		trv.pack(padx=10,pady=10,fill='both',expand='yes')
		trv.heading(1,text='N°')
		trv.heading(2,text='NCIN')
		trv.heading(3,text='NOM')
		trv.heading(4,text='PRENOM')
		trv.heading(5,text='AGE')
		a=1
		h=''
		younger=[]
		for i in Candidat:
			if int(i.split(';')[3])<=20:
				h=str(a)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
				younger.append(h)
				a+=1
		for i in younger:
			trv.insert('','end',values=i)

		btn=Button(frame,text='Retour Au Menu',font=('consolas',20,'bold'),fg='white',bg='green',command=main,activeforeground='white',activebackground='green')
		btn.pack(expand='yes',padx=10,side=LEFT,pady=5)

#--------------------fonction qui cree les ficier pour chaqune des fillier--------------------------

#---------------------fonction qui permet de lire dans un fichier grace a un paramertre---------------- 

def recuperer_resultat(Resultat):
	with open(FICRESU,"r") as f:
		for line in f:
			line=line.strip()
			#print(line.split())
			Resultat.append(line)
	return len(Resultat)



def selection():
	resultat=ncin=nom=prenom=age=Resultat=[]
	n=recuperer_resultat(Resultat)
	f=open(FICMATH,'w')
	f1=open(FICPHY,'w')
	f2=open(FICCHM,'w')
	f3=open(FICICT,'w')
	f4=open(FICGEOS,'w')
	f5=open(FICBIOS,'w')
	for i in Resultat:
		if i.split(';')[7]=='Mathematique':
			print('mathematic')
			f.write('{};{};{};{}\n'.format(i.split(';')[0],i.split(';')[1],i.split(';')[2],i.split(';')[3]))
		if i.split(';')[7]=='Physique':
			print('physique')
			f1.write('{};{};{};{}\n'.format(i.split(';')[0],i.split(';')[1],i.split(';')[2],i.split(';')[3]))
		if i.split(';')[7]=='Chimie':
			print('chiemie')
			f2.write('{};{};{};{}\n'.format(i.split(';')[0],i.split(';')[1],i.split(';')[2],i.split(';')[3]))
		if i.split(';')[7]=='Ict':
			print('ict')
			f3.write('{};{};{};{}\n'.format(i.split(';')[0],i.split(';')[1],i.split(';')[2],i.split(';')[3]))
		if i.split(';')[7]=='Geo_Science':
			print('geos')
			f4.write('{};{};{};{}\n'.format(i.split(';')[0],i.split(';')[1],i.split(';')[2],i.split(';')[3]))
		if i.split(';')[7]=='Bio_Science':
			f5.write('{};{};{};{}\n'.format(i.split(';')[0],i.split(';')[1],i.split(';')[2],i.split(';')[3]))
	f.close()
	f1.close()
	f2.close()
	f3.close()
	f4.close()
	f5.close()

#-----------------------fonction qui affiche les candidat par filliere-------------------


def affichier_fillier():
	selection()
	Math=[]
	Bios=[]
	Chim=[]
	Phy=[]
	Geos=[]
	Ict=[]
	n=recuperer_candidat_dans(FICMATH,Math)
	n1=recuperer_candidat_dans(FICBIOS,Bios)
	n2=recuperer_candidat_dans(FICCHM,Chim)
	n3=recuperer_candidat_dans(FICPHY,Phy)
	n4=recuperer_candidat_dans(FICGEOS,Geos)
	n5=recuperer_candidat_dans(FICICT,Ict)
	print(n,n3)
	clr()
	pos=1
	
	def forward(n):
		global b
		global f
		sleep(0.5)
		clr()
		#liste=['','Filiére Mathématique','Filiére Physique','Filiére Ict','Filiére Chimie','Filiére Bio Science','Filiére Geo Science']
		frame0=LabelFrame(tk,bg='white',fg='green',font=('Sergio Ui',20))
		frame0.pack(fill='both',expand='yes',padx=10,pady=10)
		trv=Treeview(frame0,columns=(1,2,3,4,5),show='headings',height='30')
		trv.pack(fill='both',expand='yes',padx=10,pady=10)
		trv.heading(1,text='N°')
		trv.heading(2,text='NCIN')
		trv.heading(3,text='NOM')
		trv.heading(4,text='PRENOM')
		trv.heading(5,text='AGE')
		g=n-1
		frame0.config(text=liste[n]+' '+str(n)+'/6')
		f=Button(frame0,text='>>',command=lambda:forward(n+1),font=('consolas',20,'bold'),fg='black',bg='powder blue',bd=1)
		b=Button(frame0,text='<<',command=lambda:backward(n-1),font=('consolas',20,'bold'),fg='black',bg='powder blue',bd=1)
		if n==6:
			f=Button(frame0,text='>>',state=DISABLED,font=('consolas',20,'bold'),fg='black',bg='powder blue',bd=1)
		if n==2:
			#par_filier(Phy)
			a=1
			h=''
			salot=[]
			#trv.delete(*trv.get_children())
			for i in Phy:
				h=str(a)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
				salot.append(h)
				a+=1
			for i in salot:
				trv.insert('','end',values=i)
		if n==3:
			a=1
			h=''
			salot=[]
			#trv.delete(*trv.get_children())
			for i in Ict:
				h=str(a)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
				salot.append(h)
				a+=1
			for i in salot:
				trv.insert('','end',values=i)
		if n==4:
			a=1
			h=''
			salot=[]
			#trv.delete(*trv.get_children())
			for i in Chim:
				h=str(a)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
				salot.append(h)
				a+=1
			for i in salot:
				trv.insert('','end',values=i)
		if n==5:
			a=1
			h=''
			salot=[]
			#trv.delete(*trv.get_children())
			for i in Bios:
				h=str(a)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
				salot.append(h)
				a+=1
			for i in salot:
				trv.insert('','end',values=i)
		if n==6:
			a=1
			h=''
			salot=[]
			#trv.delete(*trv.get_children())
			for i in Geos:
				h=str(a)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
				salot.append(h)
				a+=1
			for i in salot:
				trv.insert('','end',values=i)
		f.pack(side=RIGHT,expand='yes',anchor='ne')
		b.pack(side=LEFT,expand='yes',anchor='nw')
		Button(frame0,text='Retour Au Menu',command=main,font=('arial',20,'bold'),bg='green',fg='white').pack(side=LEFT,expand='yes',anchor='center',padx=30,ipadx=60)
		
	def backward(n):
		global b
		global f
		clr()
		sleep(0.5)
		#liste=['','Filiére Mathématique','Filiére Physique','Filiére Ict','Filiére Chimie','Filiére Bio Science','Filiére Geo Science']
		frame0=LabelFrame(tk,bg='white',fg='green',font=('Sergio Ui',20))
		frame0.pack(fill='both',expand='yes',padx=10,pady=10)
		trv=Treeview(frame0,columns=(1,2,3,4,5),show='headings',height='30')
		trv.pack(fill='both',expand='yes',padx=10,pady=10)
		trv.heading(1,text='N°')
		trv.heading(2,text='NCIN')
		trv.heading(3,text='NOM')
		trv.heading(4,text='PRENOM')
		trv.heading(5,text='AGE')
		g=n
		frame0.config(text=liste[n]+' '+str(g)+'/6')
		f=Button(frame0,text='>>',command=lambda:forward(n+1),font=('consolas',20,'bold'),fg='black',bg='powder blue',bd=1)
		
		b=Button(frame0,text='<<',command=lambda:backward(n-1),font=('consolas',20,'bold'),fg='black',bg='powder blue',bd=1)
		if n==1:
			b=Button(frame0,text='<<',state=DISABLED,font=('consolas',20,'bold'),fg='black',bg='powder blue',bd=1)
			a=1
			h=''
			salot=[]
			#trv.delete(*trv.get_children())
			for i in Math:
				h=str(a)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
				salot.append(h)
				a+=1
			for i in salot:
				trv.insert('','end',values=i)
		if n==2:
			a=1
			h=''
			salot=[]
			#trv.delete(*trv.get_children())
			for i in Phy:
				h=str(a)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
				salot.append(h)
				a+=1
			for i in salot:
				trv.insert('','end',values=i)
		if n==3:
			a=1
			h=''
			salot=[]
			#trv.delete(*trv.get_children())
			for i in Ict:
				h=str(a)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
				salot.append(h)
				a+=1
			for i in salot:
				trv.insert('','end',values=i)
		if n==4:
			a=1
			h=''
			salot=[]
			#trv.delete(*trv.get_children())
			for i in Chim:
				h=str(a)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
				salot.append(h)
				a+=1
			for i in salot:
				trv.insert('','end',values=i)
		if n==5:
			a=1
			h=''
			salot=[]
			#trv.delete(*trv.get_children())
			for i in Bios:
				h=str(a)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
				salot.append(h)
				a+=1
			for i in salot:
				trv.insert('','end',values=i)
		f.pack(side=RIGHT,expand='yes',anchor='ne')
		b.pack(side=LEFT,expand='yes',anchor='nw')
		Button(frame0,text='Retour Au Menu',command=main,font=('arial',20,'bold'),bg='green',fg='white').pack(side=LEFT,expand='yes',anchor='center',padx=30,ipadx=60)



	liste=['','Filiére Mathématique','Filiére Physique','Filiére Ict','Filiére Chimie','Filiére Bio Science','Filiére Geo Science']
	frame0=LabelFrame(tk,text=liste[pos]+' '+str(pos)+'/6',bg='white',fg='green',font=('Sergio Ui',20))
	frame0.pack(fill='both',expand='yes',padx=10,pady=10)
	trv=Treeview(frame0,columns=(1,2,3,4,5),show='headings',height='30')
	trv.pack(fill='both',expand='yes',padx=10,pady=10)
	trv.heading(1,text='N°')
	trv.heading(2,text='NCIN')
	trv.heading(3,text='NOM')
	trv.heading(4,text='PRENOM')
	trv.heading(5,text='AGE')
	if pos==1:
		a=1
		h=''
		salot=[]
		#trv.delete(*trv.get_children())
		for i in Math:
			h=str(a)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
			salot.append(h)
			a+=1
		for i in salot:
			trv.insert('','end',values=i)
	f=Button(frame0,text='>>',command=lambda:forward(pos+1),font=('consolas',20,'bold'),fg='black',bg='powder blue',bd=1)
	f.pack(side=RIGHT,expand='yes',anchor='ne')
	b=Button(frame0,text='<<',state=DISABLED,font=('consolas',20,'bold'),fg='black',bg='powder blue',bd=1)
	b.pack(side=LEFT,expand='yes',anchor='nw')
	Button(frame0,text='Retour Au Menu',command=main,font=('arial',20,'bold'),bg='green',fg='white').pack(side=LEFT,expand='yes',anchor='center',padx=30,ipadx=60)
	
	

#----------------------fonction qui permet d'enregistre les candidat------------------------------
def ajouter():
	pass

#------------------fonction qui affiche les candidat enregstre--------------------------------
def display():
	Candidat=[]
	Bacc=[]
	Choix=[]
	a=1
	clr()
	frame=LabelFrame(tk,text='Candidat Deja Enregistrer ',font=('BaltimoreTypewriterBold',22,'bold'),fg='green',bg='sky blue')
	frame.pack(fill='both',expand='yes',padx=10,pady=10)
	trv=Treeview(frame,columns=(1,2,3,4,5,6,7,8,9,10,11),show='headings',height='30')
	trv.pack(expand='yes',fill='both',padx=10,pady=10)
	trv.heading(1,text='N°')
	trv.heading(2,text='NCIN')
	trv.heading(3,text='NOM')
	trv.heading(4,text='PRENOM')
	trv.heading(5,text='AGE')
	trv.heading(6,text='MOYENNE')
	trv.heading(7,text='SERIE')
	trv.heading(8,text='NOTEMATH')
	trv.heading(9,text='NOTEPHY')
	trv.heading(10,text='CHOIX2')
	trv.heading(11,text='CHOIX3')
	n=recuperer_candidat(Candidat)
	n1=recuperer_bacc(Bacc)
	n2=recuperer_choix(Choix)
	h=''
	ncin=[]
	nom=[]
	prenom=[]
	age=[]
	moy=[]
	serie=[]
	notemath=[]
	notephy=[]
	choix2=[]
	choix3=[]
	Total=[]
	for i in Candidat:
		ncin.append(i.split(';')[0])
		nom.append(i.split(';')[1])
		prenom.append(i.split(';')[2])
		age.append(i.split(';')[3])
	for i in Bacc:
		moy.append(i.split(';')[1])
		serie.append(i.split(';')[2])
		notemath.append(i.split(';')[3])
		notephy.append(i.split(';')[4])

	for i in Choix:
		c=i.split(';')[1]
		c=combine_name(c)
		choix2.append(c)
		v=i.split(';')[2]
		v=combine_name(v)
		choix3.append(v)


	for i in range(0,n):

		for j in range(0,n-1-i):

			if(nom[j]>nom[j+1]):

				ncin[j+1],ncin[j]=ncin[j],ncin[j+1]
				nom[j+1],nom[j]=nom[j],nom[j+1]
				prenom[j+1],prenom[j]=prenom[j],prenom[j+1]
				age[j+1],age[j]=age[j],age[j+1]
				moyenne[j+1],moyenne[j]=moyenne[j],moyenne[j+1]
				notemath[j+1],notemath[j]=notemath[j],notemath[j+1]
				notephy1[j+1],notephy1[j]=notephy1[j],notephy1[j+1]
				dec[j+1],dec[j]=dec[j],dec[j+1]

	for i in range(n):
		h=str(a)+' '+ncin[i]+' '+nom[i]+' '+prenom[i]+' '+age[i]+' '+moy[i]+' '+serie[i]+' '+notemath[i]+' '+notephy[i]+' '+choix2[i]+' '+choix3[i]
		Total.append(h)
		a+=1
	for i in Total:
		trv.insert('','end',values=i)
	Button(frame,text='Retour Au Menu',font=('BaltimoreTypewriterBold',20,'bold'),fg='white',bg='green',command=main,relief=RAISED).pack(padx=10,pady=5,expand='yes')




#--------------fonction qui permet d'afficher les admis en info

def admis():
	Candidat=[]
	ADMIS=[]
	h=''
	pos=1
	frame2=''
	clr()
	n=recuperer_resultat(Candidat)
	with open(FICADMIS,'w') as f:
		for i in Candidat:
			if i.split(';')[7]=='Informatique':
				h=str(pos)+' '+i.split(';')[0]+' '+i.split(';')[1]+' '+i.split(';')[2]+' '+i.split(';')[3]
				ADMIS.append(h)
				f.write('{};{};{};{}\n'.format(i.split(';')[0],i.split(';')[1],i.split(';')[2],i.split(';')[3]))
				pos+=1
	frame1=LabelFrame(tk,text='Candidat Admis En Filiére Informatique',font=('BaltimoreTypewriterBold Beveled',20),fg='green')
	frame1.pack(fill='both',expand='yes',padx=10,pady=10)
	trv=Treeview(frame1,columns=(1,2,3,4,5),show='headings',height='30')
	trv.pack(fill='both',expand='yes',padx=10,pady=10)
	trv.heading(1,text='N°')
	trv.heading(2,text='NCIN')
	trv.heading(3,text='NOM')
	trv.heading(4,text='PRENOM')
	trv.heading(5,text='AGE')
	for i in ADMIS:
		trv.insert('','end',values=i)
	Button(tk,text='Retourner au menu ',font=('FrankRuehl',20),fg='white',bd=2,command=main,bg='green',activebackground='green',).pack(padx=10,pady=10)




#fonction qui cree les fichier candidat,bacc et choix
def creat_primary_files():
	try:
		open('candidat.txt','r')
	except :
		open('candidat.txt','w')
	try:
		open('bacc.txt','r')
	except :
		open('bacc.txt','w')
	try:
		open('choix.txt','r')
	except :
		open('choix.txt','w')
		
frame1=None
frame2=None

# -------------------voici mon menu-------------------------------------
def main():
	global frame1,frame2
	clr()
	bg=PhotoImage(file='tp2.png')
	#------------------------------------

	#-----------------------label------------------
	Label(tk,image=bg,width=1200,height=800).place(x=0,y=0)

	frame1=Frame(tk,height=700,width=1000,bg='sky blue')
	frame1.place(x=80,y=40)
	#frame1.pack(fill='both',expand='yes',padx=80,pady=40)
	Label(tk,text='TP 1031 2020/2021',font=('sergio ui',30,'bold'),bg='sky blue',fg='green').place(x=355,y=50)
	frame2=Frame(tk,height=600,width=900,bg='light grey')
	frame2.place(x=130,y=90)
	Label(tk,text='System Intelligent Des Selection En Informatique ',font=('arial',20,'bold'),bg='light grey',fg='blue').place(x=270,y=90)
	Label(tk,text='1',font=('arial',25,'bold'),fg='blue',bg='light grey').place(x=180,y=133)
	Button(tk,text='Enregistrer Un Candidat ',font=('arial',20,'bold'),bg='light grey',fg='black',activebackground='light grey',activeforeground='red',bd=0,command=ajouter).place(x=210,y=130)
	Label(tk,text='2',font=('arial',25,'bold'),fg='blue',bg='light grey').place(x=180,y=173)
	Button(tk,text='Modifier Un Candidat Enregistrer ',font=('arial',20,'bold'),bg='light grey',fg='black',activebackground='light grey',activeforeground='red',bd=0,command=modifier).place(x=210,y=170)
	Label(tk,text='3',font=('arial',25,'bold'),fg='blue',bg='light grey').place(x=180,y=213)
	Button(tk,text='Supprimer Un Candidat Enregistrer',font=('arial',20,'bold'),bg='light grey',fg='black',activebackground='light grey',activeforeground='red',bd=0,command=supprimer).place(x=210,y=210)
	Label(tk,text='4',font=('arial',25,'bold'),fg='blue',bg='light grey').place(x=180,y=253)
	Button(tk,text='Affichier Les Resultat Des Candidat ',font=('arial',20,'bold'),bg='light grey',fg='black',activebackground='light grey',activeforeground='red',bd=0,command=resultat).place(x=210,y=250)
	Label(tk,text='5',font=('arial',25,'bold'),fg='blue',bg='light grey').place(x=180,y=293)
	Button(tk,text='Affichier Les Candidat Admis En Informatique',command=admis,font=('arial',20,'bold'),bg='light grey',fg='black',activebackground='light grey',activeforeground='red',bd=0).place(x=210,y=290)
	Label(tk,text='6',font=('arial',25,'bold'),fg='blue',bg='light grey').place(x=180,y=333)
	Button(tk,text='Affichier Les Statistique Des Selection ',font=('arial',20,'bold'),bg='light grey',fg='black',activebackground='light grey',activeforeground='red',bd=0,command=statistique).place(x=210,y=330)
	Label(tk,text='7',font=('arial',25,'bold'),fg='blue',bg='light grey').place(x=180,y=373)
	Button(tk,text='Supprimer Les Plus Ågée Des Admis ',command=Supprimer,font=('arial',20,'bold'),bg='light grey',fg='black',activebackground='light grey',activeforeground='red',bd=0).place(x=210,y=370)
	Label(tk,text='8',font=('arial',25,'bold'),fg='blue',bg='light grey').place(x=180,y=413)
	Button(tk,text='Affichier Les Candidats Par Filiere ',command=affichier_fillier,font=('arial',20,'bold'),bg='light grey',fg='black',activebackground='light grey',activeforeground='red',bd=0).place(x=210,y=410)
	Label(tk,text='9',font=('arial',25,'bold'),fg='blue',bg='light grey').place(x=180,y=453)
	Button(tk,text='Affichier Les Candidats Enregistrer ',command=display,font=('arial',20,'bold'),bg='light grey',fg='black',activebackground='light grey',activeforeground='red',bd=0).place(x=210,y=450)
	Label(tk,text='10',font=('arial',25,'bold'),fg='blue',bg='light grey').place(x=170,y=493)
	Button(tk,text='Renitialiser Les Fichier ',font=('arial',20,'bold'),command=renitializer,bg='light grey',fg='black',activebackground='light grey',activeforeground='red',bd=0).place(x=210,y=490)
	Label(tk,text='11',font=('arial',25,'bold'),fg='blue',bg='light grey').place(x=170,y=533)
	Button(tk,text='A Propos de Tp 1031',font=('arial',20,'bold'),command=about,bg='light grey',fg='black',activebackground='light grey',activeforeground='red',bd=0).place(x=210,y=530)
	Label(tk,text='Copyright (c) 2021 Navi Coperation',font=('arial',20,'italic'),bg='light grey',fg='green').place(x=550,y=650)

total1=count()

def ajouter():
	global total1,frame1,frame2
	#clr()
	tk.config(bg='grey')
	frame1=Frame(tk,height=700,width=1000,bg='sky blue')
	frame1.place(x=80,y=40)
	frame2=Frame(tk,height=600,width=900,bg='light grey')
	frame2.place(x=130,y=90)
	ncin=StringVar()
	nom=StringVar()
	prenom=StringVar()
	age=StringVar()
	serie=StringVar()
	moyenne=StringVar()
	notemath=StringVar()
	notephy=StringVar()
	choix2=StringVar()
	choix3=StringVar()
	#-----------clearing the display message -------------------------
	def clear(e):
		if n.get()=='Enter the NCIN':
			n.delete(0,END)
			n.config(font=("sergio ui",15,'normal'))
			n.config(fg='black')
	def clear1(e):
		if nm.get()=='Enter the name':
			nm.delete(0,END)
			nm.config(font=("sergio ui",15,'normal'))
			nm.config(fg='black')
	def clear2(e):
		if pr.get()=='Enter the surname':
			pr.delete(0,END)
			pr.config(font=("sergio ui",15,'normal'))
			pr.config(fg='black')
	def clear3(e):
		if ag.get()=='age':
			ag.delete(0,END)
			ag.config(font=('arial',15,'normal'))
			ag.config(fg='black')
	def clear4(e):
		if moy.get()=='Average':
			moy.delete(0,END)
			moy.config(font=('arial',15,'normal'))
			moy.config(fg='black')
	def clear5(e):
		if notm.get()=='NOTEMATH':
			notm.delete(0,END)
			notm.config(font=('arial',15,'normal'))
			notm.config(fg='black')
	def clear6(e):
		if notp.get()=='NOTEPHY':
			notp.delete(0,END)
			notp.config(font=('arial',15,'normal'))
			notp.config(fg='black')		

    #-----------end of clearing ------------------------------------------
  
	list_2=["Mathematique","Physique","Chimie","Bio Science","Geo Science","Ict"]
	list_1=["C","D","Ti","F3","GCE"]

	tk.config(bg='white')
	total=Label(frame2,text='Entrez les Informatique Du Candidat '+str(total1+1)+'/1000',fg='green',bg='light grey',font=('consolas',20,'bold'))
	total.place(x=150,y=20)
	
	#-------------------------this part concerns the candidate

	Label(frame2,text='NCIN :',font=('consolas',20,'bold'),fg='black',bg='light grey').place(x=70,y=60)
	
	n=Entry(frame2,textvariable=ncin,width=20,font=('arial',15),bg='white',fg='light grey',bd=0)
	n.insert(0,"Enter the NCIN")
	n.place(x=149,y=70)
	
	Label(frame2,text='NOM :',font=('consolas',20,'bold'),bg='light grey',fg='black').place(x=70,y=115-5)
	nm=Entry(frame2,textvariable=nom,width=30,font=("arial",15),bg='white',fg='light gray',bd=0)
	nm.insert(0,"Enter the name")
	nm.place(x=149,y=125-5)
	
	
	Label(frame2,text="PRENOM : ",font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=170-5)
	pr=Entry(frame2,textvariable=prenom,font=("arial",15),bg='white',fg='light grey',width=30,bd=0)
	pr.insert(0,"Enter the surname")
	n.config(font=("Sergio ui",15,'italic'))
	nm.config(font=("sergio ui",15,'italic'))
	pr.config(font=("sergio ui",15,'italic'))
	pr.place(x=190,y=180-5)
	
	"""nm.focus()
	n.focus()
	pr.focus()"""
	Label(frame2,text='AGE :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=225-5)
	ag=Entry(frame2,textvariabl=age,font=('arial',15),bg='white',fg='light gray',width=5)
	ag.insert(0,'age')
	ag.config(font=('arial',15,'italic'))
	ag.place(x=149,y=235-5)

	#-------------------end of candidate

	#-----------------------this part concerns the information on his examination certificate

	Label(frame2,text='MOYENNE :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=280-5)
	moy=Entry(frame2,textvariable=moyenne,width=8,font=("arial",15),bg='white',fg='light grey',bd=0)
	moy.insert(0,'Average')
	moy.place(x=210,y=290-5)

	Label(frame2,text='SERIE BACC :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=335-5)
	list_serie=OptionMenu(frame2,serie,*list_1)
	list_serie.config(width=6)
	serie.set('serie')
	list_serie.place(x=250,y=341-5)

	Label(frame2,text='NOTE DE MATHEMATIQUE :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=390-5)
	notm=Entry(frame2,textvariable=notemath,width=10,font=("arial",15),bg='white',fg='light grey',bd=0)
	notm.insert(0,'NOTEMATH')
	notm.place(x=445,y=396-5)

	Label(frame2,text='NOTE DE PHYSIQUE :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=390-5+55)
	notp=Entry(frame2,textvariable=notephy,width=10,font=("arial",15),bg='white',fg='light grey',bd=0)
	notp.insert(0,'NOTEPHY')
	notp.place(x=445,y=396-5+55)

	#-------------------------end of examination --------------------------------------------

	#------------------------this part concerns the choice of the candidate-------------------
	Label(frame2,text='DEUXIEUME CHOIX :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=390-5+55+55)
	list_choix2=OptionMenu(frame2,choix2,*list_2)
	list_choix2.config(width=12)
	choix2.set('CHOIX2')
	list_choix2.place(x=445,y=396-5+55+55)

	Label(frame2,text='TROISIEME CHOIX :',font=("consolas",20,'bold'),bg='light grey',fg='black').place(x=70,y=390-5+55+55+55)
	list_choix2=OptionMenu(frame2,choix3,*list_2)
	list_choix2.config(width=12)
	choix3.set('CHOIX3')
	list_choix2.place(x=445,y=396-5+55+55+55)

	#---------------------------end of choice--------------------------------------------------

	#------------binding attributing the mouse to the entry--------------

	n.bind("<Button-1>",clear)
	nm.bind("<Button-1>",clear1)
	pr.bind("<Button-1>",clear2)
	ag.bind("<Button-1>",clear3)
	moy.bind("<Button-1>",clear4)
	notm.bind("<Button-1>",clear5)
	notp.bind("<Button-1>",clear6)

	#-----------end of binding--------------------------------------


	#----------clear values---------------------------------------

	def clr_vals():
		ncin.set('')
		nom.set('')
		prenom.set('')
		age.set('')
		moyenne.set('')
		serie.set('serie')
		notemath.set('')
		notephy.set('')
		choix2.set('CHOIX2')
		choix3.set('CHOIX3')
		n.focus()


	#----------end-------------------------------------------------


	#---------------------BUTTON to go the main menu and saved------------------------------

	def save():
		global total1
		h1=h2=h3=h4=h5=h6=h7=h8=h9=h10=False
		if n.get()=='Enter the NCIN' or n.get()=='':
			showerror('Primary KEY','Veillier Entrez Le NCIN Du Candidat!')
			n.focus()
			ncin.set('')
			n.config(fg='black')
			n.config(font=('arial',15,'normal'))
		else:
			h1=True

		if nm.get()=='Enter the name' or nm.get()=='':
			showerror("ERREUR ","Veillier Entrez Le Nom Du Candidat!")
			nm.focus()
			nom.set('')
			nm.config(fg='black')
			nm.config(font=('arial',15,'normal'))
		else:
			NAME=upr(NAME)
			NAME=combine_name(nm.get())
			
			h2=True

		if prenom=='Enter the surname' or pr.get()=='':
			showerror('ERREUR ','Veillier Entrez Le Prenom du Candidat!')
			pr.focus()
			prenom.set('')
			pr.config(fg='black')
			pr.config(font=('arial',15,'normal'))
		else:
			SURNAME=upr(SURNAME)
			SURNAME=combine_name(pr.get())
			
			print(upr(SURNAME))
			h3=True

		try:
			Age=int(ag.get())
			if Age>=14 and Age<=100:
				h4=True
			else:
				showerror("AGE INVALID","Veillier Rentrez L'age,entre 14 et 100")
				age.set('')
				ag.focus()
				ag.config(fg='black')
				ag.config(font=('arial',15,'normal'))
		except:
			showerror("INCOMPATIBLE TYPE","Veillier Rentrez L'age,l'age doit etre un entier")
			age.set('')
			ag.focus()
			ag.config(fg='black')
			ag.config(font=('arial',15,'normal'))

		try:
			Moy=float(moy.get())
			if Moy>=10 and Moy<=20:
				h5=True
			else:
				showerror("MOYENNE INVALID","Veillier Rentrez une moyenne elle entre 0 et 20")
				moyenne.set('')
				moy.focus()
				moy.config(fg='black')
				moy.config(font=('arial',15,'normal'))
		except:
			showerror("INCOMPATIBLE TYPE","Veillier Rentrez la moyenne elle doit étre un nombre decimal")
			moyenne.set('')
			moy.focus()
			notp.config(fg='black')
			notp.config(font=('arial',15,'normal'))

		try:
			NM=float(notm.get())
			if NM>0 and NM<=20:
				h6=True
			else:
				showerror("NOTEMATH INVALID!","Veillier Rentrez la NOTEMATH elle doit étre entre 0 et 20")
				notemath.set('')
				notm.focus()
				notm.config(fg='black')
				notm.config(font=('arial',15,'normal'))
		except:
			showerror("INCOMPATIBLE TYPE","Veillier Rentrez la NOTEMATH elle doit étre un nombre decimal")
			notemath.set('')
			notm.focus()
			notm.config(fg='black')
			notm.config(font=('arial',15,'normal'))

		try:
			NP=float(notp.get())
			if NP>0 and NP<=20:
				h7=True
			else:
				showerror("MOYENNE INVALID","Veillier Rentrez la NOTEPHY elle doit étre entre 0 et 20")
				notephy.set('')
				notp.focus()
				notp.config(fg='black')
				notp.config(font=('arial',15,'normal'))
		except:
			showerror("INCOMPATIBLE TYPE","Veillier Rentrez la NOTEPHY elle doit étre un nombre decimal")
			notephy.set('')
			notp.focus()
			notp.config(fg='black')
			notp.config(font=('arial',15,'normal'))

		if serie.get()=='serie':
			showerror('ERREUR',"Veillier Selectionioner La serie du candidat!")
		else:
			h8=True

		if choix2.get()=='CHOIX2':
			showerror('ERREUR',"Veillier Selectionioner Le Deuxiemme choix du candidat!")
		else:
			if choix2.get()==choix3.get():
				showerror('ERREUR',"Veillier Selectionioner Un autre choix du candidat!")
			h9=True

		if choix3.get()=='CHOIX3':
			showerror('ERREUR',"Veillier Selectionioner Le Troisieme choix du candidat!")
		else:
			if choix3.get()==choix2.get():
				showerror('ERREUR',"Veillier Selectionioner Un autre choix du candidat!")
				choix3.set('CHOIX3')
			else:
				h10=True
		if (h1==h2==h3==h4==h5==h6==h7==h8==h9==h10)==True:
			print('ok')
			k=serie.get()
			print(k)
			if(does_this_NCIN_exist(n.get())==False):
				Can=CANDIAT(n.get(),NAME,SURNAME,Age)
				print(Can.add())
				Bac=BACC(n.get(),Moy,k,NM,NP)
				print(Bac.add())
				Bac.add()
				Cho=CHOIX(n.get(),choix2.get(),choix3.get())
				print(Cho.add())
				q=askyesno('TP','voulez vous ajouter encore un Candidat ?')
				if q==True:
					total1=int(total1)
					total1=total1+1
					total.config(text='Entrez les Informatique Du Candidat '+str(total1+1)+'/1000')
					clr_vals()
				else:
					main()
			else:
				showerror("Alert","Ce NCIN Appartient A Un Autre Candidat")
				n.focus()
				ncin.set('')

	Button(tk,text="Retour Au Menu",command=main,font=('arial',20,'bold'),fg='white',bg="blue",activebackground='blue',activeforeground='white').place(x=80,y=740)
	Button(tk,text="Enregistrer",command=save,font=('arial',20,'bold'),fg='white',bg="green",activebackground='green',activeforeground='white').place(x=907,y=740)

	#---------------------------------------------------------------------------------------

def renitializer():
	clr()
	def clean(file):
		message='Voulez Vous Renitialiser Le Fichier '+file
		r=askyesno('Tp',message)
		if r==True:
			f=open(file,'w')
			f.close()
			message='Le Fichier '+file+' A été Renitialiser avec Success'
			sleep(1)
			showinfo('Tp',message)
		else:
			pass
	frame=LabelFrame(tk,text='Renitialiser Les Fichier',font=('elephant',25),fg='blue',bg='white')
	frame.pack(fill='both',expand='yes',padx=10,pady=10)
	fr1=LabelFrame(frame,text='Fichier Primaire',font=('arial',15,'bold'),fg='black',bg='white')
	fr1.pack(fill='both',expand='yes',padx=50,pady=5)
	fr2=LabelFrame(frame,text='Fichier Secondaire',font=('arial',15,'bold'),fg='brown',bg='white')
	fr2.pack(fill='both',expand='yes',padx=50,pady=5)
	Button(fr1,text='Fichier Candidat',font=('arial',15),fg='green',bg='white',command=lambda:clean(FICCAN)).pack(expand='yes',padx=10,pady=1)
	Button(fr1,text='Fichier Bacc',font=('arial',15),fg='green',bg='white',command=lambda:clean(FICBACC)).pack(expand='yes',padx=10,pady=1)
	Button(fr1,text='Fichier Choix',font=('arial',15),fg='green',bg='white',command=lambda:clean(FICCHOIX)).pack(expand='yes',padx=10,pady=1)
	

	Button(fr2,text='Fichier Resultat',font=('arial',15),fg='green',bg='white',command=lambda:clean(FICRESU)).pack(expand='yes',padx=10,pady=1)
	Button(fr2,text='Fichier Admis',font=('arial',15),fg='green',bg='white',command=lambda:clean(FICADMIS)).pack(expand='yes',padx=10,pady=1)
	Button(fr2,text='Fichier Mathématique',font=('arial',15),fg='green',bg='white',command=lambda:clean(FICMATH)).pack(expand='yes',padx=10,pady=1)
	Button(fr2,text='Fichier Physique',font=('arial',15),fg='green',bg='white',command=lambda:clean(FICPHY)).pack(expand='yes',padx=10,pady=1)
	Button(fr2,text='Fichier Chimie',font=('arial',15),fg='green',bg='white',command=lambda:clean(FICCHM)).pack(expand='yes',padx=10,pady=1)
	Button(fr2,text='Fichier Ict',font=('arial',15),fg='green',bg='white',command=lambda:clean(FICICT)).pack(expand='yes',padx=10,pady=1)
	Button(fr2,text='Fichier Bio Science',font=('arial',15),fg='green',bg='white',command=lambda:clean(FICBIOS)).pack(expand='yes',padx=10,pady=1)
	Button(fr2,text='Fichier Geo Science',font=('arial',15),fg='green',bg='white',command=lambda:clean(FICGEOS)).pack(expand='yes',padx=10,pady=1)

	Button(frame,text='Retour Au Menu',font=('arial',20),fg='white',bg='green',command=main).pack(padx=10,pady=0,expand='yes')



SHOW=False
HIDE=True

def pwd():
	clr()
	frame=LabelFrame(tk,text='Tp',font=('BaltimoreTypewriterBold',30,),fg='black',bg='powder blue',relief='ridge',bd=10)
	frame.pack(fill='both',expand='yes',padx=10,pady=10)
	im=PhotoImage(file='tp1.png')
	eye=False
	im=im.subsample(2,2)
	
	ps=StringVar()
	name=StringVar()
	ps=StringVar()
	def show_psw():
		P.config(show='')
	def hide_psw():
		P.config(show='*')
	def sho_hid():
		global SHOW,HIDE
		if SHOW==False and HIDE==True:
			show_psw()
			HIDE=False
			SHOW=True
		elif SHOW==True and HIDE==False:
			hide_psw()
			SHOW=False
			HIDE=True
	def validate():
		if ps.get()=='tp 1031' or ps.get()=='TP 1031':
			sleep(1)
			main()
		else:
			showwarning('TP','Mot de Pass Incorrect Veuillez Ressayer')
			ps.set('')
			P.focus()
	def reset():
		ps.set('')
		name.set('')
		N.focus_set()
	
	"""Label(frame,text='Mot De Pass ',font=('arial',20),fg='black',bg='white',padx=1).pack(expand='yes',anchor='ne')
	psw=Entry(frame,font=('consolas',30),show='*',justify=CENTER,textvariable=ps)
	psw.pack(expand='yes',padx=1,anchor='n',side='left')
	psw.focus()
	Label(frame,image=im).pack(padx=10,pady=10,expand='yes')
	Button(frame,text='(0)',font=('arial',15,'bold'),command=sho_hid,padx=0).pack(padx=1,expand='yes',)	
	Button(frame,text='OK',font=('arial',20,'bold'),pady=10,fg='white',bg='green',command=validate).pack(side='bottom')"""
	frame1=Frame(frame,height=500,width=700,bg='sky blue',bd=20,relief='ridge')
	frame1.grid(row=1,column=0,pady=20,padx=200)

	frame2=Frame(frame,height=500,width=700,bg='sky blue',bd=20,relief='ridge')
	frame2.grid(row=2,column=0,pady=20,padx=200)

	Label(frame,text='System De Securité',font=('arial',30,'bold'),fg='cadet blue',bg='powder blue').grid(row=0,column=0,columnspan=3)
	Label(frame1,text="Nom d'utilisateur ",font=('arial',30,'bold'),fg='white',bg='sky blue').grid(row=1,column=0,padx=10)
	N=Entry(frame1,textvariable=name,width=25,font=('consolas',19),bg='light grey')
	N.grid(row=1,column=1,padx=10,pady=5)
	N.insert(0,'USER')
	Label(frame1,text='Mot de pass',font=('arial',30,'bold'),fg='white',bg='sky blue',pady=20,width=17).grid(row=2,column=0,padx=5)
	P=Entry(frame1,textvariable=ps,width=23,font=('arial',20,'bold'),fg='white',bg='cadet blue',show='*')
	P.grid(row=2,column=1,padx=10)
	Button(frame1,text='(0)',font=('arial',13,'bold'),relief='raised',fg='black',bg='cadet blue',command=sho_hid).grid(row=2,column=2)
	N.focus_set()
	P.focus_set()
	Button(frame2,text='Connectez-Vous',font=('consolas',20,'bold'),command=validate,fg='black',padx=5,bg='green',activebackground='green').grid(row=0,column=0,pady=15,padx=19)
	Button(frame2,text='Actualiser',font=('consolas',20,'bold'),command=reset,fg='black',bg='white',padx=5).grid(row=0,column=1,pady=15,padx=21)
	Button(frame2,text='Fermer La Fenetre',command=lambda:tk.destroy(),font=('consolas',20,'bold'),fg='black',bg='red',padx=5,activebackground='red').grid(row=0,column=2,pady=15,padx=20)



def about():
	showinfo('TP 1031','TP 1031 a été Concu pour Facilité la tache de la Console')


def load():
	clr()
	f=LabelFrame(tk,text='Tp',font=('arial',25,'bold'),fg='blue',bg='white')
	f.pack(fill='both',expand='yes',padx=30,pady=30)
	im=PhotoImage(file='tp2.png')
	im=im.subsample(2,2)
	Label(f,image=im).pack(expand='yes',padx=10)
	Label(f,text='LOADING',font=('consolas',30),fg='black',bg='white').pack(expand='yes',padx=10,pady=10,fill='both')
	progress=Progressbar(f,orient=HORIZONTAL,mode='determinate')
	progress.pack(expand='yes',padx=10,pady=10,anchor='center')
	progress['value']=20
	tk.update_idletasks()
	sleep(1)
	progress['value']=40
	tk.update_idletasks()
	sleep(1)
	progress['value']=60
	tk.update_idletasks()
	sleep(1)
	progress['value']=80
	tk.update_idletasks()
	sleep(1)
	progress['value']=100
	tk.update_idletasks()
	sleep(1)
	"""progress['value']=80
				tk.update_idletasks()
				sleep(1)
				progress['value']=60
				tk.update_idletasks()
				sleep(1)
				progress['value']=40
				tk.update_idletasks()
				sleep(1)
				progress['value']=20
				tk.update_idletasks()
				sleep(1)
				progress['value']=0
				tk.update_idletasks()
				sleep(1)
			"""


tk=Tk()
tk.title("Projet 1031")
tk.geometry("1200x800+0+0")
im=PhotoImage(file='logo.png')
tk.iconphoto(False,im)
#--------adding an image-------------
bg=PhotoImage(file='tp2.png')
#------------------------------------
#load()
#-----------------------label------------------
Label(tk,image=bg,width=1200,height=800).place(x=0,y=0)

#----------menu-------------------
menu=Menu(tk)
menu.config(bg='grey')
tk.config(menu=menu)
File=Menu(tk,tearoff=0)
Help=Menu(tk,tearoff=0)
About=Menu(tk,tearoff=0)
menu.add_cascade(label='File',menu=File)
menu.add_cascade(label='About',menu=About)
menu.add_cascade(label='Help',menu=Help)
#------------------------------------

creat_primary_files()
pwd()

#main()
tk.mainloop()
