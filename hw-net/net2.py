from net import Net
net = Net()

x = net.variable(1)
y = net.variable(2)
z = net.variable(3)

x2 = net.mul(x, x)
y2 = net.mul(y, y)
z2 = net.mul(z, z)

o1 = net.add(x2, y2)
o2 = net.add(o1, z2)

net.gradient_descendent()
print('x=', x.v, 'y=', y.v, 'z=', z.v)