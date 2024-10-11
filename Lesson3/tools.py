#Tools.py為內建module

#定義常數
MON = 1
TUE = 2
WED = 3
THU = 4
FRI = 5
SAT = 6
SUN = 7

#建立class
class Eagle(object):
    #自訂inatial
    def __init__(self,name:str,age:int):
        self.__name=name #__name，__代表private。attribute值需要透過setter，符合條件才可設定此attribute值
        self.__age=age #private attribute。若public attribute代表object可以直接修改attribute。
        pass
    #自訂實體被print時的輸出
    def __repr__(self)->str:
        return f"學名:{self.name}\n年紀:{self.age}"
    @property #註冊property，取得attribute的值=getter
    def name(self)->str:#property，read only
        return self.__name #存取att__name輸出
    @name.setter #可接收property的name可接收property的name
    def name(self, n):#n為name傳進為nameproperty傳進來的值由n接收
        print(f"不不可以改名為{n}")
    @property
    def age(self)->int:#property getter
        return self.__age
    @age.setter #property setter。若private attribute，符合setter設定條件時，可以修改attribute的值。
    def age(self,value):
        if value >100 or value<0: #
            print("Invalid value")
        else:
            self.__age=value #object set value符合setter設定條件時，可以修改attribute的值

#子類別
#繼承是為了擴充父類別功能
class JUEagle(Eagle):#繼承自Eagle
    @classmethod#不需要實體，只需要class就可執行
    def echo(cls):
        print("I'm JUEagle")
    #初始化建立實體
    def __init__(self, name, age, height:int=0, weight:int=0, wingspan:int=0):
        #除了父類別的name,age參數，多其他引數。有預設值的話寫在最後面
        super().__init__(name=name, age=age)#super()代表執行父類別的初始化。引數=父類別的參數，
        self.height=height
        self.weight=weight
        self.wingspan=wingspan
        #繼承後，再設定其他attribute
    @property
    def BMI (self)->float:
        return self.weight/((self.height/100)**2)
    
    #實體方法instance method
    def w_ratio (self)->float:#每公分翅膀乘載多少體重(?)
        return round(self.weight/self.wingspan,ndigits=2)
    
def get_eagle(name:str,age:int)->Eagle:#建立get eagle function ，屬於eagle類別
    return Eagle(name=name,age=age)#使用Eagle初始化。建立實體，引數名稱等於參數值。傳出實體。

def get_JUeagle(name:str,age:int,height:int,weight:int,wingspan:int)->JUEagle:#建立get eagle function ，屬於eagle類別
    return JUEagle(name=name,age=age,height=height,weight=weight,wingspan=wingspan)#使用Eagle初始化。建立實體，引數名稱等於參數值。傳出實體。