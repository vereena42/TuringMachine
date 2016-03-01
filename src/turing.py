#!/usr/bin/env python2

# Copyright (c) 2015, Dominika Salawa <vereena42@gmail.com>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
# 
#     * Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#       and/or other materials provided with the distribution.
# 
#     * Neither the name of the <organization> nor the names of its
#       contributors may be used to endorse or promote products derived from this
#       software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import collections

import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('nazwa',type=str)  
	args = parser.parse_args()
	nazwa=args.nazwa
	plik=open(nazwa)
	lines=plik.readlines()
	plik.close()
	table = collections.defaultdict(lambda:0)
	start=lines[0]
	start=start[:len(start)-1]
	end=lines[1]
	end=end[:len(end)-1]
	end=end.split()
	fun=lines[2]
	fun=fun[:len(fun)-1]
	funs=fun.split()
	i=3
	while fun!="":
		if len(funs)!=5:
			print "You need to enter 5 parameters!"
		elif len(funs[1])!=1:
			print "Second parameter must be a character!"
		elif len(funs[3])!=1:
			print "Fourth parameter must be a character!"	
		elif funs[4]!="L" and funs[4]!="R" and funs[4]!="S":
			print "5th parameter must be L R or S"
		else:
			if table[funs[0],funs[1]]!=0:
				print "Turing machine must be deterministic!"
			else:
				table[(funs[0],funs[1])]=(funs[2],funs[3],funs[4])
		fun=lines[i]
		fun=fun[:len(fun)-1]
		i+=1
		funs=fun.split()
	inp=lines[i]
	inp=inp[:len(inp)-1]
	pointer=0
	state=start
	print "State: "+state
	print inp
	poin=""
	for i in range(len(inp)):
		if i==pointer:
			poin+="^"
		poin+=" "
	print poin
	back=[]
	while not state in end:
		y=raw_input("Next step? q - quit, b - back, n - next: ")
		if y=="q":
			print "Machine stopped"
			break
		elif y=='b':
			if len(back)==0:
				print "You can't go back!"
				continue
			how=back[-1]
			back=back[:len(back)-1]
			if how[4]=='R':
				if inp[pointer]=='-' and pointer==len(inp)-1:
					inp=inp[:len(inp)-1]
					pointer-=1
				elif pointer==0:
					inp='-'+inp
				else:
					pointer-=1
			elif how[4]=='L':
				if inp[pointer]=='-' and pointer==0:
					inp=inp[1:]
				elif pointer==len(inp)-1:
					inp=inp+'-'
					pointer+=1
				else:
					pointer+=1
			state=how[0]
			inp=inp[:pointer]+how[1]+inp[pointer+1:]
			print "State: "+state
			print inp
			poin=""
			for i in range(len(inp)):
				if i==pointer:
					poin+="^"
				poin+=" "
			print poin
			continue
		elif y!="n":
			print "q or b or n !"
			continue
		x=table[state,inp[pointer]]
		if x==0:
			print "Machine can't go further!"
		else:
			back.append((state,inp[pointer],x[0],x[1],x[2]))
			state=x[0]
			inp=inp[:pointer]+x[1]+inp[pointer+1:]
			if x[2]=="R":
				if pointer==0 and inp[pointer]=="-":
					inp=inp[1:]
				elif pointer==len(inp)-1:
					pointer+=1
					inp+="-"
				else:
					pointer+=1
			elif x[2]=="L":
				if pointer==len(inp)-1 and inp[pointer]=="-":
					inp=inp[:len(inp)-1]
					pointer-=1
				elif pointer==0:
					inp="-"+inp
				else:
					pointer-=1
		print "State: "+state
		print inp
		poin=""
		for i in range(len(inp)):
			if i==pointer:
				poin+="^"
			poin+=" "
		print poin
	i=0
	while i<len(inp) and inp[i]=='-':
		i+=1
	inp=inp[i:]
	i=len(inp)-1
	while i>=0 and inp[i]=='-':
		i-=1
	inp=inp[:i+1]
	print "Result: "+inp
	print "End!"
			
