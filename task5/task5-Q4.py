import math 
import matplotlib.pyplot as plt
import numpy as np
class BivariateGaussian:
    def __init__(self,mean_x,mean_y,var_x,var_y,cov):
        self.mean_x=mean_x
        self.var_x=var_x
        self.mean_y=mean_y
        self.var_y=var_y
        self.std_x=math.sqrt(var_x)
        self.std_y=math.sqrt(var_y)
        self.cov=cov
        self.const=-0.5/(1-((cov**2)/(var_x*var_y)))
        self.rho=cov/(self.std_x*self.std_y)
        self.coeff=1/(2*math.pi*self.std_x*self.std_y*math.sqrt(1-((cov**2)/(var_x*var_y))))
        self.marginal_xconst=1/(math.sqrt(2*math.pi)*self.std_x)
        self.marginal_yconst=1/(math.sqrt(2*math.pi)*self.std_y)
    # calcluating the joint pdf of bivariate gausian distribution for x and y
    def calculate_pdf(self,x,y):
        z=   self.const*((((x-self.mean_x)**2)/self.var_x )+(((y-self.mean_y)**2)/self.var_y) - ((2*self.rho*(x-self.mean_x)*(y-self.mean_y))/(self.std_x*self.std_y))) 
        return self.coeff*np.exp(z)
    # calculating marginal pdf of x
    def marginal_pdf_x(self,x):
        val=-0.5*((x-self.mean_x)**2/self.var_x)
        return self.marginal_xconst*math.exp(val)
    # calculating marginal pdf of y
    def marginal_pdf_y(self,y):
        val=-0.5*((y-self.mean_y)**2/self.var_y)
        return self.marginal_yconst*math.exp(val)
    # plotting pdf contour
    def plot_pdf_contour(self):
        x = np.linspace(self.mean_x - 3*self.std_x, self.mean_x + 3*self.std_x, 100)
        y = np.linspace(self.mean_y - 3*self.std_y, self.mean_y + 3*self.std_y, 100)
        X,Y=np.meshgrid(x,y)
        Z=self.calculate_pdf(X,Y)
        plt.figure(figsize=(10,6))
        plt.contour(X,Y,Z,cmap='viridis')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Bivariate Gaussian PDF Contour Plot')
        plt.colorbar(label='PDF Value')
        plt.grid(True)
        plt.show()

distribution=BivariateGaussian(2,3,1.2,2.1,0.5)
print(distribution.calculate_pdf(1,2))
print(distribution.marginal_pdf_x(2))
print(distribution.marginal_pdf_y(1))
distribution.plot_pdf_contour()



