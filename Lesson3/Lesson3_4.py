import widget
from widget import get_eagle, get_JUeagle
#widget為package
#widget功能寫在__init__.py中

print(widget.SAT)

eagle6=get_eagle(name="Max ju",age=44)
print(eagle6)

eagle7=get_JUeagle(name="Guava",age=22,height=180,weight=77,wingspan=180)#不可以把PROPERTY放引數這裡
print(eagle7)
print(eagle7.BMI)
print(eagle7.w_ratio())