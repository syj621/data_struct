a <- 1
a<- as.integer(1)
is.integer(a)
b <-0.1
is.double(b)

c<-'asdasdasda'
is.character(c)
is.numeric(c)
d<-'1231231421'
is.integer(d)
d<-as.integer(d)
is.numeric(d)

e<-paste("hello world",c,sep='.')
e
paste0('qweqweq',' _ ' ,'asdasd','  .  ','1231231')

s1<-substr('hello world',0,3)
s1

al<-TRUE
al
f<-as.logical(1)
f

v<-c(1:3)
v

s1<-1
s2<-2
d<-c(1,2)
d<-c(s1,s2,d)
d
length(d)
d[c(1,3)]
d[c(1,3)]<-c(10,20)
d

matrix1<- matrix(c(1:50),10,5)
l1<-c(1:100)
M1<-matrix(l1,ncol =5)
M1[5,1:4]<-c(10000,9781,123,13)
sum(M1)
apply(M1,2 ,sum)

class<-c(1,2,3)
name<-c('ss','kk','jj')
student<-data.frame(name=name,class=class)
student
rownames(student)<-student[,1]
student[,'name']
student[c('ss','kk'),]
student$name[2]
which(student$class %in% c(3,4,5))