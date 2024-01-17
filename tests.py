from Swagger.swaggerapi import BotList, BotDetails, Register, Login

BotL = BotList()
BotL.send(uri='/bots/')

BotDetail = BotDetails()
BotDetail.send(uri='/bots/2/')

Log = Login()
Log.send(uri='/users/login/')

Reg = Register()
Reg.send(uri='/users/')
