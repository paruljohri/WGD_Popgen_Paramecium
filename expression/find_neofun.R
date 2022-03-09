#To get outliers or putative cnadidates of neofunctionalization
t <- read.table("autogamy_tpm_paralogs.txt",h=T)


#To get neofunctionalization:
#get averages:
t$avg_log_V1 <- (log(t$VK1_para1+1.1) + log(t$V1.2_para1+1.1))/2
t$avg_log_V2 <- (log(t$VK1_para2+1.1) + log(t$V1.2_para2+1.1))/2
t$avg_log_S1 <- (log(t$S1.1_para1+1.1) + log(t$S1.2_para1+1.1))/2
t$avg_log_S2 <- (log(t$S1.1_para2+1.1) + log(t$S1.2_para2+1.1))/2
t$avg_log_T01 <- (log(t$T0.1_para1+1.1) + log(t$T0.2_para1+1.1))/2
t$avg_log_T02 <- (log(t$T0.1_para2+1.1) + log(t$T0.2_para2+1.1))/2
t$avg_log_T5_1 <- (log(t$T5.1_para1+1.1) + log(t$T5.2_para1+1.1))/2
t$avg_log_T5_2 <- (log(t$T5.1_para2+1.1) + log(t$T5.2_para2+1.1))/2
t$avg_log_T11_1 <- (log(t$T11.1_para1+1.1)+log(t$T11.2_para1+1.1))/2
t$avg_log_T11_2 <- (log(t$T11.1_para2+1.1)+log(t$T11.2_para2+1.1))/2
t$avg_log_T20_1 <- (log(t$T20.1_para1+1.1) + log(t$T20.2_para1+1.1) + log(t$T20.3_para1+1.1))/3
t$avg_log_T20_2 <- (log(t$T20.1_para2+1.1) + log(t$T20.2_para2+1.1) + log(t$T20.3_para2+1.1))/3

#get delta:
t_delta_V <- (t$avg_log_V1-t$avg_log_V2)/(t$avg_log_V1+t$avg_log_V2)
t_delta_S <- (t$avg_log_S1-t$avg_log_S2)/(t$avg_log_S1+t$avg_log_S2)
t_delta_T0 <- (t$avg_log_T01-t$avg_log_T02)/(t$avg_log_T01+t$avg_log_T02)
t_delta_T5 <- (t$avg_log_T5_1-t$avg_log_T5_2)/(t$avg_log_T5_1+t$avg_log_T5_2)
t_delta_T11 <- (t$avg_log_T11_1-t$avg_log_T11_2)/(t$avg_log_T11_1+t$avg_log_T11_2)
t_delta_T20 <- (t$avg_log_T20_1-t$avg_log_T20_2)/(t$avg_log_T20_1+t$avg_log_T20_2)


#get delta delta:
t_delta_delta_S <- t_delta_V - t_delta_S
t_delta_delta_T0 <- t_delta_V - t_delta_T0
t_delta_delta_T5 <- t_delta_V - t_delta_T5
t_delta_delta_T11 <- t_delta_V - t_delta_T11
t_delta_delta_T20 <- t_delta_V - t_delta_T20

#Plot to check distributions:
par(mfrow=c(3,2))
plot(t_delta_V, t_delta_S, main="Starvation", xlab="relative para1-para2 (vegetative)", ylab="relative para1-para2", cex.axis=1.2, cex.lab=1.5)
plot(t_delta_V, t_delta_T0, main="Autogamy (T0)", xlab="relative para1-para2 (vegetative)", ylab="relative para1-para2", cex.axis=1.2, cex.lab=1.5)
plot(t_delta_V, t_delta_T5, main="Autogamy (T5)", xlab="relative para1-para2 (vegetative)", ylab="relative para1-para2", cex.axis=1.2, cex.lab=1.5)
plot(t_delta_V, t_delta_T11, main="Autogamy (T11)", xlab="relative para1-para2 (vegetative)", ylab="relative para1-para2", cex.axis=1.2, cex.lab=1.5)
plot(t_delta_V, t_delta_T20, main="Autogamy (T20)", xlab="relative para1-para2 (vegetative)", ylab="relative para1-para2", cex.axis=1.2, cex.lab=1.5)

par(mfrow=c(3,2))
plot(density(t_delta_delta_S), main="Starvation", xlab="delta veg - delta autogamy")
plot(density(t_delta_delta_T0), main="T0", xlab="delta veg - delta autogamy")
plot(density(t_delta_delta_T5), main="T5", xlab="delta veg - delta autogamy")
plot(density(t_delta_delta_T11), main="T11", xlab="delta veg - delta autogamy")
plot(density(t_delta_delta_T20), main="T20", xlab="delta veg - delta autogamy")

#Find genes that have differential expression at the vegetative state and for each individual condition:
#t_S_2sd <- t[which(abs(t_delta_V)>2.0*sd(t_delta_V) & abs(t_delta_delta_S)>2.0*sd(t_delta_delta_S)), ]
#t_T0_2sd <- t[which(abs(t_delta_V)>2.0*sd(t_delta_V) & abs(t_delta_delta_T0)>2.0*sd(t_delta_delta_T0)), ]
#t_T5_2sd <- t[which(abs(t_delta_V)>2.0*sd(t_delta_V) & abs(t_delta_delta_T5)>2.0*sd(t_delta_delta_T5)), ]
#t_T11_2sd <- t[which(abs(t_delta_V)>2.0*sd(t_delta_V) & abs(t_delta_delta_T11)>2.0*sd(t_delta_delta_T11)), ]
#t_T20_2sd <- t[which(abs(t_delta_V)>2.0*sd(t_delta_V) & abs(t_delta_delta_T20)>2.0*sd(t_delta_delta_T20)), ]

#Find genes that have differential expression from the vegetative state and for each individual condition:
t_S_2sd <- t[which(abs(t_delta_delta_S)>2.0*sd(t_delta_delta_S)), ]
t_T0_2sd <- t[which(abs(t_delta_delta_T0)>2.0*sd(t_delta_delta_T0)), ]
t_T5_2sd <- t[which(abs(t_delta_delta_T5)>2.0*sd(t_delta_delta_T5)), ]
t_T11_2sd <- t[which(abs(t_delta_delta_T11)>2.0*sd(t_delta_delta_T11)), ]
t_T20_2sd <- t[which(abs(t_delta_delta_T20)>2.0*sd(t_delta_delta_T20)), ]

#write them in files:
write.table(t_S_2sd[,c(1,2,29,30, 31, 32)], file="neofunc_S_2SD.txt", append=F, sep='\t', row.names=F, col.names=T, quote=F)
write.table(t_S_2sd[,c(1,2,29,30, 33, 34)], file="neofunc_T0_2SD.txt", append=F, sep='\t', row.names=F, col.names=T, quote=F)
write.table(t_S_2sd[,c(1,2,29,30, 35, 36)], file="neofunc_T5_2SD.txt", append=F, sep='\t', row.names=F, col.names=T, quote=F)
write.table(t_S_2sd[,c(1,2,29,30, 37, 38)], file="neofunc_T11_2SD.txt", append=F, sep='\t', row.names=F, col.names=T, quote=F)
write.table(t_S_2sd[,c(1,2,29,30, 39, 40)], file="neofunc_T20_2SD.txt", append=F, sep='\t', row.names=F, col.names=T, quote=F)

