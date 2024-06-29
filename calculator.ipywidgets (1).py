#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ipywidgets as widgets


# In[6]:


box=widgets.Text(description="enter operation:,padding=4")
output_box=widgets.FloatText(description="output")
b7=widgets.Button(description="7")
b8=widgets.Button(description="8")
b9=widgets.Button(description="9")
b4=widgets.Button(description="4")
b5=widgets.Button(description="5")
b6=widgets.Button(description="6")
b1=widgets.Button(description="1")
b2=widgets.Button(description="2")
b3=widgets.Button(description="3")
bzero=widgets.Button(description="0")
bstar=widgets.Button(description="*")
bdiv=widgets.Button(description="/")
bplus=widgets.Button(description="+")
bmin=widgets.Button(description="-")
bequal=widgets.Button(description="=")
bclear=widgets.Button(description="ac")
bsp=widgets.Button(description="bsp")
H1=widgets.HBox([b7,b8,b9,bclear])
H2=widgets.HBox([b4,b5,b6,bequal])
H3=widgets.HBox([b1,b2,b3,bplus])
H4=widgets.HBox([bstar,bzero,bmin,bdiv])
result=widgets.HBox([box,output_box])
V=widgets.VBox([result,H1,H2,H3,H4,bsp])


# In[7]:


def f7(Self):
    box.value=box.value+"7"
def f8(self):
    box.value=box.value+"8"
def f9(self):
    box.value=box.value+"9"
def f5(self):
    box.value=box.value+"5"
def f4(self):
    box.value=box.value+"4"
def f6(self):
    box.value=box.value+"6"
def f3(self):
    box.value=box.value+"3"
def f2(self):
    box.value=box.value+"2"
def f1(self):
    box.value=box.value+"1"
def fplus(self):
    box.value=box.value+"+"
def fmin(self):
    box.value=box.value+"-"
def fstar(self):
    box.value=box.value+"*"
def fdiv(self):
    box.value=box.value+"/"
def fclear(self):
    box.value=""
def fzero(self):
    box.value=box.value+"0"
def fbsp(self):
    box.value=box.value[0:-1]
    
    


# In[8]:


def fequal(self):
    s=eval("{}".format(box.value))
    output_box.value=s


# In[9]:


try:
    b1.on_click(f1)
    b2.on_click(f2)
    b3.on_click(f3)
    b4.on_click(f4)
    b5.on_click(f5)
    b6.on_click(f6)
    b7.on_click(f7)
    b8.on_click(f8)
    b9.on_click(f9)
    bzero.on_click(fzero)
    bplus.on_click(fplus)
    bmin.on_click(fmin)
    bstar.on_click(fstar)
    bdiv.on_click(fdiv)
    bclear.on_click(fclear)
    bequal.on_click(fequal)
    bsp.on_click(fbsp)
    display(V)
except TypeError as e:
    pass


# In[ ]:





# In[21]:





# In[ ]:




