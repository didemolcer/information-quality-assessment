library(glmnet)
library(e1071)
library(caret)
library(ModelMetrics)
library(openxlsx)

path <- "c:/...."
setwd(path)


tablename="content vectorization"

alpha=0.5
weird=70

afile=paste("loocv elastic ",tablename,".xlsx",sep='')
ModelOutput<-data.frame()

str=paste("loocv elastic ",tablename,".txt",sep='')

sink(str)

while(weird <640)
{
  datasett <- read.csv(file="textual features.csv", header=TRUE, sep=",")
  
  ###matrix
  # name=paste(tablename,weird,sep=' ')
  # str=paste("loocv elastic   ",tablename,weird,".txt",sep='')
  #################
  

  ###############################
  # FOR HYBRID 
  
  # alldata <- read.csv(paste(name,".csv",sep=""),header=TRUE, sep=",")
   
  # dataset <- datasett[,1:length(datasett)-1]
  # alldata <- cbind(dataset,alldata)
  
  # alldata$Discern <- datasett$Discern
  # datasett <- alldata
  
  ###############################
  
  dataset <- datasett[,1:length(datasett)-1]
  alldata <- dataset
  
  classes <- as.matrix(datasett$Discern) #datasett$Cov.Cor
  
  #################### 
  # Model Fit
  
  fold<-1:60
  
  acc.all<-vector()
  mcc.all<-vector()
  mse.all<-vector()
  pred_alldata<-vector()
  mse_train<-vector()
  
  for (foldnum in 1:60)
  {
    classes_train1 <- classes[-which( fold == foldnum),]
    alldata_train1 <- alldata[-which(fold == foldnum),]
    
    alldata_test1 <- alldata[which(fold == foldnum),]
    class_test1<-datasett[which(fold == foldnum),]
    
    fit<-cv.glmnet(as.matrix(alldata_train1), as.matrix(classes_train1), alpha=alpha,nfold=59,family="binomial", type.measure = "class", grouped=FALSE)
    cvfit_lambda_min_avg = fit$lambda.1se
    
    #prediction train error
    pred_train = predict(fit,as.matrix(alldata_train1), cvfit_lambda_min_avg, type = "class")
    
    act<-classes_train1
    actual<-as.numeric(as.factor(act))
    
    pred_train<-as.numeric(as.factor(pred_train))
    mse_train[which(fold == foldnum)]<-mse(actual,pred_train)
    
    #predict test data
    pred_alldata[which(fold == foldnum)] = predict(fit,as.matrix(alldata_test1), cvfit_lambda_min_avg, type = "class")
    
    p= as.factor(predict(fit,as.matrix(alldata_test1), cvfit_lambda_min_avg, type = "class"))
    a= as.factor(class_test1$Discern)
    
    if(p==a){
      accuracy=1
      MCC=1
    }else{
      accuracy=0
      MCC=-1
    }
    
    mse.all[which(fold == foldnum)] <- mse(a,p)
    acc.all[which(fold == foldnum)] <- accuracy
    mcc.all[which(fold == foldnum)] <- MCC
    
    coefMatrix_fold <- as.matrix(coef(fit))
    
    orderedIndices <- order(-abs(coefMatrix_fold))
    orderedcoef_fold <- coefMatrix_fold[orderedIndices]
    
    c<-rownames(coefMatrix_fold)
    c<-c[orderedIndices]
    orderedcoef_fold<-data.frame(cbind(c,orderedcoef_fold))
    
    
    orderedcoef_fold<-orderedcoef_fold[which(orderedcoef_fold$orderedcoef_fold!=0),]
    removeintercept<-which(orderedcoef_fold$c=="(Intercept)")
    orderedcoef_fold<-orderedcoef_fold[-removeintercept,]
    len<-length(orderedcoef_fold$c)
    rankf<-1:len;   if(len>0)
      orderedcoef_fold<-cbind(orderedcoef_fold,rankf)
  }
  
  
  actual<-as.numeric(as.factor(classes))
  pred_alldata<-as.numeric(as.factor(pred_alldata))
  
  cm <- unclass(table(pred_alldata, actual))
  
  result<-c(mean(mse_train),mse(actual,pred_alldata),mean(acc.all),sd(acc.all),mean(mcc.all),sd(mcc.all))
  print(result)
  print(cm)
  print(acc.all)
  write.xlsx(ModelOutput,file=afile,append=FALSE,sheet = sheetname)
  
  weird=weird+70 
  
}
sink()
