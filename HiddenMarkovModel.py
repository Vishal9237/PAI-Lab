states = ['Rainy','Sunny']
observations = ['Walk','Shop','Clean']

ini_probs = {
    'Rainy':0.6,
    'Sunny':0.4
}

trans_probs = {
    'Rainy':{'Rainy':0.7,'Sunny':0.3},
    'Sunny':{'Rainy':0.4,'Sunny':0.6}
}

emission_probs = {
    'Rainy':{'Walk':0.1,'Shop':0.4,'Clean':0.5},
    'Sunny':{'Walk':0.6,'Shop':0.3,'Clean':0.1}
}

obs_seq = ['Walk','Shop','Clean']
obs_seq_len = len(obs_seq)

def forward_algo(ini_probs,trans_probs,emission_probs,obs_seq):
  forward_t0 = {}
  for state in states:
    forward_t0[state] = ini_probs[state] * emission_probs[state][obs_seq[0]]

  forward = [forward_t0]

  for t in range(1, len(obs_seq)):
    forward_t = {}
    for state in states:
      sum_over_prev_states = 0
      for prev_state in states:
        sum_over_prev_states += forward[t-1][prev_state] * trans_probs[prev_state][state]
      forward_t[state] = sum_over_prev_states * emission_probs[state][obs_seq[t]]
    forward.append(forward_t)

  total_prob = sum(forward[-1][state] for state in states)
  return total_prob

result = forward_algo(ini_probs,trans_probs,emission_probs,obs_seq)
print('HMM Val:',result)
