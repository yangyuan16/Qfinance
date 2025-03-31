import numpy as np

def get_A(A_0,x, r_fall):
     return (A_0 + x) * (1-r_fall)

def get_B(B_0, x):
     return B_0 + x

def get_additon_money(A,B,r_fall_upto): # additional investment for averaging down
    return (B*(1-r_fall_upto)-A) / r_fall_upto


if __name__ == "__main__":
    print()

    #r_fall_list = [0.02,0.02,0.02,0.02,0.02,0.02,0.02] # price falls ratio
    #r_fall_upto_list = [0.01,0.01,0.01,0.01,0.01,0.01,0.01] # by increasing the long side to decrase the price fall raio
    r_fall_list = [0.17]
    r_fall_upto_list = [0.01]
    A_inital = 0 # inital money
    B_inital = 0 # inital money
    x = 100  # first buy
    print("first buy %d yuan:"%x)
    for it in range(len(r_fall_list)):
      A = get_A(A_0=A_inital, x=x, r_fall=r_fall_list[it])
      B = get_B(B_0=B_inital, x=x)
      print("after %d time drop %g ratio of price"%(it+1,r_fall_list[it]))
      print("money invest %g yuan, but money becomes %g yuan"%(B,A))
      x_new = get_additon_money(A=A, B=B, r_fall_upto=r_fall_upto_list[it])
      print("For decrease the fall ratio form %g to %g, should increase the investment %g yuan"%(r_fall_list[it],r_fall_upto_list[it],x_new))
      print("------------------------------------------------------------")
      A_inital = A
      B_inital = B
      x = x_new



