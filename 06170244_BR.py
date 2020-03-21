#!/usr/bin/env python
# coding: utf-8

# In[1]:


postings = {'stan':[2, 4, 5, 6, 99, 101],
                 'brutus':[1, 2, 4, 11, 31, 45, 173, 174],
                 'calpurnia':[2,31,54,101],
                 'caesar':[5,31]}


# In[2]:


#sorted(postings.items(),key=lambda items:(items[0],items[1]),reverse = False) 


# In[3]:


#import operator
#terms = sorted(postings.items(),key=operator.itemgetter(1))
#terms


# In[4]:


def rest(terms):
    del terms[0]
    return terms

def INTERSECT(term_1, term_2):
    
    answer = []
    i = 0
    while i < len(term_1):
        if term_1[i] in term_2:
            answer.append(term_1[i])
        i+=1    
    return answer

def SORTBYINCREASINGFREQUENCY(terms):
    terms.sort()
    return terms

def boolean_retrieval(terms):
    terms = SORTBYINCREASINGFREQUENCY([postings[t] for t in query if t in postings])
    if len(terms) == None: return []
    result = terms[0]
    terms = rest(terms)
    
    while terms and result:
        result = INTERSECT(result,terms[0])
        terms = rest(terms)
    return result

if __name__ == '__main__':
    query = ['brutus', 'calpurnia', 'stan']
    answer = boolean_retrieval(query)
    print('The query {:} are appeared in document ID: {:}'.format(query,answer))


# In[5]:


#query = ['brutus', 'calpurnia', 'stan']
#a =[postings[t] for t in query if t in postings]
#a


# In[6]:


#a[0]


# In[7]:


#a.sort()
#a

