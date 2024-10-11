
import tools

print(tools.SUN)
#module要先存檔喔
eagle1=tools.Eagle(name="Little Black",age="3")
print(eagle1)

eagle2=tools.JUEagle(name="Little White",age="22")
print(eagle2)

eagle3=tools.get_eagle(name="Little flower",age="43")
print(eagle3)

eagle4=tools.get_JUeagle(name="Max Flower",age=120,height=160,weight=66,wingspan=160)
print(eagle4)
print(eagle4.BMI)
print(eagle4.w_ratio())
