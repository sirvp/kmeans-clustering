#PROGRAM TO SORT A DATA SET INTO TWO CLUSTERS USING K-MEANS CLUSTERING ALGORITHM

#        SAMPLE INPUT
#       --------------
#
#Record         A         B
#    1         1.0       2.0
#    2         1.5       2.0
#    3         3.0       4.0
#    4         5.0       7.0
#    5         3.5       5.0
#    6         4.5       5.0
#    7         3.5       4.5

#     Expected Clusters
#----------------------------

#    Cluster1 =  [0,1]
#    Cluster2 =  [2,3,4,5,6]



import math        #To perform sqrt and pow operations


def minimum(n):       #Function to find mimimum value in dataset, so as to assign as mean for Cluster1
    mini=math.sqrt(math.pow(list1[0],2)+math.pow(list2[0],2))
    i=1
    j1=0
    while i<n:
        m=math.sqrt(math.pow(list1[i],2)+math.pow(list2[i],2))
        if(m<mini):
            mini=m
            j1=i
        i+=1
    mean1=mini    #Storing Mean value
    return j1


def maximum(n):        # Function to find maximum value in dataset, so as to assign as mean for Cluster2
    maxi=math.sqrt(math.pow(list1[0],2)+math.pow(list2[0],2))
    i=1
    j2=0
    while i<n:
        m=math.sqrt(math.pow(list1[i],2)+math.pow(list2[i],2))
        if(m>maxi):
            maxi=m
            j2=i
        i+=1
    mean2=maxi     #Storing Mean value
    return j2


list1=[]            #To store values in A
list2=[]            #To store values in B
mean1=0
mean2=0
n=input("Enter the number of records: ")
i=0
j=0

# Entering records
#-------------------

while i<n:
    print "Row ",i+1
    list1.append(input("Enter 1st field: "))
    list2.append(input("Enter 2nd field: "))
    i+=1


clust1=[]          #To store Cluster1
clust2=[]          #To store Cluster2
j1=minimum(n)
j2=maximum(n)
i=0
m=0     #cluster 1 index
n1=0    #cluster 2 index


#   Sorting records into clusters
#--------------------------------------

while i<n:
    k1=math.sqrt(math.pow((list1[i]-list1[j1]),2)+math.pow((list2[i]-list2[j1]),2))
    k2=math.sqrt(math.pow((list1[i]-list1[j2]),2)+math.pow((list2[i]-list2[j2]),2))
    if k1<=k2:
        clust1.append(i)
        m+=1
        j=0     
        q=0
        p=0
        while j<m:
            a=clust1[j]
            p+=list1[a]
            b=clust1[j]
            q+=list2[b]
            j+=1
            
        mean1=math.sqrt(math.pow(p/m,2)+math.pow(q/m,2))    # New Mean

    else:
        clust2.append(i)
        n1+=1
        j=0
        x=0
        y=0
        while j<n1:
            a=clust2[j]
            x+=list1[a]
            b=clust2[j]
            y+=list2[b]
            j+=1
        mean2=math.sqrt(math.pow(x/n1,2)+math.pow(y/n1,2))      # New Mean
    i+=1
# Print Original Cluster records
#---------------------------------

print '\nCluster1=',clust1,'\n'
print 'Cluster2=',clust2

#Rechecking records to see if they are assigned to the right cluster
#by comparing it with new mean value
#---------------------------------------------------------------------

x1=0
while x1<=10:
    i=0
    while i<m:
        a=clust1[i]
        k1=math.sqrt(math.pow(list1[a]-(p/m),2)+math.pow(list2[a]-(q/m),2))
        #a=clust1[i]             
        k2=math.sqrt(math.pow(list1[a]-(x/n1),2)+math.pow(list2[a]-(y/n1),2))
        if k1>k2:
            g=clust1.pop(i)       #removing element from cluster
            m-=1                  #reducing value of cluster1 by 1
            j=0     # Iteration variable
            q=0
            p=0
            while j<m:
                a=clust1[j]
                p+=list1[a]
                b=clust1[j]
                q+=list2[b]
                j+=1
            mean1=math.sqrt(math.pow(p/m,2)+math.pow(q/m,2))    # New Mean
            
            clust2.append(g)    #adding element to the other cluster
            n1+=1
            j=0
            x=0
            y=0
            while j<n1:
                a=clust2[j]
                x+=list1[a]
                b=clust2[j]
                y+=list2[b]
                j+=1
            mean2=math.sqrt(math.pow(x/n1,2)+math.pow(y/n1,2))      # New Mean
        i+=1
    i=0
    while i<n1:
        a=clust2[i]
        k1=math.sqrt(math.pow(list1[a]-(p/m),2)+math.pow(list2[a]-(q/m),2))
        #a=clust2[i]
        k2=math.sqrt(math.pow(list1[a]-(x/n1),2)+math.pow(list2[a]-(y/n1),2))
        if k1<k2:
            h=clust2.pop(i)
            n1-=1
            j=0
            x=0
            y=0
            while j<n1:
                a=clust2[j]
                x+=list1[a]
                b=clust2[j]
                y+=list2[b]
                j+=1
            mean2=math.sqrt(math.pow(x/n1,2)+math.pow(y/n1,2))      # New Mean
            clust1.append(h)
            m+=1
            j=0     # Iteration variable
            q=0
            p=0
            while j<m:
                a=clust1[j]
                p+=list1[a]
                b=clust1[j]
                q+=list2[b]
                j+=1
            mean1=math.sqrt(math.pow(p/m,2)+math.pow(q/m,2))    # New Mean
        i+=1
    x1+=1


#     Display Final Clusters
#----------------------------

print '\nMoidefied Clusters :\n'
print '\nCluster1=',clust1
print '\nCluster2=',clust2

    
            
        
        
                     


        
                                                
