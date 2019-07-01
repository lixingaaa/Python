# 模拟购物车购物过程
# 存放商品列表
list = []
for i in range(5):
    product = input("请输入商品编号和名称进行商品入库, 每次只能输入一件商品: \n")
    list.append(product)

# 输出所有入库商品
for item in list:
    print(item)

# 存放购物车的商品信息
cat = []
buyProduct = ""
print("请输入要购买的商品编号: ")
for item in list:
    productNumber = input("")
    if item.find(productNumber) == 0:
        buyProduct = item
        cat.append(buyProduct)
        print("商品已经添加到购物车, 请继续添加要购买的商品编号: ")
    elif productNumber == "q":
        break;

print("您购物车已买商品为: ")
for m in range(len(cat)):
    print(cat[m])
