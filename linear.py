import random
import matplotlib.pyplot as plt
from statistics import mean
import math

xs = [0.11360325954487849, 0.6175674753122118, 0.27936334840940424, 0.4611393228541354, 0.47273340697149313, 0.8779290169924265, 0.20552877260862257, 0.9483866352997756, 0.8051372748949086, 0.7482560528833611, 0.8111091255795059, 0.4543047912850148, 0.4568171455867005, 0.17730360990716232, 0.9768307878054276, 0.8545778985443001, 0.8793272824499492, 0.19012224356842056, 0.4009795107582318, 0.7179798252542361, 0.5061165276584828, 0.12678567673834884, 0.17445107282141126, 0.09908934915787015, 0.5507648003449744, 0.983383501170468, 0.7001869379128899, 0.9873067316694418, 0.7195685315355539, 0.5255125835418247, 0.6552042793480682, 0.3949363973419817, 0.5666306230538082, 0.912871021708838, 0.5673376622374758, 0.23294700760796805, 0.13568943979573256, 0.9572493545658876, 0.5899525016690911, 0.30106919465422055, 0.1325273084361891, 0.15613228203172014, 0.4606580812861538, 0.2718520606064926, 0.21583347747405623, 0.9057974074030204, 0.5085680269903684, 0.38692795925315393, 0.7735509658720459, 0.6033551103346234, 0.3318059662081235, 0.03986564552538485, 0.8728463577812485, 0.3476945395495966, 0.5208243109275007, 0.5274890886090933, 0.9740054948976523, 0.19881231715521908, 0.2927817187242181, 0.6154375537246695, 0.18709778412848743, 0.11791096065124518, 0.8750955485207845, 0.524319002020453, 0.6243215010461585, 0.23540255050224634, 0.1495413071522459, 0.37842326940506144, 0.4591236105733635, 0.8476567716774138, 0.044002943500390024, 0.46959049416707344, 0.9553604004146984, 0.43268457134543803, 0.18457698104951814, 0.5169534234897956, 0.1158216801405969, 0.5548072940887923, 0.47154362761921775, 0.19931199256176646, 0.06839866813807793, 0.085962530497104, 0.7262443346218184, 0.45348032903219937, 0.4317517740871931, 0.7724150283503761, 0.11002074924354355, 0.812597868269224, 0.1262846516678804, 0.06834432783544164, 0.1747515501882595, 0.09175604411229576, 0.661912840161717, 0.3267002049141523, 0.9798626588170444, 0.6679469611877132, 0.2793087667083717, 0.286959261259077, 0.35619917583157723, 0.5013431931444129]
ys = [0.3125298484101426, 0.714539736769698, 0.7950522596649024, 0.9669153186432893, 0.8709652578573104, 1.8093283926773172, 0.570064383360865, 1.4552574661731843, 1.9117463927440306, 1.0557418897346336, 1.4576948211220229, 1.4955481403198818, 1.1788781739586045, 0.6233907933096023, 1.3232807431928983, 1.1402883564216368, 1.6873266994591163, 0.7247199517836492, 0.3211903118615068, 1.0301871383710617, 0.803459212887557, 0.36932286030825046, 0.7696539238661263, 0.4782362521383379, 1.0689119122183293, 1.3131050557059556, 1.7748468292204793, 0.873104757465986, 1.3841530482894422, 1.117271098192619, 1.2528292206647114, 0.7959812990922204, 0.8276912376230969, 1.5239956818979514, 1.4171584912324011, 0.18515873322086535, 0.4116384784259741, 1.8781119851278634, 0.4800997273569044, 0.5820784567055006, 0.5127489583313176, 0.6424315449164455, 1.0804473736049223, 0.38672027507098883, 0.8794573472170286, 1.8263727646818801, 0.8801447577406115, 0.4233518654565696, 1.4820972582120258, 1.278605733349128, 0.8547886217034861, 0.3077814326352513, 1.2929505608945997, 0.5949891768629255, 1.2193957256273902, 1.1148633618539043, 1.4033329800345282, 0.03887567215732585, 0.8211208780480757, 1.4020614190730005, 0.3337258517183215, 0.5025029827792136, 1.6268500980896654, 0.41204434575279314, 1.069367960986499, 0.7105137921808433, 0.3357698456087497, 0.7983148793074234, 0.633319308401304, 0.9094845352563807, 0.2489011955892243, 1.1333620516339846, 1.5582288932198822, 0.6770399219463202, 0.12541318100080678, 1.1051325333822488, 0.6697629768424262, 1.075779719901427, 0.8103718942168258, 0.4651540430788196, -0.013126715817264434, 0.2871018804482887, 1.1276395757656044, 0.8965092468579632, 0.5225136630080731, 1.4116536044685792, 0.373320836618978, 1.7476384795200712, 0.3311646134058262, 0.1303099699393371, 0.12757587838952655, 0.593978006446019, 1.8437798705859587, 0.6903521591893421, 1.8152213132518493, 1.3189521647556812, 0.4660673569020709, 0.626782216816369, 0.4628734030960964, 1.2467513643851065]


def regress_normal(xs, ys):
    '''
    :param xs: List of x coordinates of data points.
    :param ys: List of y coordinates of data points.
    :return: The intercept and slope of the best line through xs and ys.
    '''
    xbar = mean(xs)
    ybar = mean(ys)
    top, bottom = 0, 0

    for i in range(len(xs)):
        top += (xs[i] - xbar) * (ys[i] - ybar)
        bottom += (xs[i] - xbar)**2

    b1 = top/bottom
    b0 = ybar - (b1 * xbar)
    return b0, b1


def predict(x, b0, b1):
    '''
    :param x: The x value in question.
    :param b0: Intercept of the line.
    :param b1: Slope of the line.
    :return: The predicted value of y.
    '''
    return b0 + (b1 * x)


def sse(b0, b1):
    '''
    :param b0: Intercept of the line.
    :param b1: Slope of the line.
    :return: The sum of squared errors between the line and the actual values in ys.
    '''
    error = 0
    for i in range(len(xs)):
        error += (predict(xs[i], b0, b1) - ys[i])**2
    return error



def gradient_descent_2d(f):
    '''
    :param f: A function of two arguments.
    :return: The values x and y that minimize f(x, y).
    '''
    epsilon = 0.001
    learning_rate = 0.0001
    x = random.random()
    y = random.random()
    while True:
        # Compute approximated gradient
        x1 = x + epsilon
        y1 = y + epsilon
        z = f(x, y)
        gx = (f(x1, y) - z) / (x1 - x)  # Partial derivative with respect to x
        gy = (f(x, y1) - z) / (y1 - y)  # Partial derivative with respect to y
        # Time to stop?
        if math.sqrt(gx ** 2 + gy ** 2) < epsilon:
            return x, y
        # Take a step
        x -= learning_rate * gx
        y -= learning_rate * gy


b0, b1 = regress_normal(xs, ys)
print(b0, b1)
c0, c1 = gradient_descent_2d(sse)
print(c0, c1)

plt.plot([0, 1], [predict(0, b0, b1), predict(1, b0, b1)], label='normal equation')
plt.plot([0, 1], [predict(0, c0, c1), predict(1, c0, c1)], label='gradient descent')
plt.scatter(xs, ys, label='data')
plt.legend()
plt.show()
