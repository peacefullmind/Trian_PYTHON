def curve_pre():
    #闭包的意义在于保存了函数定义时的环境（现场）。若没有闭包的存在，则很容易受外部环境的影响，难以保证函数运行的正确进行。
    a=25

    def curve(x):
        return a*x*x

    return curve

a=10
f=curve_pre() #返回的是个公式，而不是结果
print(type(f))
print(f)

print(f(2))