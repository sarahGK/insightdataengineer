#------------------------------------------------------------DESCCRIPTION---------------------------------------------------------#
# The Viterbi algorithm is a dynamic programming algorithm for finding the most likely sequence of hidden states(Viterbi path).   #
# Especially in the context of Markov information sources and hidden Markov models.                                               #
# Widely used in speech recognition, speech synthesis, diarization, keyword spotting, computational linguistics,and bioinformatics#
#---------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------DESCCRIPTION---------------------------------------------------------#
# Parameters:
# states: a dictionary with the name of the state as the key and the index of the state as the value
# obsers: a dictionary with the name of the obersations as the key and the index of the state as the value
# init: the initial states probablities
# emiss: the emission probabilities
# seq: the observation sequence
#---------------------------------------------------------------------------------------------------------------------------------#
def viterbi(states,obsers,init,trans,emiss,seq):
    stat_seq = []
    temp1 = [[ 0 for i in range(0,len(seq))] for j in range(0,len(states))]
    temp2 = [[ 0 for i in range(0,len(seq))] for j in range(0,len(states))]
    print(temp1,'/n',temp2)

    for i in states.values():
        temp1[i][0] = init[i] * emiss[i][obsers[seq[0]]]
    print(temp1)

    for o in seq[1:]:
        j = obsers[o]
        for i in states.values():
            prob,k = maximize(temp1,trans,i,j)
            temp1[i][j] = emiss[i][j] * prob
            temp2[i][j] = k



#------------------------------------------------------------HELPER FUNCTION---------------------------------------------------------#
# output : a tuple -- maximum probability and its according state 
#---------------------------------------------------------------------------------------------------------------------------------#
def maximize(temp,trans,i,j):
    maxi = 0
    i = 0
    value = 0
    for k in range(0,len(trans)):
#        value = temp[k][i-1] * trans[k][j]
        if value > maxi:
            maxi = value
            i = k

    return maxi,i

#------------------------------------------------------------HELPER FUNCTION---------------------------------------------------------#
# output : the index with the maximum value 
#---------------------------------------------------------------------------------------------------------------------------------#
import numpy as np
def argmax(list):
    arr = np.asarray(list)
    return np.argmax(arr)


#------------------------------------------------------------EXAMPLE---------------------------------------------------------#
# states = ('Rainy', 'Sunny')
 
# observations = ('walk', 'shop', 'clean')
 
# start_probability = {'Rainy': 0.6, 'Sunny': 0.4}
 
# transition_probability = {
#   'Rainy' : {'Rainy': 0.7, 'Sunny': 0.3},
#   'Sunny' : {'Rainy': 0.4, 'Sunny': 0.6},
#   }
 
# emission_probability = {
#   'Rainy' : {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
#   'Sunny' : {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
#   }
#---------------------------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':

    states = { 'Rainy':0,
               'Sunny':1,
            }
    observations = {'walk':0,
                    'shop':1,
                    'clean':2
                    }

    state_initp = [0.6,0.4]
    state_transp = [ [0.7,0.3],
                     [0.4,0.6]
                    ]
    emiss_p = [ [0.1,0.4,0.5],
                [0.6,0.3,0.1]
            ]

    obser_seq = ('walk','shop','clean','shop')

    viterbi(states,observations,state_initp,state_transp,emiss_p,obser_seq)

    l = [0.1,0.3,0.4,0.25]
    k = argmax(l)
    print(k)

    
    
